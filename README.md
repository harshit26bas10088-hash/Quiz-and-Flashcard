Python Study Tool
A simple, offline command-line interface (CLI) application built with Python to help you study using flashcards and multiple-choice quizzes.
Features
Dual Modes: Choose between reviewing definitions with Flaspcards or testing knowledge with Quizzees.
Customizable Content: Easily modify the Python script to add your own subjects, terms, and questions.
Interactive CLI: A user-friendly menu system that runs directly in your terminal.
Offline Functionality: Requires no internet connection to run.
Prerequisites
Python: You must should  have in Python installed on your machine. You can download it from python.org.
Getting Started
Download the Script: Save the quiz_flashcard.py file to a folder on your computer.
Open Terminal: Navigate to the folder where you saved the script.
Run the Program: Execute the script using the following command in your terminal:
code
Bash
python quiz_flashcard.py
How to Use
Upon running the script, you will see the Main Menu. Follow the on-screen prompts to navigate the application.
Main Menu
Select a subject from the list provided by entering its corresponding number.
Enter 0 to exit the program.
Flashcard Mode
If the selected subject is a flashcard set:
The program will display a term.
Press Enter to reveal the definition.
The program will automatically move to the next term until the set is complete.
Quiz Mode
If the selected subject is a quiz:
A multiple-choice question will appear with options (a, b, c...).
Type the letter corresponding to your answer and press Enter.
The program will indicate if you are correct and proceed to the next question.
After the quiz, your final score will be displayed.
Customizing the Data
You can easily add your own study material by editing the Python script.
Open quiz_flashcard.py in a text editor or VS Code.
Locate the STUDY_DATA dictionary near the top of the file.
Follow the existing structure to add new subjects and content.
Example Data Structuring:
code
Python
STUDY_DATA = {
    "New Subject Name": {
        "type": "flashcards", // or "quiz"
        "data": {
            "Term": "Definition",
            "Another Term": "Another Definition"
        }
    },
    "Another Subject": {
        "type": "quiz",
        "data": [
            ("Question Text", ["Option A", "Option B", "Option C"], "Correct Option"),
            // Add more questions as tuples
        ]
    }
}
License
This project is open-source and available for personal use and modification.