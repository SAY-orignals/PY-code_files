def fib(nterm):
    n1,n2=0,1
    count = 0
    while count<nterm:
        print(n1)
        nth = n1 + n2
        n1=n2
        n2=nth
        count+=1
nterm = int(input("Enter a term: "))
if nterm<=0:
    print("Please enter a natural number!")
elif nterm==1:
    print("Fibonacci series until ",nterm,":")
    fib(nterm)
else:
    print("Fibonacci series untill ",nterm,":")
    fib(nterm)