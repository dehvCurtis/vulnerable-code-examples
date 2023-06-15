import os

def insecure_function(password):
    print("Received password: " + password)

user_input = "sensitivePassword"
insecure_function(user_input)

# (CWE-359)
# This sample Python file contains a function that prints a password to the console without any security measures.
# It can be used to test SAST tools' ability to identify sensitive information exposure.