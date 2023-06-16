# vulnerable-code-examples
## Description
This repo contains a variety of code samples of vulnerability, dependency and risk.

## IaC (Infrastructure as Code)

Repo: https://github.com/dehvCurtis/vulnerable-code-examples/tree/main/IaC

### Vulnerabilities / Exposure
#### Kubernetes
| Location        | File     | CWE / Exposure    | # of Exposures |
| ----------       | -----------                  | ------- | - |
| `IaC/kubernetes` | `docker-socket.yaml`         | CWE-284 | 1 |
| `IaC/kubernetes` | `pod-path-mount.yaml`        | CWE-668 | 1 |
| `IaC/kubernetes` | `privilege-escalation.yaml`  | CWE-284 | 1 |
| `IaC/kubernetes` | `using-host-namespaces.yaml` | CWE-653 | 1 |
| | | **Total** | 4 |

#### Terraform
| Location        | File     | CWE / Exposure    | # of Exposures |
| ----------       | -----------                  | ------- | - |
| `IaC/terraform`  | `god-mode.tf` | CWE-732, CWE-284 | 2 |
| `IaC/terraform`  | `public-access-over-network.tf` | CWE-284, CWE-668 | 2 |
| `IaC/terraform`  | `public-api.tf` | CWE-284 | 1 |
| | | **Total** | 5 |

## SAST

Repo: https://github.com/dehvCurtis/vulnerable-code-examples/tree/main/SAST

### Vulnerabilities / Exposure
#### C / C++
| Location        | File     | CWE / Exposure    | # of Exposures |
| ----------       | -----------                  | ------- | - |
| `SAST/cpp` | `memset-delete.cpp`         | CWE-14 | 1 |
| `SAST/cpp` | `posix-buffer-overflow.cpp` | CWE-119, CWE-131, CWE-788 | 3 |
| `SAST/cpp` | `toctou.cpp`                | CWE-367 | 1 |
| | | **Total** | 5 |

#### C#
| Location        | File     | CWE / Exposure    | # of Exposures |
| ----------       | -----------                  | ------- | - |
| `SAST/csharp` | `dynamic-code-injection.cs` | CWE-20, CWE-95| 2 |
| `SAST/csharp` | `http-req-forging-redir.cs` | CWE-20, CWE-601 | 1 |
| `SAST/csharp` | `unsecure-db-connect.cs` | CWE-521 | 1 |
| | | **Total** | 4 |

#### Java
| Location        | File     | CWE / Exposure    | # of Exposures |
| ----------       | -----------                  | ------- | - |
| `SAST/java` | `sample.java` | CWE-259 | 1 |
| | | **Total** | 1 |

#### JavaScript
| Location        | File     | CWE / Exposure    | # of Exposures |
| ----------       | -----------                  | ------- | - |
| `SAST/javascript` | `sample.js` | CWE-359 | 1 |
| | | **Total** | 1 |

#### PHP
| Location        | File     | CWE / Exposure    | # of Exposures |
| ----------       | -----------                  | ------- | - |
| `SAST/php` | `basic-collection.php` | ? | 3 |
| `SAST/php` | `password-exposure.php` | CWE-259 | 1 |
| `SAST/php` | `reflection-injection.php` | CWE-470 | 1 |
| `SAST/php` | `sql-injection.php` | ? | 1 |
| `SAST/php` | `untrusted-session-cookie.php` | CWE-20, CWE-384 | 1 |
| | | **Total** | 7 |

#### Python
| Location        | File     | CWE / Exposure    | # of Exposures |
| ----------       | -----------                  | ------- | - |
| `SAST/python/ciphers` | `pyca.py` | CWE-327 | 1 |
| `SAST/python/ciphers` | `pycrypto.py` | CWE-327 | 1 |
| `SAST/python/ciphers` | `pycryptodomex.py` | CWE-327 | 1 |
| `SAST/python/injection` | `dynamic-code-injection.py` | arbitrary code execution | 1 |
| `SAST/python/injection` | `http-redir-forging.py` | open redirect | 1 |
| `SAST/python/injection` | `ldap-injection.py` | LDAP injection | 1 |
| `SAST/python/injection` | `logging-injection.py` | log injection | 1 |
| `SAST/python/injection` | `os-command-injection.py` | command injections | 1 |
| `SAST/python/injection` | `serverside-template-injection.py` | ?  | 1 |
| `SAST/python/verification` | `pyjwt.py` | un-signed token | 1 |
| `SAST/python/verification` | `python-jwt.py` | un-signed token | 1 |
| `SAST/python/verification` | `ssl-standard.py` | ? | 1 |
| `SAST/python` | `print-password.py` | CWE-359 | 1 |
| | | **Total** | 13 |

#### Typescript
| Location        | File     | CWE / Exposure    | # of Exposures |
| ----------       | -----------                  | ------- | - |
| `SAST/typescript` | `Insecure-Random-Number-Generation.ts` | CWE-338 | 1 |
| `SAST/typescript` | `code-injection.ts` | CWE-94 | 1 |
| `SAST/typescript` | `dom-redir.ts` | CWE-20, CWE-601 | 2 |
| `SAST/typescript` | `dom-xss.js` | CWE-79 | 1 |
| `SAST/typescript` | `sql-injection.ts` | CWE-89 | 1 |
| `SAST/typescript` | `xss.ts` | CWE-79 | 1 |
| `SAST/typescript` | `zip-slip.js` | CWE-20, CWE-22 | 2 |
| | | **Total** | 9 |

## SCA

Repo: https://github.com/dehvCurtis/vulnerable-code-examples/tree/main/SCA

### Vulnerabilities / Exposure
#### Java
| Location        | File     | CWE / Exposure    | # of Exposures |
| ----------       | -----------                  | ------- | - |
| `SCA/java/maven` | `pom.xml` | spring-boot-starter | 1 |

#### JavaScript
| Location        | File     | CWE / Exposure    | # of Exposures |
| ----------       | -----------                  | ------- | - |
| `SCA/javascript/node` | `pom.xml` | spring-boot-starter | 1 |

#### Python
| Location        | File     | CWE / Exposure    | # of Exposures |
| ----------       | -----------                  | ------- | - |
| `SCA/python` | `requirements.txt` | dependencies | 2 |

#### Ruby
| Location        | File     | CWE / Exposure    | # of Exposures |
| ----------       | -----------                  | ------- | - |
| `SCA/ruby` | `Gemfile` | dependencies | 2 |
