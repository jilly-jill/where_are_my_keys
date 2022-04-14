
import random


questions = ["Do fish fart?", "What does blue taste like?", "What time is it yesterday?", "Do dogs dream"]
question = (random.choice('barrage_of_questions'))
answers = ["Yes", "No", "Sure", "Orange", "62:00PM"]

numbers = random.randrange(1, 11)
if numbers > 5:
    penalty = 5
else:
    penalty = 0

