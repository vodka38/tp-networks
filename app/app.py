from flask import Flask, jsonify
import pymysql
import os
import time

app = Flask(__name__)

DB_HOST = os.getenv('DB_HOST', 'db')
DB_USER = os.getenv('DB_USER', 'appuser')
DB_PASS = os.getenv('DB_PASS', 'apppass123')
DB_NAME = os.getenv('DB_NAME', 'mydb')

def get_db_connection(retries=10, delay=3):
    for i in range(retries):
        try:
            conn = pymysql.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASS,
                database=DB_NAME,
                cursorclass=pymysql.cursors.DictCursor
            )
            print(f"Connexion à {DB_HOST} réussie !")
            return conn
        except Exception as e:
            print(f"Tentative {i+1}/{retries} échouée : {e}")
            if i < retries - 1:
                time.sleep(delay)
    raise Exception("Impossible de se connecter à la base de données")

@app.route('/')
def home():
    return "Hello from app!"

@app.route('/users')
def get_users():
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
        conn.close()
        return jsonify(users)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)