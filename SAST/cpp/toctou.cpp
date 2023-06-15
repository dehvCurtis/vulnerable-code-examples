// "Time Of Check to Time Of Use" (TOCTOU) vulnerabilities occur when an application:

//     First, checks permissions or attributes of a file: for instance, is a file a symbolic link?
//     Next, performs some operations such as writing data to this file.

#include <stdio.h>

void fopen_with_toctou(const char *file) {
  if (access(file, F_OK) == -1 && errno == ENOENT) {
    // the file doesn't exist
    // it is now created in order to write some data inside
    FILE *f = fopen(file, "w"); // Noncompliant: a race condition window exist from access() call to fopen() call calls
    if (NULL == f) {
      /* Handle error */
    }

    if (fclose(f) == EOF) {
      /* Handle error */
    }
  }
}


    // OWASP Top 10 2021 Category A1 - Broken Access Control
    // OWASP Top 10 2017 Category A5 - Broken Access Control
    // MITRE, CWE-367 - Time-of-check Time-of-use (TOCTOU) Race Condition
    // CERT, FIO45-C. - Avoid TOCTOU race conditions while accessing files
