def fact_rec(n):
If n==0 or n ==1:
return 1
else:
return n*fact_rec(n-1)
num=int(input("enter the value:"))
res = fact_rec(number)
print("the factorial of {} is {}".format(number,res)