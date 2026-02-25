import os
import sys
import psycopg

def main() -> int:
    dsn = os.environ.get("DATABASE_URL")
    if not dsn:
        print("DATABASE_URL is not set", file=sys.stderr)
        return 2

    message = sys.argv[1] if len(sys.argv) > 1 else "hello from docker action"

    with psycopg.connect(dsn) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS action_events (
                    id SERIAL PRIMARY KEY,
                    message TEXT NOT NULL,
                    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
                );
            """)
            cur.execute("INSERT INTO action_events (message) VALUES (%s);", (message,))
            conn.commit()

    print("Inserted row into action_events.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())