from flask import Flask, request, render_template, redirect
import cgi
import string

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/validate", methods=['POST'])
def validate():
    username = request.form['username']
    pass1 = request.form['pass1']
    pass2 = request.form['pass2']
    email = request.form['email']
# Scanning username for length between 3 and 20 (inclusive) and spaces
    if " " in username:
        username_error = "DENIED: Agent Name Cannot Contain Spaces"
    else:
        username_error = ""
    if len(username) < 3 or len(username) > 20:
        username_error = "DENIED: Agent Name Length"
# Scanning password for length between 3 and 20 (inclusive) and spaces
    if " " in pass1:
        pass_error = "DENIED: Codephrase Cannot Contain Spaces"
    else:
        pass_error = ""
    if len(pass1) < 3 or len(pass1) > 20:
        pass_error = "DENIED: Codephrase Name Length"
    if pass1 != pass2:
        pass_error = "DENIED: Codephrase Confirmation Invalid"
# Scanning email for length and appropriate characters (no space but @ and .)
    if " " in email:
        email_error = "DENIED: Invalid Email"
    if "@" not in email:
        email_error = "DENIED: Invalid Email"
    if "." not in email:
        email_error = "DENIED: Invalid Email"
    if len(email) > 0 and (len(email) < 3 or len(email) > 20):
        email_error = "DENIED: Invalid Email Length"
    else:
        email_error = ""
# Checks for no errors, redirecting to a Welcome page instead.  Else goes back to form.
    if len(username_error)== 0 and len(pass_error)== 0 and len(email_error)== 0:
        return render_template("welcome.html", username=username)
    else:
        return render_template("signup.html",
        username=username,
        username_error=username_error,
        pass_error=pass_error,
        email=email, email_error=email_error)

@app.route("/")
def index():
    return render_template("signup.html")

app.run()
