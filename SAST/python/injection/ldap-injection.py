# The following noncompliant code is vulnerable 
# to LDAP injection because untrusted data is 
# concatenated to an LDAP query without prior 
# sanitization or validation.

from flask import request
import ldap

@app.route("/user")
def user():
    username =  request.args['username']

    search_filter = "(&(objectClass=user)(uid="+username+"))"

    ldap_connection = ldap.initialize("ldap://localhost:389")
    user = ldap_connection.search_s("dc=example,dc=org", ldap.SCOPE_SUBTREE, search_filter) # Noncompliant

    return user[0]