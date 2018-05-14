#Collatz序列，不论录入啥数字，最终结果都是1哦

def collatz(number):
    if number % 2 == 0:
        number = number // 2
        return (number)
#        print(number)
    elif number % 2 == 1:
        number = 3 * number + 1
        return (number)
#        print(number)

print('请输入一个整数')
number = int(input())
x = collatz(number)
while x != 1:
    print(x)
    x = collatz(x)
else:
    print(x)

