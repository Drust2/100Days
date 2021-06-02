from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

#Initializing the questions
question_bank = []
for i in question_data:
    question_bank.append(Question(i["text"], i["answer"]))

brainage = QuizBrain(question_bank)
more_questions = True
#Main loop of the game
while more_questions == True:
    brainage.next_question()
    more_questions = brainage.still_has_questions()

print(f"\nThat is the end of the quiz. Your final score is {brainage.score} out of {brainage.question_number}")
