#1first program
"""print("hello")"""

#comments
"""
print("hello world","deifjdfidjfdfdifjfj",end="  ")
print("hello world","deifjdfidjfdfdifjfj","shdkjsdhsk")
print("hello world","deifjdfidjfdfdifjfj",end=" joker   ") #jfnsfnfdjdndj
#single line comment
"""

#2variables
"""
var1 = "hello world" # declaring variables
var4 = " harry"
var2 = 4
var3 = 35.5
print(type(var1),end= "  ") #identifying type of variables by using "type"
print(type(var2),end = "  ")
print(type(var3))
print(var1+var4) #adding two variables by +
print(var3+var2)
"""
"""
var5 ="45"
var6 =" 56"
print(var5+var6) #output is 45 56 as it is a string

#so we use typecasting

print(int(var5)+int(var6)) #output is 101,it will know that this is an integer

#to print a string multiple times
print(100*"hello\n")
print(100*int(var5)+int(var6)) #it will multiply by var5 only
print(100* str(int(var5)+int(var6))) #it will print the string resulting from addition 100 times
"""

#3 Taking input from user
"""
print("Enter your number")
inpnum = input()
print("you entered\n ",inpnum)
print("you entered\n ",int(inpnum)+10)
print("enter your name")
inpnum =input()
print("your name is ",inpnum)
"""

#QUIZ 1 - SIMPLE CALCULATOR

"""
print("Enter first number: ")
n1 = input()
print("Enter second number: ")
n2 = input()
print("Sum of these numbers is:\n",int(n1)+int(n2))
"""

#4 STRINGS
"""
mystr = "this is python" #declaring a string
print(mystr) #to print the string
print(mystr[3]) #to print a specific character in the string
print(mystr[0:3]) #to print a portin of the string,also element at index 3 is excluded
print(len(mystr)) #to print the length of the string
print(mystr[0:14]) #to print the entire string
print(mystr[0:14:2]) #skips 1 character
print(mystr[0:14:3]) #skips 2 characters
print(mystr[0:]) #prints the entire string
print(mystr[:3]) #automatically picks up 0 and print upto the range
print(mystr[:]) #prints entire string
print(mystr[::]) #prints entire string
print(mystr[-5:-2]) #starts reverse counting by -1
print(mystr[9:12]) #replace negative indices by their respective positive indices (to resolve negative indices)
print(mystr[::-1]) #to invert the string
print(mystr[::-2]) #to invert the string and skip 2 characters
"""

#5 STRING FUNCTIONS
"""
mystr= "this is python"
print(mystr)
print(mystr.isalnum()) #checks whether the string is alphanumeric
print(mystr.isalpha()) #checks whether ths string is alpha
print(mystr.endswith("on")) #checks if the string ends with 'on'
print(mystr.count("p")) #checks how many time p appears in string
print(mystr.capitalize()) #capitalize the string
print(mystr.find("is")) #find the index of the character
print(mystr.lower()) #prints all the letters in lowercase
print(mystr.upper()) #prints all the letters in uppercase
print(mystr.replace("is","are")) #replaces 1st by 2nd
"""
#6 LIST AND LIST FUNCTIONS

grocery = ["harpic","vim bar","bhindi","lollipop"]       #creating list
print(grocery)
grocery = ["harpic","vim bar","bhindi","lollipop",56]    #list can include numbers as well
print(grocery)
grocery = ["harpic","vim bar","bhindi","lollipop"]
print(grocery[0])                                        #printing certain item from the list
print(grocery[1])
print(grocery[2])
print(grocery[3])
#gives error at 4th index as we have only 4 elements - print(grocery[4])

