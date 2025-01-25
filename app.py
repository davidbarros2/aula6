from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Configuração do banco de dados
DB_CONFIG = {
    'dbname': 'mydatabase',
    'user': 'myuser',
    'password': 'mypassword',
    'host': 'db',
    'port': 5432
}

@app.route('/')
def home():
    return "Hello, Docker Compose with PostgreSQL!"

@app.route('/data')
def get_data():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM example_table;")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
