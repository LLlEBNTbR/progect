from socket import *
import random


def generate_math_problem(operation):
    operand1 = random.randint(1, 100)
    operand2 = random.randint(1, 100)

    if operation == '+':
        answer = operand1 + operand2
    elif operation == '-':
        answer = operand1 - operand2
    elif operation == '*':
        answer = operand1 * operand2
    elif operation == '/':
        answer = operand1 / operand2
    elif operation == '^':
        answer = operand1 ** operand2

    problem = f"{operand1} {operation} {operand2}"
    return problem, answer


s = socket(AF_INET, SOCK_STREAM)

s.bind(('ip', port)) # вставьте ip сервера и порт

s.listen(100)

score = 0

user, addr = s.accept()

while True:
    operation = user.recv(1024).decode('utf-8')
    pr, ans = generate_math_problem(operation)
    user.send(f'{pr}|{ans}'.encode('utf-8'))
    play_again = user.recv(1024).decode('utf-8')
    if play_again == 'False':
        break
