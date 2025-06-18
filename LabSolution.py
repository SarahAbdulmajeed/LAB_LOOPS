#1 for loop
for i in range(45,210):
    if i == 100:
        continue
    elif i == 205:
        break
    else:
        print(i)

#2 while
while int(input("what is the product of 7 * 24 ?")) != (7 * 24):
    print("Your Answer is wrong try again..")
else:
    print("You answered this Question correctly")