// File: sample.ts

const insecureRandom = Math.random();
console.log(`Insecure random number: ${insecureRandom}`);

// Insecure Random Number Generation (CWE-338)
// This example illustrates the usage of Math.random() for generating random numbers, which is not suitable for cryptographic or security-sensitive purposes. SAST tools can detect this and recommend using a cryptographically secure random number generator for secure random number generation.