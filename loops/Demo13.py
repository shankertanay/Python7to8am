
no = int(input("Enter a No :"))

sum = 0

while no != 0:
    r = no%10
    no = no//10
    sum+=r

print("The sum = ",sum)