import random
def ges():
    guess = random.randint(1,100)
    a = int(input('введите ваше число от 1 до 100 ---'))
    if a == guess:
        print('угадал')
    else :
        print('не угадал')
print(ges())
