def calculate_HCF(p,q):
    if p>q:
        smaller=q
    else:
        smaller=p
    for i in range(1,smaller+1):
        if p%i==0 and q%i==0:
            hcf=i
    return hcf
num1=int(input('enter the value of num1:'))
num2=int(input('enter the value of num2:'))
print("hcf is:",calculate_HCF(num1,num2))