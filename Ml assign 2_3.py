x = [23,'Python', 23.98] #taking input as list, sting and float
n = []
for i in range(len(x)):  
    n.append(type(x[i]))  #append type of elements from the given list

print(x) 
print(n)       #printing the type of elements
