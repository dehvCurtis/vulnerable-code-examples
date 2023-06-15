<?php
// File: sample.php

$password = "sensitivePassword";
echo "Received password: " . $password;
?>

<!-- (CWE-259)
This sample PHP file demonstrates a simple echo statement that exposes a hardcoded password.
It can be used to test SAST tools' capability to detect hardcoded passwords. -->