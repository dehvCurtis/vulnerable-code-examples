# A public API, which can be requested by any authenticated or unauthenticated identities, can lead to unauthorized actions and information disclosures.

    # OWASP Top 10 2021 Category A1 - Broken Access Control
    # AWS Documentation - Controlling and managing access to a REST API in API Gateway
    # MITRE, CWE-284 - Improper Access Control
    # OWASP Top 10 2017 Category A5 - Broken Access Control

resource "aws_api_gateway_method" "noncompliantapi" {
  authorization = "NONE" # Sensitive
  http_method   = "GET"
}
