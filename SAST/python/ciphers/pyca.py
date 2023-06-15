# Strong cipher algorithms are cryptographic systems resistant to 
# cryptanalysis, they are not vulnerable to well-known attacks like 
# brute force attacks for example.

# It’s not recommended to use algorithm with a block size inferior 
# than 128 bits.

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

key = os.urandom(16)
iv = os.urandom(16)

tdes4 = Cipher(algorithms.TripleDES(key), mode=None, backend=default_backend()) # Noncompliant: Triple DES is vulnerable to meet-in-the-middle attack
bf3 = Cipher(algorithms.Blowfish(key), mode=None, backend=default_backend()) # Noncompliant: Blowfish use a 64-bit block size makes it vulnerable to birthday attacks
rc42 = Cipher(algorithms.ARC4(key), mode=None, backend=default_backend()) # Noncompliant: vulnerable to several attacks (see https://en.wikipedia.org/wiki/RC4#Security

    # OWASP Top 10 2021 Category A2 - Cryptographic Failures
    # OWASP Top 10 2017 Category A6 - Security Misconfiguration
    # MITRE, CWE-327 - Use of a Broken or Risky Cryptographic Algorithm
    # SANS Top 25 - Porous Defenses