# If a JSON Web Token (JWT) is not signed with a strong cipher algorithm 
# (or not signed at all) an attacker can forge it and impersonate user identities.

#     Don’t use none algorithm to sign or verify the validity of a token.
#     Don’t use a token without verifying its signature before.

import pyjwt

jwt.decode(token, verify = False)  # Noncompliant
jwt.decode(token, key, options={"verify_signature": False})  # Noncompliant