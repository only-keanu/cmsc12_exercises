'''
Name: Keane Keiph T. Hernandez
Section: CD-1L
Student Number:2020-65960
Brief description of the program:

This program computes the individual time taken by person A and person B given names of person A,B, multiplier of person B in comparison to person A and total time it would take if person A and B were to work together.


'''

personA = input("Enter the name for person A: ")
personB = input("Enter the name for person B: ")

workingTimeT = float(input("What time (in hours) will it take for " +str(personA)+ " and "+str(personB) + " to finish the work together:"))
multiplerB = float(input("Enter the multiplier for person B:"))


I1 = workingTimeT*(multiplerB+1)/multiplerB
I2 = I1 * multiplerB

print(str(personA)+" would take " + str(I1)+ " hours to finish assembling the furniture while "+ str(personB) +" would take " +str(I2)+ " hours.")



