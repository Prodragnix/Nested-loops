word=input('Please enter a word: ')
letter=input('Please enter your letter: ')
count=0
i=0
while i <len(word):
    if word[i]==letter:
        count=count+1
    i=i+1
print('The number of times '+letter+' occurs is:',count)