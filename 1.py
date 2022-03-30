number = str(input())


def solution(number):
    stack = []
    if number[0] == ')':
        return False
    for i in number:
        if i == '(':
            stack.append(i)
        else:
            stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False


if solution(number) == True:
    print('Correct')
else:
    print('Incorrect')