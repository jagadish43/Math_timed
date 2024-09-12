import random
import time

OPERATORS = ["+", "-","*"]
MIN_OPERAND = 2
MAX_OPERAND = 15
TOTAL_PROBLEMS = 10


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) +" "+operator+" "+str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0
input("Press enter to start!")
print("----------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem - " + str(i + 1) + ": "+expr +" = ")
        if guess == str(answer):
            break

end_time = time.time()
total_time = end_time - start_time

print("----------------------")
print("Nice Work! You Finished in " + str(total_time) + " Seconds")