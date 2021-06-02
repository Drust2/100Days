class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0
        
    def still_has_questions(self):
        num_questions = len(self.questions_list)
        # return self.question_number < len(self.questions_list) works better
        if num_questions == self.question_number:
            return False
        else:
            return True
        
    def check_answer(self, answer, correct):
        correct_answer = correct.lower()
        user_answer = answer.lower()
        if (correct_answer == user_answer):
            self.score += 1
            print("That is correct. +1 point.")
        else:
            print(f"That is incorrect. The correct answer was {correct_answer.title()}")
            
        print(f"Your current score is: {self.score}/{self.question_number}\n")
    
    def next_question(self):
        current_question = self.questions_list[self.question_number]
        correct_answer = self.questions_list[self.question_number].answer
        self.question_number += 1
        user_answer = input (f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, correct_answer)


        
        