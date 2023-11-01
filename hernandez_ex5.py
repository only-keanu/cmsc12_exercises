'''

Name: Keane Keiph T. Hernandez
Section: CD-1L
Student Number:2020-65960
Brief description of the program:
'''

#

def tadbalik(word):
    #bakit

    word = word.lower()
    vowelCount =0;
    vowels = 'aeiuoy'
    for i in range(0,len(word)):
        if(word[i-1] in vowels and word[i]!=word[i-1]):
            vowelCount+=1

    if(word=='mga'):
        return word
    elif(len(word)<=3):
        return word 
    elif(vowelCount==1):
        return word
    elif(word[len(word)-1] in vowels):
        if(word[len(word)-2] =='g' and word[len(word)-3]=='n'):
            return word[len(word)-3:]+word[0:len(word)-3]
        else:    
            return word[len(word)-2:]+word[0:len(word)-2]
    elif not (word[len(word)-1] in vowels):

        if(word[len(word)-2] =='n' and word[len(word)-3]=='o'):
            return word[len(word)-4:]+word[0:len(word)-4]
        elif(word[len(word)-2] in vowels and word[len(word)-3] in vowels):
            return word[len(word)-2:]+word[0:len(word)-2]
        else:
            return word[len(word)-3:]+word[0:len(word)-3]
#salubong ->bongsalu

list_words = []
N = int(input('\nEnter the number of words: '))
for i in range(0,N):
    word_entry = input('> ')
    list_words.append(word_entry)

print('\nThe translated words are:')
for translated in list_words:
    print('>',tadbalik(translated))

    #taob 