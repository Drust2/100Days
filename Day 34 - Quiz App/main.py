from question_model import Question
import data
from quiz_brain import QuizBrain
import ui


question_bank = []
questions = data.Questions()
question_data = questions.question_data 
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
window = ui.Ui(quiz)


while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

