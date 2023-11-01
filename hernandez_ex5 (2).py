'''

Name: Keane Keiph T. Hernandez
Section: CD-1L
Student Number:2020-65960
Brief description of the program:

This program translates Filipino words into tadbalik words
'''

def tadbalik(word): #Function used to translate word to tadbalik Filipino word
    

    word = word.lower() #Converts word to check to lowercase
    syllableCount =0;
    vowels = 'aeiuoy'
    repeat = 0
    for i in range(0,len(word)): #Checks if there is more than 1 syllable 
        if(word[i-1] in vowels and word[i]!=word[i-1]):
            syllableCount+=1

    if(word=='mga'): #Checks 'mga' word exception 
        return word
    elif(len(word)<=3): #Checks if character count is less than 3
        return word 
    elif(syllableCount==1): #Checks if vowel count is only 1 then returns  
        return word

    elif(word[len(word)-1] in vowels): #Checks if last character is vowel
        i=1
        while(word[len(word)-i]== word[len(word)-(i+1)]):
            repeat+=1
            i+=1
        if(word[len(word)-2] =='g' and word[len(word)-3]=='n'):
            return word[len(word)-3:]+word[0:len(word)-3]  #Returns new tadbalik word
        else:    
            return word[len(word)-2-repeat:]+word[0:len(word)-2-repeat] #Returns new tadbalik word
    elif not (word[len(word)-1] in vowels):#Checks if last character is consonant
        i=1
        while(word[len(word)-i]== word[len(word)-(i+1)]):
            repeat+=1
            i+=1
        if(word[len(word)-2] =='n' and word[len(word)-3]=='o'):
            return word[len(word)-4:]+word[0:len(word)-4] #Returns new tadbalik word
        elif(word[len(word)-2] in vowels and word[len(word)-3] in vowels):
            return word[len(word)-2:]+word[0:len(word)-2] #Returns new tadbalik word
        else:
            return word[len(word)-3-repeat:]+word[0:len(word)-3-repeat] #Returns new tadbalik word


list_words = [] #List of words
N = int(input('\nEnter the number of words: ')) #Indicates number of user-defined words
for i in range(0,N):
    word_entry = input('> ') #Inserts word
    list_words.append(word_entry) #Adds to word list

print('\nThe translated words are:')
for translated in list_words:
    print('>',tadbalik(translated)) #Prints new list

    #taob 