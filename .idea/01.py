#This program says hello and asks for my name.

print ('hello world')
print ('What is your name?')    #ask for their name
myName = input()
print ('It is good to mennt you,' + myName)
print ('The length of your name is:')
print (len(myName))
print ('What is you age?')  #ask for their age
myAge = input()
print ('You will be ' + str(int(myAge) + 1) + ' in a year.')