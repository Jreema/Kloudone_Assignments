#print the list of fibonacci series using generators
no = int(input("Enter the numberof items in fibonacci series: "))
def fibon(max_items):
    f,s =0,1
    for _ in range(max_items):
        yield f
        f,s = s,f+s
        
for i in fibon(no):
    print(i,end="\t")