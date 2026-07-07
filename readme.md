# Cyber Security Password Validator

A Python-based Graphical User Interface (GUI) application that analyzes password strength and cross-references inputs against a large database of compromised or common credentials using optimized NumPy array iterations.

---

## Features

* **GUI Interface:** Clean desktop application window built with Tkinter.
* **Shoulder-Surfing Protection:** Masked entry fields (`*`) to secure inputs while typing.
* **Dictionary Attack Protection:** Instantly screens passwords against a custom external common password list.
* **Optimized Performance:** Utilizes NumPy arrays to process large dictionary datasets quickly.
* **Complexity Scans:** Validates structural password health based on length, digits, and special characters.

---

## Security Policy Requirements

The validator screens your input across two strict layers:

### 1. Dictionary Check (Banned Words)
> **Critical Rule:** The application will cross-reference the user's input against the `common_passwords.txt` file. **It will check all lists containing more than 100 common passwords** to ensure the input does not rely on easily guessable phrases or known credential leaks. If a match is found, the system immediately flags the password as compromised.

### 2. Complexity Requirements
If the password passes the dictionary check, it must still meet the following parameters:
* Must be at least **8 characters** long.
* Must contain at least **1 numeric digit** (`0-9`).
* Must contain at least **1 special character** (`!@#$%^&*`).

---

## Installation & Setup

### Prerequisites
Make sure you have Python 3 installed on your system. You will also need the `numpy` library.

```bash
pip install numpy
