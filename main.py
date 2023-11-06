from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []  # Create a list to store the Question instances

for question in question_data:
    text = question['text']
    answer = question['answer']
    the_question = Question(text, answer)  # Create a Question instance
    question_bank.append(the_question)  # Append the instance to the list


quiz = QuizBrain(question_bank)

while quiz.is_still_has_question():

    quiz.next_question()
print("You've completed the quiz")
print(f"your score: {quiz.user_score}")
