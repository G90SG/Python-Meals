# Write a program that allows user to enter his favourite starter, main course, dessert and drink. Output a message which says – “Your favourite meal is  ………with a glass of….”

print("Hello!")
# Obtain inout from the user, asking their name 
name = input("What's your name? ")
# Concatenate the name inout within the string asking the user what their favourite starter is 
starter = input("Hey " + name + ", what is your favourite starter? ")
main = input("What about main course, what would you have? ")
dessert = input("I'm not so fond of " + main 
+ ", I prefer Pizza. What about dessert, what would you order? ")
drink = input("Great choice! What would you like to drink? ")
# Taking all input variables from above, print a string advising of their favourite meal
print ("\n")
print("Your favourite meal is " + starter + ", followed by " + main + " and " + dessert + ", accompanied by a lovely glass of " + drink + "." )
