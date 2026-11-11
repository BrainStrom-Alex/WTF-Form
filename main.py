from flask import Flask, render_template, redirect, url_for
from flask_wtf import  FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, DataRequired, Email, Length
from flask_bootstrap import Bootstrap4

app = Flask(__name__)
app.secret_key = 'abc'

bootstrap = Bootstrap4(app)

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Enter a correct Email address')])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, message="Enter atleast 8 characters")])
    submit = SubmitField('Login')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return redirect(url_for('success'))
        else:
            return redirect(url_for('denied'))
    return render_template('login.html', form=form)

@app.route("/success.html")
def success():
    return render_template('success.html')

@app.route("/denied.html")
def denied():
    return render_template('denied.html')

if __name__ == '__main__':
    app.run(debug=True)
