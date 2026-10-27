from question import Question

test = [
    "1 + 3 = ?\n(a) 2\n(b) 3\n(c) 4\n\n",
    "How many centimeters are in 1 meter?\n(a) 10\n(b) 100\n(c) 1000\n\n",
    "What color is a banana?\n(a) Black\n(b) Yellow\n(c) White\n\n"
]

questions = [
    Question(test[0], "c"),
    Question(test[1], "b"),
    Question(test[2], "b"),
]

def run_test(q_list):
    score = 0

    for q in q_list:
        user_answer = input(q.description)

        if user_answer == q.answer:
            score += 1

    print(f"You got {score} points! Total questions: {len(q_list)}")

run_test(questions)
