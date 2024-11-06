from flask import Flask, render_template
from flask_mysqldb import MySQL
import base64

app = Flask(__name__)

# Cấu hình kết nối MySQL
app.config['MYSQL_HOST'] = 'your_host'
app.config['MYSQL_USER'] = 'your_username'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'your_database'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/header')
def header():
    return render_template('header.html')

@app.route('/left_content')
def left_content():
    return render_template('left-content.html')

@app.route('/identification')
def identification():
    # Truy vấn cơ sở dữ liệu để lấy đường dẫn ảnh mới nhất
    cur = mysql.connection.cursor()
    cur.execute("SELECT image_path FROM detected ORDER BY ID DESC LIMIT 1")
    image_data = cur.fetchone()

    if image_data:
        image_path = image_data[0]  # Lấy đường dẫn ảnh
    else:
        image_path = None

    return render_template('identification.html', image_path=image_path)

@app.route('/analysis')
def analysis():
    return render_template('analysis.html')

@app.route('/storage')
def storage():
    return render_template('storage.html')

if __name__ == "__main__":
    app.run(debug=True)