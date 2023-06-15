// The Element.innerHTML property is used to replace the contents of the
// root element with user-supplied contents. The innerHTML property does 
// not sanitize its input, thus allowing for code injection.

const rootEl = document.getElementById('root');
const queryParams = new URLSearchParams(document.location.search);
const input = queryParams.get("input");

rootEl.innerHTML = input; // Noncompliant

// OWASP Top 10 2021 Category A3 - Injection
// OWASP Top 10 2017 Category A7 - Cross-Site Scripting (XSS)
// MITRE, CWE-79 - Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
// SANS Top 25 - Insecure Interaction Between Components
