# Password Strength Checker

#### Video Demo: https://youtu.be/YOUR_VIDEO_LINK_HERE

#### Description:

Password Strength Checker is a command-line Python application developed as the final project for CS50P.
The purpose of this project is to help users evaluate how secure their passwords are based on commonly
accepted security rules.

The program checks a password against multiple criteria such as minimum length, presence of uppercase
letters, lowercase letters, digits, and special characters. It also detects commonly used weak passwords
that are vulnerable to attacks.

The project consists of the following files:

project.py:
This file contains the main application logic. The main() function takes user input and displays the
password strength. Additional helper functions are used to validate specific password rules such as
checking for digits, uppercase letters, lowercase letters, special characters, and common passwords.

test_project.py:
This file contains unit tests written using pytest. Each test function validates the correctness of
the corresponding function in project.py. Testing ensures reliability and correctness of password
validation logic.

requirements.txt:
This file lists external dependencies required to run the project. Pytest is included for running
unit tests.

Design decisions:
The program uses simple and readable logic rather than advanced libraries to clearly demonstrate
understanding of Python fundamentals. Regular expressions are used for special character detection
to ensure accuracy.

This project demonstrates the use of functions, conditionals, loops, regular expressions, unit
testing, and modular design, fulfilling all CS50P final project requirements.
