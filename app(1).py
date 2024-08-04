from flask import Flask, request, render_template, request, url_for, flash
import secrets
from sqlalchemy import exc
from models import db

app = Flask(__name__, template_folder = 'templates', static_folder = 'static')
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)


@app.route('/')
def index():
    return render_template ('index.html')



if __name__ == '__main__':
    app.run(debug = True)