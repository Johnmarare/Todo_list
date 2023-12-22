from flask import render_template, url_for, flash, redirect
from flasktodo import app
from flasktodo.forms import RegistrationForm, LoginForm
from flasktodo.models import User, Task




posts = [
    {
        'author': 'John Musumba',
        'title': 'Todo list',
        'content': 'first content',
        'date_posted': 'April 20,2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Todo list',
        'content': 'first content',
        'date_posted': 'April 20,2018'
    }
]


@app.route("/")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'mararejohn@gmail.com' and form.password.data == 'password':
            flash('Succesfully Logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

