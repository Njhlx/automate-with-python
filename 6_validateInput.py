
while True:
    print('请输入您的年龄')
    age = input()
    if age.isdecimal():
        break
    print("请正确输入您的年龄")

while True:
    print('请输入您的密码（数字或字母）')
    password = input()
    if password.isalnum():
        break
    print('密码只能是数字或字母')