// The following code is vulnerable to Zip Slip as it is constructing
// a path using an archive entry name. This path is then used to copy
// a file without being validated first. Therefore, it can be leveraged 
// by an attacker to overwrite arbitrary files.


// OWASP Top 10 2021 Category A1 - Broken Access Control
// OWASP Top 10 2021 Category A3 - Injection
// OWASP Top 10 2017 Category A1 - Injection
// OWASP Top 10 2017 Category A5 - Broken Access Control
// MITRE, CWE-20 - Improper Input Validation
// MITRE, CWE-22 - Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')

// https://github.com/advisories/GHSA-xwg4-93c6-3h42

const AdmZip = require("adm-zip");
const upload = require('multer');

app.get('/example', upload.single('file'), (req, res) => {
    const zip = new AdmZip(req.file.buffer);
    const zipEntries = zip.getEntries();

    zipEntries.forEach(function (zipEntry) {
        var writer = fs.createWriteStream(zipEntry.entryName); // Noncompliant
        writer.write(zipEntry.getData().toString("utf8"));
    });
});
