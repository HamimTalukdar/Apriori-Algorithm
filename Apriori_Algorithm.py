#This is Hamim Talukdar
ln = int(input("Enter Total Transaction number: "))
print("Enter all the items separated by a space:")
print(' T. ID     --     Item set')
print('---------------------------')
ls=[]                   # ls[T. ID, Item set]
mset=set()
for i in range(ln):
    lp=[]
    for j in range(2):
        if j==0:
            p = 'T'+str(i+1)
            lp.append(p.split())
        else:
            print(p,":           => ", end="")
            p = input() 
            l=set(p.split())
            mset.update(l)
            lp.append(l)

    ls.append(lp) 
print()          
    
# pr = input("Enter support in percent: ")
# pr = pr.split('%')
# pr = int(pr[0])
# spt=int(pr*ln//100)
# print("Support = ",spt,"\n")
spt = int(input("Enter the support number: "))


def listPrint(ls, t):    
    print()
    if (t=='t'):
        print(' T. ID     --     Item set')
    else:
        print(' Item     --     Support')
    print('---------------------------')
    for i in range(len(ls)):
        print(ls[i][0], '           ', ls[i][1])
    print()

listPrint(ls, 't')


# creating c = 
c = []                      # c = [Item, Item set]
for i in range(len(mset)):
    lp=[]
    p=0
    for j in range(2):
        if j==0:
            p = mset.pop()
            lp.append(set(p.split()))
        else:
            a=0
            for t in range(len(ls)):
                if p in ls[t][1]:
                    a+=1                    
            lp.append(a)
        
    c.append(lp)
    

#creating l1=
def createL(c):
    l1=[]                  # l1 = [Item, Item set]
    for i in range(len(c)):
        if c[i][1] >= spt :
            l1.append(c[i])
    return l1


# creating new C table func
def createC(l, a):
    c=[]
    length = len(l[0][0]) + 1
    for i in range (len(l)):
        st=l[i][0]
        for j in range(i+1, len(l)):
            s = st.union(l[j][0])
            # print(s)
            lsp=[]
            if len(s)==length:
                lsp.append(s)
                count = 0
                for p in range(len(ls)):
                    if s.issubset(ls[p][1]):
                        count+=1
                lsp.append(count)
                if i==0 and j==0:
                    c.append(lsp)
                bol=True
                for k in range(len(c)):
                    if c[k][0]==lsp[0]:
                        bol=False
                        break
                if bol:
                    c.append(lsp)
    if len(c)==0:
        return False
    
    if a==1:
        pass
    else:
        n=len(l)-1
        if len(c) == n*(n+1) / 2 :
            return  False     
        
    return c

l1=[]
l2=[]
l3=[]

# the main Apriori algo func
def Apriori(c):
    print("C1 = ")
    listPrint(c, 'l')
    
    bol = True
    i = 1
    while bol:
        l = createL(c)
        print("L"+str(i)+ "= ")
        listPrint(l, 'l')
            
        if i==1:
            c=createC(l, 1)
            global l1
            l1=l
        else:
            c=createC(l, 2)
            
        if c != False:
            print("C"+str(i+1)+ "= ")
            listPrint(c, 'l')
            global l2
            l2=l
        else:
            print("Iteration done.\n")
            bol = False
            global l3
            l3=l
        i+=1
            
Apriori(c)

def ruleMining(l1, l2, l3):
    cd=input("Enter minimum confidence in percent: ")
    cd=cd.split('%')
    cd=int(cd[0])
    print("Rule mining:\n")
    i=0
    while i<len(l3):
        lp=l3[i][0]
        j=0
        v1=-1
        v2=-1
        while j<len(l3[i][0]):
            s1=set()
            lt=l3[i][0]
            s1.add(lp.pop())
            s2=lt-s1
            st1='Ok'
            st2='Ok'
            for t in range(len(l1)):
                if l1[t][0] == s1:
                    v1=l1[t][1]
                    break
                
            for t in range(len(l2)):
                if l2[t][0] == s2:
                    v2=l2[t][1]
                    break
                
            if int(l3[i][1]/v1*100)<cd:
                st1='x'
            if int(l3[i][1]/v2*100)<cd:
                st2='x'
            print(s2,"->",s1, " Confidence = ", l3[i][1],"/",v2, " Confidence rate = ", int(l3[i][1]/v2*100), " ",st2)
            print(s1,"->",s2, " Confidence = ", l3[i][1],"/",v1, " Confidence rate = ", int(l3[i][1]/v1*100), " ",st1)
            
            lt.add(s1.pop())
            j+=1
            
        i+=1
        
ruleMining(l1, l2, l3)
