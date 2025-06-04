import argparse

from .meta import fetch_leads
from .db import init_db, save_leads


def run_sync(token: str, leadgen_form_id: str, db_path: str):
    conn = init_db(db_path)
    leads = fetch_leads(token, leadgen_form_id)
    save_leads(conn, leads)
    print(f"Saved {len(leads)} leads to {db_path}")


def main():
    parser = argparse.ArgumentParser(description="Simple CRM for Meta leads")
    subparsers = parser.add_subparsers(dest="command")

    sync_parser = subparsers.add_parser("sync", help="Fetch leads from Meta")
    sync_parser.add_argument("leadgen_form_id", help="Lead generation form ID")
    sync_parser.add_argument("--token", required=True, help="Meta access token")
    sync_parser.add_argument("--db", default="crm.db", help="SQLite DB path")

    args = parser.parse_args()

    if args.command == "sync":
        run_sync(args.token, args.leadgen_form_id, args.db)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
