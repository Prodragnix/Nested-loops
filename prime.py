start=int(input('Please enter the starting number of your range: '))
end=int(input('Please enter the ending number of your range: '))
for i in range(start,end+1):
    if i>1:
        for y in range(2,i):
            if (i%y)==0:
                break
        else:
            print(i)