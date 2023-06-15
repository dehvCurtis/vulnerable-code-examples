void f(char *password, size_t bufferSize) {
  char localToken[256];
  init(localToken, password);
  memset(password, ' ', strlen(password)); // Noncompliant, password is about to be freed
  memset(localToken, ' ', strlen(localToken)); // Noncompliant, localToken is about to go out of scope
  free(password);
}

    // OWASP Top 10 2017 Category A3 - Sensitive Data Exposure
    // MITRE, CWE-14 - Compiler Removal of Code to Clear Buffers
