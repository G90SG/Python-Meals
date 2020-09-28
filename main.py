#1. Write a program that allows user to enter his favourite starter, main course, dessert and drink. Output a message which says – “Your favourite meal is  ………with a glass of….”

print("Hello!")
name = input("what's your name?")
starter = input("Hey," + name + " what is your favourite Starter?")
main = input("What about Main Course, what would you have?")
dessert = input("I'm not so fond of " + main 
+ " I prefer Pizza. What about dessert, what would you order? ")
drink = input("Great choice! What would you like to drink?")
print("Your favourite meal is " + starter + " 
followed by " + main + " and " + dessert + ", accompanied by a lovely glass of " + drink + "." )
