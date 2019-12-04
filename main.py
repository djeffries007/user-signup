from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True 

def is_invalid(inpt):
    if len(inpt) < 3 or len(inpt) > 20:
        return True
    elif ' ' in inpt:
        return True
    return False

def valid_email(inpt):
    if '@' in inpt:
        return True
    return False


@app.route('/login', methods=['POST', 'GET'])
def login():

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        email = request.form['email']

        if is_invalid(username) or not username:
            username_error = "That's not a valid username"
            username = ''

        if is_invalid(password) or not password:
            password_error = "That's not a valid password"
            password = ''

        if password != verify:
            verify_error = "Password doesn't match"
            verify = ''
        
        if email:
            if not valid_email(email):
                email_error = "That's not a valid email"
                email = ''   

        if not (username_error or password_error or verify_error or email_error):
            return redirect('/welcome?username={0}'.format(username))
    return render_template('login.html', username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error)

@app.route('/welcome', methods=['GET'])
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)



if __name__ == '__main__':
    app.run()