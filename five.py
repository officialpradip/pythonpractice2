'''Create a tuple with your first name, last name, and age. Create a list,
people, and append your tuple to it. Make more tuples with the
corresponding information from your friends and append them to the
list. Sort the list. When you learn about sort method, you can use the
key parameter to sort by any field in the tuple, first name, last name,
or age.
'''

bio = ("Pradip", "Thapa", 21)
people = [bio]
people.append(("Ram","karki",22))
people.append(("Hari","Dahal",42))
people.append(("Anup","Pokharel",49))

people.sort()

print(people)
