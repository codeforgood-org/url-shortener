# Security Policy

## Supported Versions

We release patches for security vulnerabilities in the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

We take the security of the Todo List Manager seriously. If you believe you have found a security vulnerability, please report it to us as described below.

### How to Report

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them via email to the repository maintainers. You can find the contact information in the repository's main page.

Include the following information in your report:

- Type of vulnerability
- Full paths of source file(s) related to the vulnerability
- Location of the affected source code (tag/branch/commit or direct URL)
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the vulnerability, including how an attacker might exploit it

### What to Expect

- We will acknowledge receipt of your vulnerability report within 48 hours
- We will send a more detailed response within 5 business days indicating the next steps
- We will keep you informed of the progress towards a fix and announcement
- We will credit you in the security advisory (unless you prefer to remain anonymous)

## Security Best Practices

When using Todo List Manager:

1. **File Permissions**: Ensure your `tasks.json` file has appropriate permissions if it contains sensitive information
2. **Input Validation**: The application validates all user inputs, but be cautious with task descriptions
3. **Data Storage**: Tasks are stored locally in JSON format - ensure your filesystem is secure
4. **Dependencies**: Keep Python and any optional dependencies up to date
5. **Code Review**: Review the source code if you have security concerns - it's open source!

## Known Security Considerations

### Data Storage

- Tasks are stored in plain text JSON files
- No encryption is applied to stored data
- Files are created with default system permissions

**Recommendation**: Do not store highly sensitive information in task descriptions. If you need to reference sensitive data, use identifiers or references instead.

### Command Injection

- The application uses standard Python file I/O operations
- No shell commands are executed with user input
- All user inputs are properly sanitized

### Dependencies

- The core application has zero external dependencies
- Optional development dependencies are specified in `requirements.txt`
- We regularly update dependencies to address security vulnerabilities

## Security Scanning

This project uses:

- **Bandit**: Static security analysis for Python code
- **Safety**: Checks for known security vulnerabilities in dependencies
- **GitHub Actions**: Automated security checks on every commit

## Disclosure Policy

When we receive a security report, we will:

1. Confirm the problem and determine affected versions
2. Audit code to find any similar problems
3. Prepare fixes for all supported versions
4. Release new versions as soon as possible
5. Publish a security advisory

## Comments on this Policy

If you have suggestions on how this process could be improved, please submit a pull request or open an issue to discuss.

## Attribution

This security policy is based on best practices from the open-source community and adapted for this project.
