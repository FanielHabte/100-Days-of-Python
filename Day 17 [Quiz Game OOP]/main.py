from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for questions in question_data:
    text = questions['question']
    answer = questions['correct_answer']
    new_q = Question(text, answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
# quiz.next_question()
# # answer = quiz.answer

while quiz.still_has_questions():
    if quiz.check_answer:
        quiz.next_question()


if not quiz.still_has_questions():
    print("You have completed the quiz!")
    print(f"Your final score was: {quiz.current_score}/{quiz.question_number}")
