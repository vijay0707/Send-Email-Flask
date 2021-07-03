from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

app = Flask(__name__) 
 
app.config['SECRET_KEY'] = 'e0555713429c48c6713502c6fb4e042a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

 
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_DEFAULT_SENDER"]= 'flaskform00@gmail.com'
app.config["MAIL_USERNAME"] = 'flaskform00@gmail.com'
app.config["MAIL_PASSWORD"] = 'flasktest123'
mail = Mail(app) 


from flaskapp import routes