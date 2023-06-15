function insecureFunction(password) {
    console.log("Received password: " + password);
  }
  
  var userInput = "sensitivePassword";
  insecureFunction(userInput);

// (CWE-359)
// This sample JavaScript file contains an insecure function that logs a password to the console. 
// It can be used to test SAST tools' ability to identify sensitive information exposure.