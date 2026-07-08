# DevSecOps Demo Application

A deliberately insecure Flask application built to demonstrate how security checks and CI/CD safeguards can help identify and mitigate common vulnerabilities in a real project.

> ⚠️ This repository is intentionally vulnerable for educational purposes. It should only be used in a local development or training environment.

## Overview

This project simulates a small web application that exposes a few insecure patterns commonly found in legacy applications:

- SQL injection through an unsanitized query parameter
- A hardcoded secret-like value in source code
- Debug mode enabled in the application runtime
- A simple containerized setup for CI/CD security demonstrations

The goal is to showcase how DevSecOps practices such as static analysis, dependency scanning, container scanning, and secret detection can be used to catch and remediate these issues.

## What This App Does

The application exposes a basic endpoint:

- GET /user_data?id=<id>

It reads the user ID from the query string and uses it directly in a SQL query, which makes the endpoint vulnerable to injection.

## Tech Stack

- Python 3.9
- Flask
- SQLite
- Docker

## Project Structure

- main.py - Flask application with intentionally insecure code
- requirements.txt - Python dependencies
- Dockerfile - Container definition for the app
- README.md - Project overview and usage instructions

## Getting Started

### 1. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app locally

```bash
python main.py
```

The app will start on port 5000.

### 4. Test the endpoint

```bash
curl "http://127.0.0.1:5000/user_data?id=1"
```

## Security Issues Demonstrated

This app intentionally includes examples of common weaknesses such as:

- SQL injection
- Hardcoded credentials/secrets
- Unsafe runtime configuration
- Lack of secure-by-default development practices

## DevSecOps Demo Ideas

This repository is ideal for demonstrating:

- Static Application Security Testing (SAST)
- Dependency vulnerability checks
- Secret scanning
- Container image scanning
- CI/CD policy enforcement and build gating

Typical checks you can add in a pipeline include:

- Bandit for Python security analysis
- pip-audit or Safety for dependency scanning
- Gitleaks for secret detection
- Trivy for container scanning

## Suggested Next Steps

To turn this demo into a stronger DevSecOps example, you can:

1. Add automated security checks to a CI pipeline
2. Fail builds when vulnerabilities are detected
3. Fix the insecure patterns in a secure branch
4. Compare the vulnerable version with the remediated version

## License

This project is intended for educational and demonstration purposes only.
