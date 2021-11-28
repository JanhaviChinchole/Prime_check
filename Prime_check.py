def prime_check(num):
    if num==1:
        print("1 is not a prime number")
    if num==2:
        print("2 is a prime number")
    for x in range (2,num):
        if num%x==0:
            print(f"{num} is not a prime number")
            break
        else:
            print(f"{num} is a prime number")
prime_check(7)
prime_check(4)