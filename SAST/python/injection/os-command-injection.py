# The following code is vulnerable to command injections because 
# it is using untrusted inputs to set up a new process. Therefore 
# an attacker can execute an arbitrary program that is installed 
# on the system.

def ping():
    cmd = "ping -c 1 %s" % request.args.get("host", "www.google.com")
    status = os.system(cmd) # Noncompliant
    return str(status == 0)