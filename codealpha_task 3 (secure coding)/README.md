# Secure Coding Review

### Project Overview;

The Secure Coding Review project focuses on analyzing application code to identify potential security vulnerabilities and improve overall software security. The objective is to review the code, detect security weaknesses, and suggest proper remediation techniques and secure coding practices.

## Objectives;

Identify security vulnerabilities in application code

Apply secure coding best practices

Document findings from the code review process

Provide remediation steps to fix identified issues


### Tools and Technologies;

Programming Language: Python

Code Analysis Tools: Bandit / Pylint (optional)

Concepts Used: Secure Coding Practices, Code Review, Vulnerability Analysis


### Security Issues Identified;

During the code review, the following issues were observed:

Hardcoded Credentials
Sensitive information like usernames and passwords stored directly in the code.

Plain Text Password Handling
Passwords compared or stored without encryption.

Lack of Input Validation
User inputs were not properly validated before processing.

Unlimited Login Attempts
The system allowed unlimited login attempts, increasing the risk of brute force attacks.

### Recommendations and Best Practices;

Avoid storing sensitive data directly in the source code.

Use password hashing techniques to protect credentials.

Validate and sanitize all user inputs.

Implement maximum login attempt limits.

Follow secure authentication and authorization practices.

### Remediation Steps;

To address the identified vulnerabilities, the following steps were implemented:

Replaced hardcoded credentials with secure storage methods.

Implemented password hashing for secure authentication.

Added input validation checks to prevent malicious input.

Introduced a maximum login attempt policy to prevent brute force attacks.

### Learning Outcomes;

Understanding common software security vulnerabilities

Learning secure coding practices

Gaining experience in code review and vulnerability identification

Improving application security through remediation techniques

## Conclusion

The Secure Coding Review project highlights the importance of writing secure code and regularly reviewing applications for vulnerabilities. By implementing secure coding practices and remediation strategies, software systems can be made more reliable and resistant to security threats.
