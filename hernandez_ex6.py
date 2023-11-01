'''

Name: Keane Keiph T. Hernandez
Section: CD-1L
Student Number:2020-65960
Brief description of the program:

This program simulates a simple bookstore using dictionaries and functions
'''

def printMenu(): #Function used to display the main menu
    print('\nMAIN MENU\n')
    print('[1] Add Book')
    print('[2] View All Books')
    print('[3] Delete a Book')
    print('[4] Delete All Books')
    print('[5] Restock a Book')
    print('[6] Consume a Book')
    print('[0] Exit')
    choice = input('\nEnter choice: ')
    return choice

def addBook(d1): #Function used to add books to the simple bookstore system
    print('\nADD BOOK\n')
    code = int(input('     Enter book code:')) #Input book code
    if(code in d1): #Checks if book already exists
        print('     Book already exists.')
    else: #Enters book details
        title = input('     Enter book title: ')
        author = input('     Enter book author: ')
        quantity = int(input('     Enter book quantity: '))
        d1[code] = [title,author,quantity]
        print('     \n     The book has been sucessfully added') #Confirms if book is added
        return d1
def viewBook(d1): #Function used to view books 
    print('\nVIEW BOOKS\n')
    if(len(d1)==0): #Checks if book inventory is empty
        print('     The inventory is empty. Nothing to view')
    else:
        for k,v in d1.items(): #Displays all books
            print('     Book Code: ', k)
            print('     Book Title: ',v[0])
            print('     Book Author: ',v[1])
            print('     Book Quantity: ',v[2],'\n')
def delete(d1,code): #Function used to delete books 
    
    if(code in d1):
        print('     You have deleted',d1[code][0], 'by',d1[code][1])
        d1.pop(code)
        return d1
    else:
        print('     Code not in inventory')
        return d1

def deleteAll(d1): #Function used to delete all books 
    print('\nDELETE ALL BOOKS\n')
    if(len(d1)==0):
        print('     The inventory is empty. Nothing to delete') 
    else:
        d1.clear() #Clear values for book inventory
        print('     All books has been deleted')
        return d1
def restockBook(d1,code): #Function used to restock books 
    
    if(code in d1): #Check if book is in inventory
        consumed = int(input('     Enter amount to restock: '))
        d1[code][2]+=consumed
        print('     New stock of',d1[code][0],'by',d1[code][1],':',d1[code][2])
        return d1
    else:
        print('     This book does not exist')

def consume(d1,code): #Function used to consume books 
    
    if(code in d1):
        consumed = int(input('     Enter amount to consume: '))
        if(d1[code][2]>=consumed):
            d1[code][2]-=consumed
            print('     Consumed',consumed,'of',d1[code][0],'by',d1[code][1])
            print('     New stock of',d1[code][0],'by',d1[code][1],':',d1[code][2])
            return d1
        else:
            print('     Insufficient/Out of stock')
            return d1
    else:
        print('     This book does not exist')

books = {} #Initializes list of books for bookstore
while True: #Creates an infinite loop of the bookstore system until user exits
    choice = printMenu() #Initializes choice to print main menu
    if choice =='1': #Adds books if choice chosen is 1
        addBook(books)
    elif choice =='2': #View books if choice chosen is 2
        viewBook(books)
    elif choice =='3': #Delete books if choice chosen is 3
        print('\nDELETE BOOK\n')
        if(len(books)==0):
            print('     The inventory is empty. Nothing to delete')
        else:
            code = int(input('     Enter a book code: '))
            delete(books,code)
    elif choice =='4': #Delete all books if choice chosen is 4
        deleteAll(books)    
    elif choice =='5': #Restock books if choice chosen is 5
        print('\nRESTOCK BOOK\n')
        if(books=={}):
            print('     The inventory is empty. Nothing to restock')
        else:
            code = int(input('     Enter a book code: '))
            restockBook(books,code)
    elif choice =='6': #Consume books if choice chosen is 6
        print('\nCONSUME BOOK\n')
        if(books=={}):
            print('     The inventory is empty. Nothing to consume')
        else:
            code = int(input('     Enter a book code: '))
            consume(books,code)
    elif choice =='0': #Exit program if choice chosen is 0
        print('Goodbye!') 
        break  
    else:
        print('Invalid input!')
        print('Please make a valid input') 
        choice = printMenu
