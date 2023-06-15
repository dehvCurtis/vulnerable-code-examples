# The following code is vulnerable to arbitrary code execution because it runs dynamic Python code based on untrusted data.

from flask import request

@app.route("/")
def example():
    operation = request.args.get("operation")
    eval(f"product_{operation}()") # Noncompliant
    return "OK"