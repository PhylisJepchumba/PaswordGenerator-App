import random

# Define function to generate to shuffle characters of the string

def shuffle(string):
    tempList=list(string)
    random.shuffle(tempList)
    return ''.join(tempList)
#Generate a random Characters (based on ASCII code)

uppercaseLetter1=chr(random.randint(77, 90))
uppercaseLetter2=chr(random.randint(77, 90))
lowercaseletter1=chr(random.randint(100, 107))
lowercaseletter2=chr(random.randint(100, 107))
digit1=chr(random.randint(48, 50))
digit2=chr(random.randint(48, 50))
punctuationsign1=chr(random.randint(33, 36))
punctuationsign2=chr(random.randint(33, 36))

#Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2  + lowercaseletter1+lowercaseletter2+digit1+digit2+punctuationsign1+punctuationsign2
password = shuffle(password)

#print the output
print('Random password is:', password)
