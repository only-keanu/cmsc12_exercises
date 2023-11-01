'''
Name: Keane Keiph T. Hernandez
Section: CD-1L
Student Number:2020-65960
Brief description of the program:

This program tells the user if their inputted brewing method and brewing time is
perfectly extracted, under-extracted, or over-extracted.
'''


brewingMethod = input('Enter your chosen brewing method in all caps (only one of the ff: DRIP,FRENCH PRESS,ESPRESSO,COLD BREW): ')
brewingTime = float(input('Enter the brewing time (in minutes) : '))

if(brewingMethod=='DRIP'):
    if(brewingTime*60>=270 and brewingTime*60<=330):
        print('Perfectly extracted!')
    elif(brewingTime*60<270):
        print('Under-extracted!');
    elif(brewingTime*60>330):
        print('Over-extracted!');
elif(brewingMethod=='FRENCH PRESS'):
    if(brewingTime*60>=120 and brewingTime*60<=240):
        print('Perfectly extracted!')
    elif(brewingTime*60<120):
        print('Under-extracted!');
    elif(brewingTime*60>240):
        print('Over-extracted!');

elif(brewingMethod=='ESPRESSO'):
    if(brewingTime*60>=20 and brewingTime*60<=30):
        print('Perfectly extracted!')
    elif(brewingTime*60<20):
        print('Under-extracted!');
    elif(brewingTime*60>30):
        print('Over-extracted!');

elif(brewingMethod=='COLD BREW'):
    if(brewingTime*60>=39600 and brewingTime*60<=43200):
        print('Perfectly extracted!')
    elif(brewingTime*60<39600):
        print('Under-extracted!');
    elif(brewingTime*60>43200):
        print('Over-extracted!');

else:
    print('Please enter a proper brewing method!')

