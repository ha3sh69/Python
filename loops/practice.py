# n=int(input("enter the number"))
# for i in range(0,11):
#     print(f'{n}X{i}={n*i}') 




# l=["harsh","batman","boogeyman","harry"]
# for name in l:
#     if(name.startswith('b')):
#         print(f'hello {name}')


# n=int(input("enter the number: "))

# i=1

# while (i<11):
#     print(f'{n} X {i} = {n*i}')
#     i+=13

# n=int(input("enter the number: "))
# for i in range(2,n):
#     if(n%2==0):
#         print("the number is not prime")
#         break
# else:
#     print("the number is prime")


# n= int(input("enter the number: "))
# i=1
# sum=0
# while(i<=n):
#     sum+=i
#     i+=1

# print(sum)


n=int(input("enter the number: "))
product=1
for i in range(1,n+1):
    product = product*i
    print(f'the factorial of {n} is {product}')
else:
    print("done")

