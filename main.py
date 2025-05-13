from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Railway + FastAPI"}

@app.get("/db")
def read_db_time():
    try:
        conn = psycopg2.connect(
            host=os.environ["PGHOST"],
            database=os.environ["PGDATABASE"],
            user=os.environ["PGUSER"],
            password=os.environ["PGPASSWORD"],
            port=os.environ.get("PGPORT", 5432)
        )
        cur = conn.cursor()
        cur.execute("SELECT NOW();")
        db_time = cur.fetchone()
        cur.close()
        conn.close()
        return {"db_time": db_time}
    except Exception as e:
        return {"error": str(e)}