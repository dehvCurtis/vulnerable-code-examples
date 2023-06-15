<!-- Session Cookie Injection occurs when a web application assigns session cookies to users using untrusted data. -->

<!--  Session cookies are used by web applications to identify users. Thus, controlling these enable control over the identity of the users within the application. -->


<!-- OWASP Top 10 2021 Category A3 - Injection -->
    <!-- OWASP Top 10 2017 Category A1 - Injection -->
    <!-- MITRE, CWE-20 - Improper Input Validation -->
    <!-- MITRE, CWE-384 - Session Fixation -->

    <?php

use Symfony\Component\HttpFoundation\Cookie;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;

public function checkCookie(Request $request): Response
{
    $response = $this->render('/welcome.html');

    if (!$request->cookies->has('PHPSESSID')) {
        $value = $request->query->get('cookie');
        $cookie = Cookie::create('PHPSESSID', $value);
        $response->headers->setCookie($cookie); // Noncompliant
    }

    return $response;
}

?>
