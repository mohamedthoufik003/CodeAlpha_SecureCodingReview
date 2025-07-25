from flask import Flask, request, render_template

app = Flask(__name__)

# Hardcoded users (insecure)
users = {
    "admin": "admin123",
    "user": "password"
}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:
            return f"Welcome, {username}!"
        else:
            return "Invalid credentials", 401

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
