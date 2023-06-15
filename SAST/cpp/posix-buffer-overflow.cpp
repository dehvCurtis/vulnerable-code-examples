char array[10];
initialize(array);
void *pos = memchr(array, '@', 42); // Noncompliant, buffer overflow that could expose sensitive data


    // OWASP Top 10 2017 Category A9 - Using Components with Known Vulnerabilities
    // MITRE, CWE-119 - Improper Restriction of Operations within the Bounds of a Memory Buffer
    // MITRE, CWE-131 - Incorrect Calculation of Buffer Size
    // MITRE, CWE-788 - Access of Memory Location After End of Buffer
    // CERT, ARR30-C. - Do not form or use out-of-bounds pointers or array subscripts
    // CERT, STR50-CPP. - Guarantee that storage for strings has sufficient space for character data and the null terminator
