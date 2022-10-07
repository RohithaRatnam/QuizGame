class QuizBrain():

    def __init__(self, questions):
        self.question_number = 0
        self.questions_list = questions
        self.score = 0

    def check_answer(self, user_answer):
        return self.questions_list[self.question_number].answer == user_answer
    
    def next_question(self):
        current_question = self.questions_list[self.question_number]
        user_answer = input(f"{self.question_number+1}. {current_question.text}? (True/False): ").title()
        if self.check_answer(user_answer):
            self.score+=1
            print("You got it right!")
        else:
            print("That's wrong.")
        self.question_number+=1
        print(f"The correct answer was: {current_question.answer}")
        print(f"Your score is {self.score}/{self.question_number}.")
        print("\n")
        
    
