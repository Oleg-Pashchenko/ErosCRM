import psycopg2
import dotenv
import os


class Postgres:
    dotenv.load_dotenv()
    database = os.getenv("POSTGRES_DATABASE")
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def get_connection(self):
        conn = psycopg2.connect(
            database=self.database,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
        )
        cur = conn.cursor()
        return conn, cur

    def commit_statement(self, sql, params):
        conn, cur = self.get_connection()
        cur.execute(sql, params)
        conn.commit()
        conn.close()

    def insert(self, sql, params):
        self.commit_statement(sql, params)

    def update(self, sql, params):
        self.commit_statement(sql, params)

    def select_one(self, sql, params):
        conn, cur = self.get_connection()
        cur.execute(sql, params)
        row = cur.fetchone()
        conn.close()
        return row

    def select_all(self, sql, params):
        conn, cur = self.get_connection()
        cur.execute(sql, params)
        rows = cur.fetchall()
        conn.close()
        conn.close()
        return rows
