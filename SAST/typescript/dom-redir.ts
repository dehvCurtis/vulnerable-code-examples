// The following example is vulnerable to open redirection through the 
// following URL: https://example.com/redirect?url=https://evil.com;

const queryParams = new URLSearchParams(document.location.search);
const redirectUrl = queryParams.get("url");
document.location = redirectUrl; // Noncompliant


// OWASP Top 10 2021 Category A1 - Broken Access Control
// OWASP Top 10 2017 Category A5 - Broken Access Control
// MITRE, CWE-20 - Improper Input Validation
// MITRE, CWE-601 - URL Redirection to Untrusted Site ('Open Redirect')
// SANS Top 25 - Risky Resource Management
