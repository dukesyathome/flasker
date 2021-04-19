from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# Create a flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "my super secret key 123"
# Create Form Class


class NamerForm(FlaskForm):
    name = StringField("What's Your Name", validators=[DataRequired()])
    submit = SubmitField("Submit")


# def index():
#   return "<h1>Hello World!</h1>"
'''
FILTERS
safe
capitalize
lower
upper
title
trim
striptags
'''


@app.route('/')
def index():
    first_name = "alan duke"
    stuff = "This is bold text"
    favorite_pizza = ["Pepperoni", "Cheese", "Mushroom"]
    return render_template("index.html",
                           first_name=first_name,
                           stuff=stuff,
                           favorite_pizza=favorite_pizza
                           )


@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)
    # return "<h1>Hello {}</h1>".format(name)


# Create Custom Error Pages

# Invalid url

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# Internal Serever Error


@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500


@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form Submitted Successfully!")

    return render_template("name.html", name=name, form=form)

