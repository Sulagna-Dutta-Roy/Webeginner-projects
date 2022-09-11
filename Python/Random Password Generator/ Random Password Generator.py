import random

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program starts here
#Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter1=chr(random.randint(97,122)) 
uppercaseLetter2=chr(random.randint(48,57))
uppercaseLetter3=chr(random.randint(33,43))
uppercaseLetter4=chr(random.randint(57,96))
uppercaseLetter5=chr(random.randint(128,191))
uppercaseLetter6=chr(random.randint(57,122))


#Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2  + uppercaseLetter3 + uppercaseLetter4 + uppercaseLetter5 + uppercaseLetter6
password = shuffle(password)

#Output
print("Your password is : ")
print(password)
