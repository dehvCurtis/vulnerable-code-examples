# The following noncompliant code example is vulnerable 
# to open redirection as it constructs a URL with 
# user-controllable data. This URL is then used to 
# redirect the user without being first validated. An 
# attacker can leverage this to manipulate users into 
# performing unwanted redirects.

from flask import Flask, redirect

app = Flask("example")

@app.route("/redirect")
def redirect():
    url = request.args["url"]
    return redirect(url) # Noncompliant