a = str(input())


def solution(a):
    stack = []
    if a[0] == ')':
        return False
    for i in a:
        if i == '(':
            stack.append(i)
        else:
            stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False


if solution(a) == True:
    print('Correct')
else:
    print('Incorrect')