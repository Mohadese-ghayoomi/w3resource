def Prime(num):
    if num>=2:
        for x in range(2,num):
            if num%x==0:
                print(num, "is not prime")
                break
            elif num%x!=0:
                print(num,"is a prime")
                break
    else:
        print("enter a number larger than 2")
-----------------------------------------------
def Prime(num):
    if num>=2:
        for x in range(2,num):
            if num%x==0:
                return False
        return True

