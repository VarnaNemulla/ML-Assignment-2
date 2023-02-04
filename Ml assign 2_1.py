rows = 5     #taking standard row number as 5
for i in range(0, rows):    #using for loop to dispaly the star pattern from 0 to rows 
    for j in range(0, i + 1):
        print("*", end=' ') #Displaying '*' in the output
    print("\r")             

for i in range(rows, 0, -1):  #using for loop to dispaly the star pattern from 0 to -1
    for j in range(0, i - 1):
        print("*", end=' ')   #Displaying '*' in the output
    print("\r")    
