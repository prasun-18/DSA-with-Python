def fact(n):
    if n == 0 or n==1:
        return 1
    return n * fact(n-1)

num = int(input("Enter the number to find the factorial\n"))
res = fact(num)
print("Factorial of", num, "=", res)
