from flaskapp import app, db, mail
from flask import render_template, url_for
from flask import request, flash, redirect
# from flaskapp.model import User
from flaskapp.form import SurveyForm
from flask_mail import Message

@app.route('/', methods = ['POST', 'GET'])
def form():
    form = SurveyForm()
    if form.validate_on_submit():
        # user = User(name=form.name.data, email=form.email.data)
        # db.session.add(user)
        # db.session.commit()

        body = """
        Thank you {} for filling the form!😊
        """.format(form.name.data)
        msg = Message(subject="survey form", sender='', recipients=[form.email.data], body=body)
        

        mail.send(msg)
        flash('Your feedback is successfully submitted!!', 'success')
        return redirect(url_for('thank'))
    return render_template('form.html', form=form)

@app.route('/thank')
def thank():
    return render_template('thank.html')
