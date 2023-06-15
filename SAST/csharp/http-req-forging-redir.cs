// The following noncompliant code example is vulnerable 
// to open redirection as it constructs a URL with 
// user-controllable data. This URL is then used to redirect 
// the user without being first validated. An attacker can 
// leverage this to manipulate users into performing unwanted redirects.

using System.Web;
using System.Web.Mvc;

public class ExampleController : Controller
{
    [HttpGet]
    public void Redirect(string url)
    {
        Response.Redirect(url);
    }
}

    // OWASP Top 10 2021 Category A1 - Broken Access Control
    // OWASP Top 10 2017 Category A5 - Broken Access Control
    // MITRE, CWE-20 - Improper Input Validation
    // MITRE, CWE-601 - URL Redirection to Untrusted Site ('Open Redirect')