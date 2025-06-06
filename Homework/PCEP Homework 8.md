## practice quizziz link: https://quizizz.com/embed/quiz/681ebc1a55dd9be136cbad90


### **Part 1: Conceptual Questions**

### 1. **Short Answer Questions:**
  - What is the purpose of the `try` and `except` blocks in Python?
  - Describe the difference between `else` and `finally` in exception handling.
  - List three common exceptions in Python and give an example of when each might occur.

---

### 2. **Traceback Analysis:**
  Examine the following code:
  ```
  Traceback (most recent call last):
    File "main.py", line 5, in <module>
      result = 10 / 0
  ZeroDivisionError: division by zero
  ```
  - What type of exception occurred?
  - Which line of code caused the exception?
  - How would you fix this error?

---

### 3. File Handling
Write a program that:
1. Prompts the user for a filename.
2. Attempts to open the file for reading.
3. If the file does not exist, catch the `FileNotFoundError` and display an error message.
4. Ensure the program prints "Operation complete" at the end using a `finally` block.
