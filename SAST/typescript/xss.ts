// File: sample.ts

const userInput = '<script>alert("XSS vulnerability");</script>';
const message = `Hello, ${userInput}!`;
document.getElementById('output').innerHTML = message;

// Cross-Site Scripting (XSS) (CWE-79)
// This example demonstrates a cross-site scripting (XSS) vulnerability by directly injecting user input into HTML content without proper sanitization. SAST tools can detect this vulnerability and suggest using appropriate encoding or escaping mechanisms to prevent XSS attacks.