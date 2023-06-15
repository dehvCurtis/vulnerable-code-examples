# Strong cipher algorithms are cryptographic systems resistant to 
# cryptanalysis, they are not vulnerable to well-known attacks like 
# brute force attacks for example.

# It’s not recommended to use algorithm with a block size inferior 
# than 128 bits.

from Crypto.Cipher import *

des3 = DES.new('ChangeIt') # Noncompliant: DES works with 56-bit keys allow attacks via exhaustive search
tdes3 = DES3.new('ChangeItChangeIt') # Noncompliant: Triple DES is vulnerable to meet-in-the-middle attack
bf2 = Blowfish.new('ChangeItWithYourKey', Blowfish.MODE_CBC, 'ChangeIt') # Noncompliant: Blowfish use a 64-bit block size makes it
rc21 = ARC2.new('ChangeItWithYourKey', ARC2.MODE_CFB, 'ChangeIt') # Noncompliant: RC2 is vulnerable to a related-key attack
rc41 = ARC4.new('ChangeItWithYourKey') # Noncompliant: vulnerable to several attacks (see https://en.wikipedia.org/wiki/RC4#Security)


    # OWASP Top 10 2021 Category A2 - Cryptographic Failures
    # OWASP Top 10 2017 Category A6 - Security Misconfiguration
    # MITRE, CWE-327 - Use of a Broken or Risky Cryptographic Algorithm
    # SANS Top 25 - Porous Defenses
