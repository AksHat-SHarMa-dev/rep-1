# n = int(input("Enter a number:"))
# for i in range(1,11):
#     print(f"the table is :{n*i}")\
# l = ["Harry","Sachin","Soham","Rahul"]
# for name in l:
#     if (name.startswith("S")) :
#         print(f"Hello {name}")
#     else :
#         print (f"No greet {name}")

# n = int(input("Enter a number"))
# i=1
# while i<=10:
#     print(f"The table is:{n*i}")
#     i+=1

# n=int(input("Enter your number:"))
# for i in range(2,n):
#     if n%i==0 :
#         print("The no is not prime")
#         break 
#     else:
#         print("the no is prime")
#         break
n=int(input("Enter your number:"))
for i in range(0,n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("My name is lakhan")