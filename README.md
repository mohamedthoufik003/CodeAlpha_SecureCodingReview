# 🔒 CodeAlpha Task 3: Secure Coding Review

This is my submission for **Task 3: Secure Coding Review** as part of the CodeAlpha Cybersecurity Internship.

---

## 🛠️ Project Overview

A simple login system built with **Python Flask**. The goal of this task was to analyze a sample application for **security vulnerabilities**, suggest improvements, and follow **secure coding best practices**.

---

## 🚨 Vulnerabilities Identified

1. **Hardcoded Credentials**
   - Credentials were stored in plain Python code (`app.py`)
   - ⚠️ Risk: Easy to extract passwords if leaked

2. **No Input Validation**
   - Username and password inputs were not sanitized
   - ⚠️ Risk: Susceptible to injection attacks

3. **No HTTPS/TLS**
   - Application runs on HTTP by default
   - ⚠️ Risk: Credentials could be sniffed over unsecured networks

---

## 🛡️ Recommended Fixes

- 🔐 Use secure user storage (e.g., hashed passwords + database)
- ✋ Add input validation and escape mechanisms
- ✅ Deploy using `HTTPS` with SSL certificates
- 🔁 Implement proper session and error handling
- ⚙️ Use Flask extensions like `Flask-Login` and `Flask-WTF` for secure user auth

---

## 📷 Screenshots & Demo

> https://drive.google.com/file/d/1iTEfI2Ixh44_PZLZt24eyJZMu2Vo1P2q/view?usp=drive_link

> https://drive.google.com/file/d/1JznjZvrHwgZG1tjv9Pc9rW6GPVXILwPm/view?usp=drive_link

---

## 🧪 Tools Used

- 🐍 Python 3.x
- 🌐 Flask (micro web framework)
- 🔎 Manual Code Review
- 📋 Static code analyzers (optional)

---

## 💼 Submitted To

**CodeAlpha**  
Cybersecurity Internship (Task 3)  
✅ [LinkedIn Profile](https://www.linkedin.com/in/mohamed-thoufik)  
📁 GitHub: [CodeAlpha_SecureCodingReview](https://github.com/mohamedthoufik003/CodeAlpha_SecureCodingReview)

---

## 🚀 Author

**👨‍💻 Mohamed Thoufik**  
- GitHub: [mohamedthoufik003](https://github.com/mohamedthoufik003)  
- Email: mohamedthoufik25668@gmail.com

