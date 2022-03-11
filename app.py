from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# creates an object of the flask class
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class CliffordBlog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False)
    posted_by = db.Column(db.String(20), nullable=False, default='N/A')
    posted_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    # helps to define a string representation for the db object
    def __repr__(self):
        return self.title

db.create_all()
db.session.commit()

# creates a route decorator
# this links the /home url to the welcome function
@app.route('/')
@app.route('/clifford')
@app.route('/home')
def Welcome():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

