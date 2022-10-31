def printx():
    global list2,list1,win
    print("\t\t\t\t{}|{}|{} \t{}|{}|{}".format(list1[0],list1[1],list1[2],list2[0],list2[1],list2[2]))
    print("\t\t\t\t-+-+- \t-+-+-")
    print("\t\t\t\t{}|{}|{} \t{}|{}|{}".format(list1[3],list1[4],list1[5],list2[3],list2[4],list2[5]))
    print("\t\t\t\t-+-+- \t-+-+-")
    print("\t\t\t\t{}|{}|{} \t{}|{}|{}".format(list1[6],list1[7],list1[8],list2[6],list2[7],list2[8]))

def winner():
    print("\t\t\t\t\t{}|{}|{}".format(list1[0],list1[1],list1[2]))
    print("\t\t\t\t\t-+-+-")
    print("\t\t\t\t\t{}|{}|{}".format(list1[3],list1[4],list1[5]))
    print("\t\t\t\t\t-+-+-")
    print("\t\t\t\t\t{}|{}|{}".format(list1[6],list1[7],list1[8]))

def new():
    print("\n"*5)
    
def xt():
    global list2,list1,win
    new()
    printx()
    print("\t\t\t\t\tX's Turn:")
    ch=int(input("\t\t\t\tEnter the number:"))
    list1[ch-1]='X'
    clear()

def ot():
    global list2,list1,win
    new()
    printx()
    print("\t\t\t\t\tO's Turn:")
    ch=int(input("\t\t\t\tEnter the number:"))
    list1[ch-1]='O'
    clear()

def row():
    global list2,list1,win
    if list1[0]==list1[1]==list1[2]!=' ':
        win=list1[0]
    if list1[3]==list1[4]==list1[5]!=' ':
        win=list1[3]
    if list1[6]==list1[7]==list1[8]!=' ':
        win=list1[6]

def col():
    global list2,list1,win
    if list1[0]==list1[3]==list1[6]!=' ':
        win=list1[0]
    if list1[1]==list1[4]==list1[7]!=' ':
        win=list1[1]
    if list1[2]==list1[5]==list1[8]!=' ':
        win=list1[2]

def dia():
    global list2,list1,win
    if list1[0]==list1[4]==list1[8]!=' ':
        win=list1[0]
    if list1[6]==list1[4]==list1[2]!=' ':
        win=list1[6]

def check():
    global list2,list1,win
    row()
    col()
    dia()

if __name__ == '__main__':
    import os
    clear=lambda:os.system("cls")
        
    while True:
        list2=[x for x in range(1,10)]
        list1=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
        win=0
        i=0
        clear()
        while True:
            i+=1
            xt()
            check()
            if i==5:
                break
            if win!=0:
                break
            ot()
            check()
            if win!=0:
                break
        
        if win==0:
            new()
            print("\t\t\t\tMatch Tied")
            winner()
        else:
            new()
            print("\t\t\t\t{} is the winner".format(win))
            winner()

        print("\t\tPress Yes to play again")
        print("\t\tPress No to Exit")
        cho=input("\tEnter Your Choice:")
        if cho=='no' or cho=='NO'or cho=='No':
            break
        
