'''
Name: Keane Keiph T. Hernandez
Section: CD-1L
Student Number:2020-65960
Brief description of the program:

This program simulates the POS system of a burger restaurant
'''

def mainMenu():#Displays main menu

    print('\nMAIN MENU')
    print('[1] Choose burgers')
    print('[2] Add drinks')
    print('[3] Compute total and pay')
    print('[4] Exit')
    choice = input('Enter your chosen task: ')
    if(choice=='1' or choice=='2' or choice=='3' or choice=='4'):
        return choice
    else:
        print('\nPlease make a valid choice!\n')
        choice = mainMenu()
        return choice         
def addBurger():#Display burger menu and adds burgers to shopping cart
    print('\nBURGERS\n')
    print('[1] Etinum Regrub: P35.00')
    print('[2] Double Etinum Regrub: P47.00')
    print('[3] Bacon Cheese Regrub: P73.00')
    print('[4] Triple Onion Regrub: P600.00')
    print('[0] Back to main menu')
    burgerChoice = input('Enter your chosen option: ')
    return burgerChoice
def addDrinks():#Adds drinks to shopping cart and displays total price of drinks
    print('\nEach drink costs P25.50')
    drinkAmount = int(input('How many drinks would you like to order? '))
    return drinkAmount*25.50
def serviceCharge(totalPrice): #Computes service charge by restaurant 
    return totalPrice+totalPrice*0.07
def discountPrice(totalPrice): #Computes discount price if there is a PWD/Senior Citizen ID
    return totalPrice*0.8
def computeBill(totalPrice): #Computes the total price from shopping cart
    print('\nYour total is P'+(str(totalPrice)))
    if(totalPrice>0):
            print('Your total with service charge of 7%: P'+str(serviceCharge(totalPrice)))
            totalPrice = serviceCharge(totalPrice)
            discountID =input('Do you have a PWD ID or a Senior Citzen ID?(y/n): ')
            if(discountID=='y'): #Makes sure if valid choice
                print('Your total bill with 20%'+' discount: P'+str(discountPrice(totalPrice)))
                return discountPrice(totalPrice)
            else:
                return totalPrice
                
    else:
        return 0
def changeCalculator(totalComputed): #Computes the change from amount given by customer
    amountGiven = float(input('Enter amount to pay: '))
    if(amountGiven>totalComputed): #Makes sure amount is greater than total amount
        print('Your change is: P'+str(amountGiven-totalComputed))
        print('\nThank you for shopping!')
    else: #If amount is not a number then request for a valid amount and calls function again
        print('Please enter a valid amount!')
        changeCalculator(totalComputed)

print('WELCOME TO ETINUM REGRUB\n') #Welcome display
currentBill = 0  #Initializes current bill 
burgerCosts = 0
drinkCosts = 0
option = mainMenu() #Initialize menu choice
while(True): #Continuously run program while customer hasn't exitted 
    while(option=='1'): #Continuously show burger menu while customer hasn't exitted
        burger = addBurger()
        #Computes for different burger options to current bill
        if(burger=='1'):
            burgerCosts += 35
        elif(burger=='2'):
            burgerCosts += 47
        elif(burger=='3'):
            burgerCosts += 73
        elif(burger=='4'):
            burgerCosts += 600
        elif(burger=='0'):
            print('The burger/s costs P'+str(burgerCosts))
            currentBill+= burgerCosts;
            print('Your current bill is valued at P'+str(currentBill))
            option = mainMenu()
        if not(burger=='0'):
            print('Your order has been placed!') #Confirms order to customer
    if(option=='2'): #Add drink to shopping cart
        drink = addDrinks()
        drinkCosts += drink #Adds drink/s cost/s to current bill
        print('The drinks costs a total of P'+str(drinkCosts)) #Displays total drink bill
        currentBill += drinkCosts
        print('Your current bill is valued at P'+str(currentBill))
        option = mainMenu() #Goes back to main menu
    elif(option=='3'): #Computes for total bill
        totalBill = computeBill(currentBill) 
        if(totalBill>0): #Checks if total bill is not 0 
            changeCalculator(totalBill)
            currentBill = 0
            drinkCosts = 0
            burgerCosts = 0
            option = mainMenu()
        else:
            option = mainMenu()
    elif(option=='4'): #Exits program
        print('\nGoodbye!') 
        break