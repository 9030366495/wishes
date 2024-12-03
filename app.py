from flask import Flask, render_template, request

app = Flask(__name__)

# Replace these with your friend's details
FRIEND_NAME = "MOHANA LAKSHMI"  # Replace with your friend's name
FRIEND_DOB = "2004-12-04"       # Replace with your friend's DOB in YYYY-MM-DD format

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    dob = request.form.get('dob')

    if username == FRIEND_NAME and dob == FRIEND_DOB:
        # Successful login
        return f"""
        <h1>Happy Birthday, {FRIEND_NAME}!</h1>
        <p>Wishing you a fantastic year ahead filled with joy and success!</p>
        <img src="static/happy_birthday.jpeg" alt="Happy Birthday" style="width:50%;">


        """
    else:
        # Invalid login
        return "<h2>Invalid login details. Please try again.</h2>"

if __name__ == '__main__':
    app.run(debug=True)
