import random
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = q_list

    def next_question(self):
        current_question = random.choice(self.questions_list)
        self.questions_list.remove(current_question)
        self.question_number += 1
        user_answer = input(f"{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_question(self):
        return len(self.questions_list) > 0

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"You got it right:")
        else:
            print("That's wrong:")
        print(f"Answer is: {correct_answer}.")
        print (f"Your score is: {self.score}, for {self.question_number} number of questions")
        print("\n")

