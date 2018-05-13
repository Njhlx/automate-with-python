#global语句

def spam():
    global eggs
    eggs = 'spam'
    print(eggs)

eggs = 'global'
print(eggs)
spam()
