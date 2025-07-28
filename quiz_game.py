def run_quiz():
    score = 0

    questions = [
        {
            "question": "Which keyword is used to define a function in Python?",
            "choices": ["a) func", "b) define", "c) def", "d) function"],
            "answer": "c"
        },
        {
            "question": "Who directed the movie 'Inception'?",
            "choices": ["a) Christopher Nolan", "b) Steven Spielberg", "c) James Cameron", "d) Martin Scorsese"],
            "answer": "a"
        },
        {
            "question": "What is the output of: print(2 ** 3)?",
            "choices": ["a) 6", "b) 8", "c) 9", "d) 5"],
            "answer": "a"
        },
        {
            "question": "Which animal is known as the 'King of the Jungle'?",
            "choices": ["a) Tiger", "b) Lion", "c) Elephant", "d) Gorilla"],
            "answer": "b"
        }
    ]

    for q in questions:
        print("\n" + q["question"])
        for choice in q["choices"]:
            print(choice)

        answer = input("Your answer (a/b/c/d): ").lower()

        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is {q['answer']}.")

    print(f"\n🏆 You scored {score} out of {len(questions)}!")

while True:
    run_quiz()
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! 👋")
        break
