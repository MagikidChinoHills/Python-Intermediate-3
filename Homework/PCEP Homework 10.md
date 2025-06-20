# **Lesson 10: Advanced Error Handling - Homework**

## **Instructions:**

Complete the following exercises on exception handling. Ensure that you apply the concepts of `try-except`, multiple exception handling, `else`, `finally`, and custom exceptions where applicable.

---

### **1. Identifying Exceptions**

For each of the following scenarios, identify which Python exception would likely occur and explain why:

* Trying to divide a number by zero.
* Attempting to convert the string `'abc'` into an integer.
* Accessing the 10th index of a list with only 5 elements.
* Attempting to retrieve a non-existent key from a dictionary.
* Using an undefined variable in an arithmetic operation.

---

### **2. Exception Handling in User Input**

Write explanations for how you would handle the following user input errors:

* A user enters a string instead of a number when asked to input an age.
* A user inputs `0` as a denominator when asked to perform division.
* A user tries to access a file that does not exist.

Explain how a `try-except` block would be structured to handle these cases.

---

### **3. Handling Multiple Exceptions**

Consider a situation where a program needs to:

* Read an integer from the user.
* Perform a division operation with another user-provided number.
* Access a specific index from a predefined list.

Explain how you would structure multiple `except` blocks to handle potential errors, including `ValueError`, `ZeroDivisionError`, and `IndexError`.

---

### **4. Using `else` and `finally`**

Explain the difference between the `else` and `finally` clauses in a `try-except` block. Provide a practical example where you would use each one.

---

### **5. Creating Custom Exceptions**

Define a scenario where a custom exception would be useful. Explain:

* Why a standard Python exception would not be sufficient.
* How a custom exception improves error handling.
* What message the custom exception should display when triggered.

---

### **6. Debugging Error Messages**

Below are some common error messages seen in Python. Explain what each error means and how it can be fixed:

* `ZeroDivisionError: division by zero`
* `ValueError: invalid literal for int() with base 10: 'abc'`
* `IndexError: list index out of range`
* `KeyError: 'missing_key'`
* `TypeError: unsupported operand type(s) for +: 'int' and 'str'`
