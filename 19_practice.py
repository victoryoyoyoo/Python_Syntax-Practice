# A simple quiz game to practice Class and Object!
from question import Question 

# Prepare the question text and choices
test = [
    "1 + 3 = ?\n(a) 2\n(b) 3\n(c) 4\n\n",
    "How many centimeters are in 1 meter?\n(a) 10\n(b) 100\n(c) 1000\n\n",
    "What color is a banana?\n(a) Black\n(b) Yellow\n(c) White\n\n"
]

# Pack the question text and the correct answer together into 'Question' objects
questions = [
    Question(test[0], "c"),
    Question(test[1], "b"),
    Question(test[2], "b"),
]

# The main logic to run the quiz
def run_test(q_list):
    score = 0
    
    # Loop through every question in our list
    for q in q_list:
        # Show the question and wait for the user to type their answer
        user_answer = input(q.description)
        
        # Check if they got it right
        if user_answer == q.answer:
            score += 1
            
    # Show the final result
    print(f"You got {score} points! Total questions: {len(q_list)}")

run_test(questions)