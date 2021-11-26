import psycopg2
import psycopg2.extensions


class db:
    def __init__(self) -> None:
        self.database = None
        self.DBNAME = "data"
        self.TNAME = "userdata"


    def get_conn(self):
        conn = psycopg2.connect(dbname='postgres', user='postgres', password='a', port='5432')
        conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()
        cursor.execute("SELECT datname FROM pg_catalog.pg_database WHERE datname='{}'".format(self.DBNAME))
        if not cursor.fetchone():
            cursor.execute("CREATE DATABASE {}".format(self.DBNAME))

        cursor.close()
        conn.close()

        conn = psycopg2.connect(dbname=self.DBNAME, user='postgres', password='a', port='5432')
        return conn

    def get_db(self):
        if not self.database:
            conn = self.get_conn()
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS {}(id text PRIMARY KEY, 
            name TEXT NOT NULL, email text, handle text, signin date, xp int DEFAULT 100, 
            solved json, recommended json DEFAULT '[]'::json, 
            qpd json DEFAULT '[]'::json, xp_pd json DEFAULT '[]'::json, rpd json DEFAULT '[]'::json)""".format(self.TNAME))
            cursor.execute("commit")
            self.database = cursor
        
        return self.database
