import random
import sys

# --- 1. Data Configuration ---
# You can modify this dictionary to add your own subjects and questions.
# Format: "Subject Name": { "Flashcards": {term: definition}, "Quiz": [(question, options, correct_answer)] }
DATA = {
    "Python Basics": {
        "Flashcards": {
            "Variable": "A named storage location for data.",
            "String": "A sequence of characters enclosed in quotes (e.g., 'hello').",
            "Integer": "A whole number, positive or negative, without decimals.",
            "Boolean": "A data type with two values: True or False.",
            "List": "An ordered, mutable collection of items.",
            "Dictionary": "An unordered collection of key-value pairs."
        },
        "Quiz": [
            ("What data type is the result of 10 / 2?", ["int", "float", "str", "bool"], "float"),
            ("Which keyword is used to define a function in Python?", ["func", "def", "define", "lambda"], "def"),
            ("How do you start a comment in Python?", ["//", "/*", "#", "--"], "#"),
            ("Which method adds an element to the end of a list?", ["append()", "add()", "insert()", "push()"], "append()")
        ]
    },
    "tuples": {
        "Flashcards": {
            "What is a tuple in Python?": "An ordered, immutable collection of items.",
            "How do you create a tuple with one element?": "By adding a comma after the element, e.g., (5,).",
            "Can you change an element inside a tuple after creating it?": "No, tuples are immutable.",
            "What is a list in Python?": "An ordered, mutable collection of items.",
            "Which method adds an item to the end of a list?": "append()"
        },
        "Quiz": [
            ("which of the following data types is immutable ", ["list", "tuple", "dict", "set"], "tuple"),
            ("how do you create an empty dictionary?", ["{}", "[]", "()", "None"], "{}"),
            ("which value pairs with the key value in a dictionary named my_dict?", ["my_dict['key']", "my_dict[key]", "my_dict[key]", "my_dict['key']"], "my_dict['key']")
        ]
    }
}

# --- 2. Helper Functions ---

def print_header(title):
    """Prints a formatted header."""
    print("\n" + "="*60)
    print(f" {title.center(58)} ")
    print("="*60 + "\n")

def get_valid_choice(options_dict):
    """Handles user input for selecting a subject."""
    subjects = list(options_dict.keys())
    for index, subject in enumerate(subjects):
        print(f"{index + 1}. {subject}")
    print("0. Exit")

    while True:
        try:
            choice = int(input("\nEnter the number of your choice: "))
            if choice == 0:
                return None
            if 1 <= choice <= len(subjects):
                return subjects[choice - 1]
            else:
                print(f"Invalid choice. Please enter a number between 0 and {len(subjects)}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# --- 3. Flashcard Module ---

def run_flashcards(subject_data):
    """Runs the flashcard session for the selected subject."""
    flashcards = subject_data["Flashcards"]
    terms = list(flashcards.keys())
    random.shuffle(terms) # Shuffle terms for variety

    print_header(f"FLASHCARDS: {subject_data['name']}")
    print("Type 'reveal' to see the definition, 'skip' for the next card, or 'quit' to exit.")

    for term in terms:
        definition = flashcards[term]
        input(f"\n[Term]: {term}") # Waits for user to press Enter
        
        while True:
            action = input(f"  [Definition]: (Type 'reveal' to see) ").strip().lower()
            if action == 'reveal':
                print(f"    -> {definition}")
                break
            elif action == 'skip':
                print(f"    The definition was: {definition}")
                break
            elif action == 'quit':
                print("\nExiting Flashcards.")
                return
            else:
                print("Invalid command. Please type 'reveal', 'skip', or 'quit'.")
    
    print("\n--- Flashcard deck completed! ---")

# --- 4. Quiz Module ---

def run_quiz(subject_data):
    """Runs the multiple-choice quiz for the selected subject."""
    quiz_questions = subject_data["Quiz"]
    random.shuffle(quiz_questions)
    score = 0
    total = len(quiz_questions)

    print_header(f"QUIZ: {subject_data['name']}")
    
    for i, (question, options, correct_answer) in enumerate(quiz_questions):
        print(f"Question {i+1}/{total}: {question}")
        
        # Shuffle options and map them to numbers
        shuffled_options = list(options)
        random.shuffle(shuffled_options)
        option_map = {}
        for j, option in enumerate(shuffled_options):
            print(f"  {j+1}. {option}")
            option_map[str(j+1)] = option

        while True:
            answer_idx = input("\nEnter your answer (1-4): ").strip()
            if answer_idx in option_map:
                user_answer = option_map[answer_idx]
                if user_answer == correct_answer:
                    print("  Correct! ✅")
                    score += 1
                else:
                    print(f"  Incorrect. The correct answer was: {correct_answer} ❌")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        print("-" * 40) # Separator

    print_header("QUIZ RESULTS")
    print(f"You scored {score} out of {total} ({int((score/total)*100)}%)")
    if score == total:
        print("Perfect score! Excellent work! 🏆")
    elif score >= total / 2:
        print("Good job! Keep practicing.")
    else:
        print("Better luck next time! Review the material and try again.")

# --- 5. Main Menu ---

def main():
    """The main program loop."""
    while True:
        print_header("STUDY SUITE: QUIZ & FLASHCARDS")
        print("Please select a mode:")
        print("1. Flashcards")
        print("2. Quiz")
        print("0. Exit")

        mode_choice = input("\nEnter the number of your choice: ").strip()

        if mode_choice == '1':
            print_header("SELECT A SUBJECT FOR FLASHCARDS")
            selected_subject = get_valid_choice(DATA)
            if selected_subject:
                subject_data = DATA[selected_subject]
                subject_data['name'] = selected_subject
                run_flashcards(subject_data)

        elif mode_choice == '2':
            print_header("SELECT A SUBJECT FOR QUIZ")
            selected_subject = get_valid_choice(DATA)
            if selected_subject:
                subject_data = DATA[selected_subject]
                subject_data['name'] = selected_subject
                run_quiz(subject_data)

        elif mode_choice == '0':
            print("\nGoodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter 1, 2, or 0.")

if __name__ == "__main__":
    main()