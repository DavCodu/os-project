import os
import time
from flask import Flask
import mysql.connector

app = Flask(__name__)

def get_db_connection():
   
    for i in range(5):
        try:
            connection = mysql.connector.connect(
                host=os.environ.get('DB_HOST', 'localhost'),
                user=os.environ.get('DB_USER', 'root'),
                password=os.environ.get('DB_PASSWORD', 'my-super-secret-password'),
                database=os.environ.get('DB_NAME', 'os_db')
            )

            return connection
        except mysql.connector.Error:
            print("Базата данни все още зарежда... нов опит след 2 сек.")
            time.sleep(2)
    return None

@app.route('/')
def index():
    conn = get_db_connection()
    if conn and conn.is_connected():
        conn.close()
        return "<h1>Успех! Python се свърза с MySQL базата данни вътре в Docker! 🚀</h1>"
    else:
        return "<h1>Грешка! Връзката с базата данни пропадна. ❌</h1>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)