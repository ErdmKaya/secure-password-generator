# Advanced Secure Password Generator

A robust command-line tool written in Python that generates cryptographically strong passwords. Unlike basic random generators, this tool utilizes Python's `secrets` module to ensure passwords are secure enough for real-world application.

## Features

* **Cryptographically Secure:** Uses the `secrets` library (instead of `random`) to generate unpredictable passwords.
* **Customizable:** User defines the password length.
* **Complexity Options:** Optional inclusion of **digits** (0-9) and **special symbols** (!@#$...).
* **Validation:**
    * Ensures the minimum length is met (4+ characters).
    * Guarantees that selected options (e.g., symbols) actually appear in the final password.
* **User-Friendly:** Interactive command-line interface with input error handling.

## Why `secrets`?

Unlike the `random` module, Python’s `secrets` module is designed for
security-sensitive applications such as passwords and tokens.

## Requirements

* Python 3.6 or higher.
* No external libraries required (uses standard `secrets`, `string`, and `time` modules).

## How to Run

1. **Clone the repository** (or download the script):
    ```bash
    git clone https://github.com/ErdmKaya/secure-password-generator.git
    cd secure-password-generator
    ```

2.  **Run the script:**
    ```bash
    python randomPassword.py
    ```

3.  **Follow the on-screen prompts:**
    * Enter the desired length.
    * Type `y` or `n` for numbers and symbols.

## Usage Example

```text
=======================================
ADVANCED SECURE PASSWORD GENERATOR
=======================================
Tip: Including numbers and symbols is recommended for strong security. 

Password Length (min 4): 16
Include numbers? (y/n): y
Include symbols? (y/n): y

Generating secure password...
------------------------------
YOUR PASSWORD: xK9#mP2$vL5@nQ8!
------------------------------
Do not share your password with anyone!