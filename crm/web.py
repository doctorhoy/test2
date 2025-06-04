import argparse
import json
from flask import Flask, render_template_string, request, redirect, url_for

from .db import init_db, save_leads
from .meta import fetch_leads

TEMPLATE = """
<!DOCTYPE html>
<html lang='es'>
<head>
    <meta charset='utf-8'>
    <title>Simple CRM</title>
</head>
<body>
    <h1>Clientes potenciales</h1>
    <form method="post" action="/sync">
        <label>Form ID: <input type="text" name="form_id" required></label>
        <label>Token: <input type="text" name="token" required></label>
        <button type="submit">Sincronizar</button>
    </form>
    <ul>
    {% for lead in leads %}
        <li><pre>{{ lead | tojson(indent=2) }}</pre></li>
    {% else %}
        <li>No hay clientes guardados.</li>
    {% endfor %}
    </ul>
</body>
</html>
"""

app = Flask(__name__)


def get_leads(db_path: str):
    conn = init_db(db_path)
    cur = conn.cursor()
    cur.execute("SELECT data FROM leads ORDER BY rowid DESC")
    return [json.loads(row[0]) for row in cur.fetchall()]


@app.route("/")
def index():
    leads = get_leads(app.config["DB_PATH"])
    return render_template_string(TEMPLATE, leads=leads)


@app.route("/sync", methods=["POST"])
def sync():
    token = request.form["token"]
    form_id = request.form["form_id"]
    conn = init_db(app.config["DB_PATH"])
    leads = fetch_leads(token, form_id)
    save_leads(conn, leads)
    return redirect(url_for("index"))


def main():
    parser = argparse.ArgumentParser(description="Web interface for the CRM")
    parser.add_argument("--db", default="crm.db", help="Ruta de la base de datos SQLite")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=5000)
    args = parser.parse_args()

    app.config["DB_PATH"] = args.db
    app.run(host=args.host, port=args.port)


if __name__ == "__main__":
    main()
