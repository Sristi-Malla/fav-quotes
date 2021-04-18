from flask import Flask ,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:password@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://zuyadbjldlivnb:15c9e3fa3e608c019434213ee2b9a4a29404e6d6c0ee661ccccbdecc53b98751@ec2-34-233-0-64.compute-1.amazonaws.com:5432/d7a5pf53dblfsk'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy()

class Favquotes(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	author = db.Column(db.String(30))
	quote = db.Column(db.String(2000))


@app.route('/')
def index():
	result = Favquotes.query.all()
	return render_template('index.html',result=result)


@app.route('/quotes')
def quotes():
	 return render_template('quotes.html')

@app.route('/process', methods =['POST'])
def process():
	author = request.form['author']
	quote = request.form['quote']
	quotedata =Favquotes(author=author,quote=quote)
	db.session.add(quotedata)
	db.session.commit()

	return redirect(url_for('index'))




   	  #else:
		 #return render_template('quotes.html')
