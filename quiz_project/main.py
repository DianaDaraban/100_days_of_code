from question_model import Question
from data import question_data
from quiz_brain import  QuizBrain

questions_bank = []
for question in question_data:
    q_text = question['text']
    q_answer = question['answer']
    new_question = Question(q_text, q_answer)
    questions_bank.append(new_question)

quiz = QuizBrain(questions_bank)

while quiz.still_has_questions():
    quiz.next_question()
else:
    print('You completed the quiz!')
    print(f'Your final score is {quiz.score}/{quiz.question_number}.')