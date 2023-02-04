def unique_list(l):    #taking unique list function 
  x = []
  for a in l:
    if a not in x:
      x.append(a)      #appending the unique value to the list
  return x
print(unique_list([1,2,3,3,3,3,4,5]))  #printing unique values
