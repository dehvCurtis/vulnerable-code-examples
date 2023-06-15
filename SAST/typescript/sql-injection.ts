// File: sample.ts

import { executeQuery } from 'database';

const userId = '1; DROP TABLE users;';
const query = `SELECT * FROM users WHERE id = ${userId}`;
executeQuery(query);

// SQL Injection (CWE-89)
// This example showcases a SQL injection vulnerability where an attacker manipulates the userId parameter to execute arbitrary SQL statements. SAST tools can detect this vulnerability and recommend using parameterized queries or prepared statements to prevent SQL injection attacks.