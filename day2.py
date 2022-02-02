#Day 2 Assignment Python

lottery=input("Enter a string:")
print(lottery)
print("choose any character from your entire string")
inputs=input(" ").lower()
if inputs==lottery[1] or inputs==lottery[3] or inputs==lottery[4] or inputs==lottery[6]:
    print("Congratulations,you are win a lottery!")
else:
    print("Sorry,you didn't win a lottery,try next time")

    
