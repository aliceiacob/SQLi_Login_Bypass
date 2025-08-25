# SQL Injection Login Bypass Demo

This project demonstrates how a web application vulnerable to **SQL Injection (SQLi)** can be exploited to bypass login authentication.  
It uses a **Python script** with the `requests` and `BeautifulSoup` libraries to automate the attack and highlights the importance of secure coding practices.

---

## 🔍 What This Project Does
- Extracts a **CSRF token** from the login page.
- Submits a login form with a malicious SQL payload as the **username**.
- Detects whether login was successful (e.g., if a "Logout" keyword appears in the response).
- Demonstrates how weak validation allows attackers to bypass authentication.

---

## 🛠 Requirements
- Python 3.x  
- Libraries:
  ```bash
  pip install requests beautifulsoup4
