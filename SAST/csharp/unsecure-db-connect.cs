// When relying on the password authentication mode for the 
// database connection, a secure password should be chosen.

protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
{
  optionsBuilder.UseSqlServer("Server=myServerAddress;Database=myDataBase;User Id=myUsername;Password="); // Noncompliant
}

    // OWASP Top 10 2021 Category A7 - Identification and Authentication Failures
    // OWASP Top 10 2017 Category A2 - Broken Authentication
    // OWASP Top 10 2017 Category A3 - Sensitive Data Exposure
    // MITRE, CWE-521 - Weak Password Requirements