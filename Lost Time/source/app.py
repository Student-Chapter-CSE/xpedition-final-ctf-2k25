from flask import Flask, request, render_template_string, redirect, make_response
import jwt
import datetime

app = Flask(__name__)

with open('private_key.pem', 'rb') as f:
    PRIVATE_KEY = f.read()

with open('public_key.pub', 'rb') as f:
    PUBLIC_KEY = f.read()

with open('flag.txt', 'r') as f:
    FLAG = f.read().strip()

def generate_token(username):
    payload = {
        "username": username,
        "currentDate": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    }
    return jwt.encode(payload, PRIVATE_KEY, algorithm="EdDSA")


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        username = request.form.get("username")
        token = generate_token(username)
        response = make_response(redirect("/return-stone"))
        response.set_cookie("auth", token)
        return response
    return '''
        <h3>Enter your username to return the time stone</h3>
        <form method="post">
            <label>Enter your username:</label>
            <input type="text" name="username" required>
            <button type="submit">Submit</button>
        </form>
    '''


@app.route("/return-stone")
def return_stone():
    token = request.cookies.get("auth")
    if not token:
        return "No token found! Please go back and enter your username.", 403

    try:
        payload = jwt.decode(
            token, PUBLIC_KEY, algorithms=jwt.algorithms.get_default_algorithms())
        username = payload["username"]

        if "PRIVATE_KEY" in username or "FLAG" in username:
            username = "Human!"

        current_date = datetime.datetime.strptime(
            payload["currentDate"], "%Y-%m-%d")
        deadline = datetime.datetime(2025, 3, 20)

        if current_date < deadline:
            message = '''
            {% if username %}
            Hello ''' + username + '''
            {% endif %}
            <br>
            Congratulations! You just saved the world!!!
            <br>
            <br>
            Heres a gift for you: {{FLAG}}
            '''
        else:
            message = '''
            {% if username %}
            Hello ''' + username + '''
            {% endif %}
            <br>
            You are late! The world was destroyed!!
            '''

        return render_template_string(message, username=username, **globals())

    except jwt.ExpiredSignatureError:
        return "Token expired!", 403
    except jwt.InvalidTokenError:
        return "Invalid token!", 403


if __name__ == "__main__":
    app.run(debug=True)
