'''4.	Create a list. Append the names of your colleagues and friends to it.
 Has the id of the list changed? Sort the list. What is the first item on the
  list? What is the second item on the list? '''

list = ['ram']
list_length = len(list)
for colleagues in range(list_length):
    list.append("krishna")

print(f'names of colleagues and friends are',list)
print(f'sorted form of names are:',sorted(list))