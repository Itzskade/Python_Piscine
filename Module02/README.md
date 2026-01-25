# 🌿 Garden Guard  
## Data Engineering for Smart Agriculture

**Garden Guard** is a Python project focused on **building resilient data pipelines** for smart agriculture systems.  
Through a series of exercises, you will learn how to **handle errors, manage failures gracefully, and design fault-tolerant systems** that can survive unreliable sensor data, corrupted inputs, and unexpected runtime issues.

This project is part of the progression from Python fundamentals to **robust data engineering practices** applied to agricultural monitoring systems.

---

## 🎯 Project Goals

- Understand Python exception handling in depth  
- Build resilient data pipelines for real-world scenarios  
- Handle faulty sensor data and invalid user input  
- Use built-in Python exceptions appropriately  
- Create custom exception types  
- Apply `try / except / finally` patterns correctly  
- Design systems that continue running despite errors  
- Write clean, readable, and maintainable Python code  

---

## 📁 Exercises Overview

| Exercise | Description                                      | Directory | File to Submit                 |
|---------:|--------------------------------------------------|-----------|--------------------------------|
| 00       | Agricultural data validation pipeline            | ex0/      | ft_first_exception.py          |
| 01       | Handling different types of errors               | ex1/      | ft_different_errors.py         |
| 02       | Creating custom exception types                  | ex2/      | ft_custom_errors.py            |
| 03       | Using `finally` blocks for cleanup               | ex3/      | ft_finally_block.py            |
| 04       | Raising your own errors                          | ex4/      | ft_raise_errors.py             |
| 05       | Complete garden management system                | ex5/      | ft_garden_management.py        |

---

## 🧠 Project Context

Modern smart agriculture relies heavily on **continuous data streams**:
- Sensor readings (temperature, humidity, soil conditions)
- IoT devices
- External APIs (weather forecasts)

Failures are inevitable. Sensors break, networks fail, and corrupted data appears.  
This project teaches you that **robust systems are not built to avoid errors, but to handle them correctly**.

Python’s exception-handling system is your main tool to:
- Detect anomalies
- Prevent corrupted data from spreading
- Recover gracefully from failures
- Keep systems running under real conditions

---

## 📐 General Rules

- Python **3.10 or higher**
- One exercise per file
- Follow **flake8** standards
- Include simple and clear docstrings
- Focus on demonstrating error-handling concepts
- Show both normal execution and error scenarios
- Programs must **never crash unexpectedly**
- Keep solutions simple and educational

---

## 🛠 Concepts Covered

- `try / except`
- Multiple exception handling
- Built-in exceptions (`ValueError`, `ZeroDivisionError`, etc.)
- Custom exception classes
- Exception inheritance
- `raise`
- `finally` blocks
- Fault-tolerant system design

---

## 📦 Final Exercise: Garden Management System

The final exercise combines **all concepts** from the project:
- Custom exceptions
- Error recovery
- Resource cleanup
- Graceful degradation
- Meaningful error messages

You will build a simple but complete **garden management system** that continues working even when some operations fail.

---

## 📤 Submission & Evaluation

- Submit your work through your Git repository
- Only files specified in the subject will be evaluated
- You must be able to **explain every line of your code**
- During evaluation, you may be asked to:
  - Trace execution flow
  - Modify your code
  - Justify design decisions

Focus on clarity, correctness, and understanding—not complexity.

---

## 📜 License

This project is part of an educational program.  
All code is intended for learning purposes and personal reference.

---

## 🙋 Author

Developed as part of a Python learning path focused on **Data Engineering and System Reliability**.

---

## 📧 Contact

[rmarin-n@student.42barcelona.com](mailto:rmarin-n@student.42barcelona.com)
