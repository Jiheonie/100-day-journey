from question_model import Question
from quiz_brain import QuizBrain
from data import question_data


question_bank = []
for question in question_data:
    new_q = Question(question["question"], question["correct_answer"])
    question_bank.append(new_q)


quiz_game = QuizBrain(question_bank)


while quiz_game.still_has_question():
    quiz_game.next_question()


print("You've completed the quiz")
print(f"Your final score is: {quiz_game.score}/{quiz_game.question_number}")