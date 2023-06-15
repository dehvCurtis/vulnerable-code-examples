# The following code is vulnerable to log injection as it constructs
# log entries using untrusted data. An attacker can leverage this to
# manipulate the chain of events being recorded.

import logging

app = Flask(__name__)

@app.route('/example')
def log():
    data = request.args["data"]
    app.logger.critical("%s", data) # Noncompliant