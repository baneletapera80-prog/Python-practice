quiz = []

def add_question(question, options, correct_answer):
    quiz.append({
        'question': question,
        'options': options,
        'correct_answer': correct_answer
    })  

def get_questions():
    return quiz

def clear_quiz():
    quiz.clear()

def main():
    while True:
        print("\nQuiz Application Menu:")
        print("1. Add Question")
        print("2. View Questions")
        print("3. Clear All Questions")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            question = input("Enter the question: ")
            options = input("Enter options separated by commas: ").split(',')
            correct_answer = input("Enter the correct answer: ")
            add_question(question, options, correct_answer)
            print(f"Added question: '{question}'.")

        elif choice == '2':
            questions = get_questions()
            if questions:
                for idx, item in enumerate(questions, start=1):
                    print(f"\nQuestion {idx}: {item['question']}")
                    for opt_idx, option in enumerate(item['options'], start=1):
                        print(f"  {opt_idx}. {option}")
                    print(f"Correct Answer: {item['correct_answer']}")
            else:
                print("No questions available.")

        elif choice == '3':
            clear_quiz()
            print("All questions cleared.")

        elif choice == '4':
            print("Exiting Quiz Application.")
            break

        else:
            print("Invalid choice. Please try again.")  

if __name__ == "__main__": 
    main()