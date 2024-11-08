def func_case(str):
    lower = 0
    upper = 0
    for i in range(len(str)):
        if str[i].islower():
            lower+=1
        else:
            upper+=1
    print("lower cases:",lower)
    print("upper cases:",upper)




a=input("enter a string")
func_case(a)
