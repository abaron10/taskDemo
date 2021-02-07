from flask import Flask, render_template,json,request,url_for
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database/task.db'
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('index.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)