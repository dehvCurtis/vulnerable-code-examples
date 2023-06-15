// File: sample.ts

const code = `console.log("Executing arbitrary code!");`;
eval(code);

// Code Injection (CWE-94)
// This example demonstrates code injection vulnerability by using eval() to execute arbitrary code. SAST tools can detect this vulnerability and warn against using eval() or dynamically executing user-supplied code.