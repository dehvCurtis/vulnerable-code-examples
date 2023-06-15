<!-- User-provided data, such as URL parameters, should always be considered untrusted and tainted. Constructing class or method names directly from tainted data enables attackers to inject specially crafted values that could result in unexpected behavior, e.g. crash of the application. -->

<!-- 
    OWASP Top 10 2021 Category A3 - Injection
    OWASP Top 10 2017 Category A1 - Injection
    MITRE, CWE-470 - Use of Externally-Controlled Input to Select Classes or Code ('Unsafe Reflection') 
-->

<?php

$input = $_GET["input"];

call_user_func($input, "abc"); # Noncompliant
$input(); # Noncompliant
$o = new $input(); # Noncompliant

?>
