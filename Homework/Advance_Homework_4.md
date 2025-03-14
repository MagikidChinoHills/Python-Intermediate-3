## **Homework 4: Enhancing the Password Generator**  

### **Problem 1: Add an Option to Include or Exclude Special Characters**  
- Modify the password generator to **give users the choice** to include or exclude special characters.  
- Add a **checkbox** that toggles special characters **on or off**.  
- If unchecked, the password should only contain letters and numbers.  

💡 **Hint:** Use a `BooleanVar()` to track the state of the checkbox.  

---

### **Problem 2: Implement a Strength Indicator**  
- Add a **strength indicator** that categorizes passwords as **Weak, Medium, or Strong**.  
- Display a label below the password that updates based on **length and character complexity**.  

💡 **Hint:** A strong password should:  
✅ Have **at least 10 characters**  
✅ Include **uppercase & lowercase letters**  
✅ Contain **numbers and symbols**  

---

### **Problem 3: Add a "Clear" Button**  
- Add a **Clear** button that **removes** the generated password from the display.  
- Ensure it also clears the password length entry field.  

💡 **Hint:** Use `.set("")` on `StringVar()` to reset values.  

---

### **Problem 4: Implement a History Feature**  
- Store the last **5 generated passwords** in a list.  
- Display these passwords in a small box (such as a `Text` or `Listbox` widget).  
- Ensure older passwords are removed once the list reaches **5 entries**.  

💡 **Hint:** Use a list to **store and update** password history dynamically.  

---

### **Problem 5: Customize the Interface**  
- Change the **background color** and **font style** of the application.  
- Modify button colors for better **visual appeal**.  

💡 **Hint:** Use `.config(bg="color")` and `.config(font=("FontName", size))` to style widgets.  

---

### **Bonus Challenge**  
🔹 Save passwords to a text file when generated.  
🔹 Create a button labeled **"Save Password"** that writes the password **to a file** for future reference.  

---

### **Submission Instructions**  
📌 Submit your updated Python script with comments explaining the changes you made.  
📌 Answer the following **reflection question** in a separate file:  
   - **How does password length affect its security?**  

---

**💡 Reminder:** Always use strong passwords to protect sensitive accounts! 🔒✨
