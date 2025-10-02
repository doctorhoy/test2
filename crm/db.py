import json
import sqlite3
from sqlite3 import Connection


def init_db(db_path: str = "crm.db") -> Connection:
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS leads ("
        "id TEXT PRIMARY KEY,"
        "data TEXT NOT NULL"
        ")"
    )
    conn.commit()
    return conn


def save_leads(conn: Connection, leads: list):
    cur = conn.cursor()
    for lead in leads:
        cur.execute(
            "INSERT OR IGNORE INTO leads (id, data) VALUES (?, ?)",
            (lead.get("id"), json.dumps(lead)),
        )
    conn.commit()
