'''
Name: Keane Keiph T. Hernandez
Section: CD-1L
Student Number:2020-65960
Brief description of the program:

This program takes in a number n from the user and outputs number of odd and even digits.
'''
while(True):
    num = int(input('\nEnter a number n:')) #Takes in number n from user
    oddDigit = 0 #Initializes odd digits
    evenDigit = 0 #Initializes even digits
    if(num>0): #Checks if number is greater than 0
        while(num>0):
            digit = num%10 #Takes each nth digit by getting the remainder when divided by 10
            if(digit%2==0): #Checks if digit is even
                evenDigit = evenDigit + 1 #Even digit counter
            else:
                oddDigit = oddDigit + 1 #Odd digit  counter
            num = num//10 #Divides number by 10 to move on to next digit
        print('Even digits',evenDigit) #Displays number of even digits
        print('Odd digits:',oddDigit) #Displays number of odd digits
    else:
        print('Goodbye!') #Displays goodbye message
        break #Breaks while-loop
        