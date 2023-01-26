# Stack : The stack is a linea data structure. LIFO mechanisum
# Push, Pop, Peek, DIsplyed
a = []
while True:
    b = int (input('''
        1 Push Element
        2 Pop Element
        3 Peek Element
        4 Display Element
        5 Exit
    '''))
    if b==1:    # Push
        n=input("Enter the value")
        a.append(n)
        print(a)
    elif b==2:    # Pop
        if len(a)==0:
            print("Empty Stack")
        else:   
            p=a.pop()
            print(p)
            print(a)
    elif b==3:    # Peek
        if len(a)==0:
            print("Empty Stack")
        else:
            print("Last Stack Value",a[-1])
    elif b==4:
            print("Display Stack",a)
    elif b==5:
        break