# A policy that grants all permissions may indicate an improper access control, which violates the principle of least privilege.

#     OWASP Top 10 2021 Category A1 - Broken Access Control
#     AWS Documentation - Grant least privilege
#     Google Cloud Documentation - Understanding roles
#     MITRE, CWE-732 - Incorrect Permission Assignment for Critical Resource
#     MITRE, CWE-284 - Improper Access Control
#     OWASP Top 10 2017 Category A5 - Broken Access Control

# AWS
resource "aws_iam_policy" "example" {
  name = "noncompliantpolicy"

  policy = jsonencode({
    Version   = "2012-10-17"
    Statement = [
      {
        Action   = [
          "*" # Sensitive
        ]
        Effect   = "Allow"
        Resource = [
          aws_s3_bucket.mybucket.arn
        ]
      }
    ]
  })
}

# GCP
resource "google_project_iam_binding" "example" {
  project = "example"
  role    = "roles/owner" # Sensitive

  members = [
    "user:jane@example.com",
  ]
}
