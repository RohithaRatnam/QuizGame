from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
#from quiz_brain import QuizBrain

question_bank = []


for question in question_data:
    q = question['text']
    a = question['answer']
    question_bank.append(Question(q, a))

quiz = QuizBrain(question_bank)
while len(quiz.questions_list)!=quiz.question_number:
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
