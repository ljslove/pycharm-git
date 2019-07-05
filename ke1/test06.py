



def add(a,b):
    c=0
    if (isinstance(a,int) or isinstance(a,float)) and (isinstance(b,int) or isinstance(b,float)):
        c=a+b
    else:
        print("请输入整数或者小数")
    print(c)

add(1,34)
add(12.4,13.4)
#add("454",233)
#add("889","899")
add(454,"7889")
print("testtestetetr")


