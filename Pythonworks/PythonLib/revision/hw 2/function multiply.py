def multiply_function(a):
    result=1
    for i in range(len(a)):
        result*=a[i]
    print(result)
multiply_function([3,2,4])