def fact_function(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    print("factorial is:",fact)
fact_function(5)
