from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Go to login page for login or welcome page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(f"Password entered: {password}")
        # Do something with the username and password
        return "Logged in successfully"
    return '''
        <form method="post">
            <p>Username: <input type="text" name="username"></p>
            <p>Password: <input type="password" name="password"></p>
            <input type="submit" value="Log In">
        </form>
    '''
if __name__ == '__main__':
    app.run(debug=True)