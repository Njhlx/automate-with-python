#Collatz序列

def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print(number)
    elif number % 2 == 1:
        number = 3 * number + 1
        print(number)


print('请输入一个整数')
number = int(input())
collatz(number)

while number == 4:
    x = collatz(number)
    number = collatz(x)


# while number != 1:
#     number = collatz(number)
#     collatz(number)

