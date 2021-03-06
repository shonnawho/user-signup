from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2
import re


template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    template = jinja_env.get_template('signup_form.html')
    return template.render()


#app.route('/signup')
#def display_signup_form():
   #return render_template('signup_form.html', username='', username_error='', password_error='')

valid_email = re.compile("\w+@\w+.(net|edu|com|org)")

@app.route('/signup', methods=['POST'])
def validate_signup():

    username = request.form['username']
    password_input = request.form['password_input']
    password_verify = request.form['password_verify']
    email = request.form['email']

    
    password_error = ''
    username_error = ''
    password_verify_error = ''
    email_error = ''

    
        
    if len(username) < 3 or len(username) > 20:
        username_error = 'Invaild username'


    
    if len(password_input) < 3 or len(password_input) > 20:
        password_error = 'Invaild password'
            

    if password_input != password_verify:
        password_verify_error = 'Passwords do not match'
    
    if email:
    
        if valid_email.match(email):
            email_error = 'invalid email'



        if len(email) < 3 or len(email) > 20:
            email_error = 'invaild email'
        
    

    if username_error or password_error or email_error:
        password_input = ''
        password_verify = ''
        username = username
        return render_template('signup_form.html', username=username, password_error=password_error, username_error=username_error, password_input=password_input,
         password_verify_error=password_verify_error,email_error=email_error) 
                
        
        
    else:
        template = jinja_env.get_template('signup_form.html')
        return redirect('/vaild-signup?username={0}'.format(username))

        


@app.route('/vaild-signup', methods=['GET'])
def vaild_signup():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()