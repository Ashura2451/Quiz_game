from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    q_text = question["question"]
    q_answer = question["correct_answer"]

    quest = Question(q_text, q_answer)
    question_bank.append(quest)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("YOU HAVE COMPLETED THE QUIZ")

print(f"YOUR FINAL SCORE IS {quiz.score} / {len(question_bank)}")