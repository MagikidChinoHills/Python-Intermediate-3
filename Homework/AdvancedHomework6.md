### **Homework 6: Enhancing the Trivia Game**

This homework will challenge you to **improve the Trivia Game** by adding new features and making it more interactive.

---

## **Problem 1: Add a New Trivia Category**
- Create a **new trivia category** (e.g., **GeographyTrivia, SportsTrivia, or MathTrivia**).
- Each category should contain **at least 3 questions**.
- The new category should **inherit from `GameRound`** like the existing categories (HistoryTrivia, ScienceTrivia).

🔹 **Hint:**  
- Look at how `HistoryTrivia` and `ScienceTrivia` are implemented.  
- Use `super().__init__(questions)` to call the `GameRound` constructor.

---

## **Problem 2: Track and Display High Scores**
- Modify the game to **keep track of the highest score** achieved by the player.
- Display a **high-score message** when the game ends.

🔹 **Hint:**  
- Store the highest score in a **global variable** or a **text file**.
- Check if the player's current score is higher than the previous high score.

---

## **Problem 3: Add a Countdown Timer**
- Implement a **countdown timer** for each question.
- If the player does not select an answer within **10 seconds**, move to the next question.
- Display a **warning message** when time runs out.

🔹 **Hint:**  
- Use `self.master.after(1000, function_name)` to update the timer every second.
- Display the timer in the GUI.

---

## **Problem 4: Improve the GUI Design**
- Add **colors and styling** to the trivia game.
- Make the buttons **larger and easier to read**.
- Change the background color **based on the trivia category** (e.g., blue for Science, red for History).

🔹 **Hint:**  
- Use `self.master.configure(bg="color_name")` to change background color.
- Modify the font size of the **labels and buttons** for better readability.

---

## **Bonus Challenge: Add Sound Effects 🎵**
- Play a **"correct" sound** when the player selects the right answer.
- Play an **"incorrect" sound** when the player selects the wrong answer.

🔹 **Hint:**  
- Use the `pygame` library to play sound effects.
- Example: `pygame.mixer.Sound("correct_sound.wav").play()`

---

### **Submission Instructions:**
- Complete **at least 3 out of 4 problems**.
- Submit your **modified trivia game code**.
- Add comments to explain **any new code you write**.

---

💡 **Extra Tip:**  
Try playing your game **several times** to make sure all new features work correctly! 🚀
