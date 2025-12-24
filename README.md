
# 📘 Python & Selenium Automation Learning Repository

## 👤 Author

**Seraj**

---

## 📌 Project Overview

This repository contains **Python fundamentals, practice programs, and Selenium automation examples** created as part of my learning journey in **Python for Test Automation (SDET)**.

The goal of this repository is to:

* Build a **strong Python foundation**
* Practice **automation-ready Python concepts**
* Implement **Selenium + PyTest + Allure**
* Maintain a **clean, structured, and review-friendly codebase**

---

## 🧠 What You Will Learn

### 🔹 Python Basics

* Variables & Data Types
* Literals
* Operators
* Conditions & Loops
* Functions
* Strings, Lists, Tuples, Sets, Dictionaries
* Decorators
* Input/Output handling

### 🔹 Problem Solving

* Fibonacci Series
* Factorial Program
* Grade Calculator
* Leap Year Checker
* Triangle Classification
* Mathematical Programs

### 🔹 Automation Foundations

* Selenium WebDriver
* PyTest Framework
* Assertions
* Test Execution
* Allure Reporting

---

## 📂 Project Structure

```
📦 python-selenium-learning
│
├── 📁 src
│   ├── 📁 ex_01_Python_Basics
│   │   ├── variables.py
│   │   ├── data_types.py
│   │   ├── operators.py
│   │   ├── conditions.py
│   │   ├── loops.py
│   │   └── functions.py
│   │
│   ├── 📁 ex_02_String_List
│   │   ├── string_operations.py
│   │   ├── slicing.py
│   │   └── list_operations.py
│   │
│   ├── 📁 ex_03_Problem_Solving
│   │   ├── factorial.py
│   │   ├── fibonacci.py
│   │   ├── grade_calculator.py
│   │   └── leap_year.py
│   │
│   ├── 📁 ex_04_Selenium_Basics
│   │   ├── test_selenium_01.py
│   │   └── test_selenium_02.py
│
├── 📁 reports
│   └── allure-results
│
├── 📁 resources
│   └── test_data
│
├── 📄 requirements.txt
├── 📄 pytest.ini
├── 📄 README.md
└── 📄 .gitignore
```

---

## ⚙️ Prerequisites

Make sure you have the following installed:

* Python **3.10+**
* pip (latest version)
* Git
* Browser (Chrome / Edge)
* WebDriver (ChromeDriver / EdgeDriver)

---

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/python-selenium-learning.git
cd python-selenium-learning
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

### 3️⃣ Activate Virtual Environment

**Windows**

```bash
.venv\Scripts\activate
```

**Mac/Linux**

```bash
source .venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running Python Programs

```bash
python src/ex_01_Python_Basics/variables.py
```

---

## 🧪 Running Selenium Tests with PyTest

```bash
pytest src/ex_04_Selenium_Basics/test_selenium_01.py
```

---

## 📊 Generating Allure Report

### 1️⃣ Run Tests with Allure Results

```bash
pytest src/ex_04_Selenium_Basics --alluredir=reports/allure-results
```

### 2️⃣ Open Allure Report

```bash
allure serve reports/allure-results
```

---

## 🧾 Sample Test Code

```python
@allure.title("Print the title of the page")
def test_selenium():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    print(driver.title)
    driver.quit()
```

---

## 📝 Coding Standards Followed

* Snake_case naming
* Modular structure
* Meaningful comments
* One concept per file
* Clean and readable code

---

## 🚀 Future Enhancements

* Page Object Model (POM)
* Data-driven testing
* CI/CD Integration
* Docker support
* API Automation (Requests)

---

## 📬 Feedback & Review

This repository is created for **learning and review purposes**.
Suggestions and improvements are always welcome.

---

