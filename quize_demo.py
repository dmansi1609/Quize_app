import json

# Quiz questions and answers
data = [
    {"question": "What is the capital of France?", "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"], "answer": "C"},
    {"question": "Which language is used for web development?", "options": ["A) Python", "B) HTML", "C) C++", "D) Java"], "answer": "B"},
    {"question": "What is the square root of 64?", "options": ["A) 6", "B) 7", "C) 8", "D) 9"], "answer": "C"}
]

def run_quiz(questions):
    score = 0
    for item in questions:
        print(f"\n{item['question']}")
        for option in item['options']:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == item['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {item['answer']}")
    print(f"\nYour final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    print("Welcome to the Simple Quiz App!")
    run_quiz(data)
