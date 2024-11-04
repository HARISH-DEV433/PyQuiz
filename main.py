from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for quest_list in question_data:  # Iterate over the outer list
    for quest in quest_list:  # Iterate over each dictionary inside the inner list
        question_text = quest["question"]
        question_answer = quest["correct_answer"]
        new_q = Question(question_text, question_answer)
        question_bank.append(new_q)


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")