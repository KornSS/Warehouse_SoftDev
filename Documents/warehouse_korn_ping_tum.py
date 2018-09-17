import random
class WarehouseManage():
    def FactoryMethod(self):
        self.A = Warehouse('A')
        self.B = Warehouse('B')
        self.C = Warehouse('C')
        self.D = Warehouse('D')
        self.E = Warehouse('E')

        self.belt = beltCreator()

    def __init__(self):
        self.FactoryMethod()    
    
    def summary(self):
        self.A.summary()
        self.B.summary()
        self.C.summary()
        self.D.summary()
        self.E.summary()
        print("")

    def hash(self,_cmd):
        '''x=chr((ord(_cmd[0])-ord('A'))%5+ord('A'))
        y=int(_cmd[1])
        z=int(_cmd[2:])''' #this is an ordinary straight forward hash function

        if ord(_cmd[0]) in range(ord('A'),ord('U')):
            z=int( str( int(_cmd[1])-1 ) + _cmd[2:4] )%400
            return 'E',ord(_cmd[0])-ord('A'),z

        elif ord(_cmd[0]) in range(ord('U'),ord('Z')):
            return chr(((ord(_cmd[0])-ord('U'))%3)+ord('A')),int(_cmd[1])-1,int(_cmd[2:4])
        else:
            print("Wrong input!")
            return -1
        #return x,y,z

    def hash2(self,_cmd):
        return 'D',int(_cmd[1:4])%7,ord(_cmd[0])-ord('A')

    def links(self,wh,dir):
        link_next={'A':'','B':'A','C':'A','D':'B,A','E':'B,A'}
        if(dir=='FWD'):
            print("Moving from Start to A")
            prev='A'
            if wh=='A': return True
            self.next=link_next[wh]
            for i in range(len(self.next)-2,-1,-1):
                if self.next[i]!=',':
                    print("Moving from "+prev+" to "+self.next[i])
                    prev=self.next[i]
            print("Moving from "+prev+" to "+wh)
            return True
        else:
            prev=wh
            self.next=link_next[wh]
            for i in range(len(self.next)):
                if self.next[i]!=',':
                    print("Moving from "+prev+" to "+self.next[i])
                    prev=self.next[i]
            print("Moving from A to Start")
            return True
    def retrieve(self,_cmd):

        if _cmd in self.move_temp:
            if self.move_temp[_cmd]=='-1':
                print("Slot is empty. Cannot retrieve the product.")
                return -1
            hx=self.hash(self.move_temp[_cmd])
        else:
            hx=self.hash(_cmd)
        #print("self."+hx[0]+".retrieve"+"("+_cmd +","+str(hx[1])+","+str(hx[2])+")")
        if(eval("self."+hx[0]+".retrieve"+"(\'"+_cmd +"\',"+str(hx[1])+","+str(hx[2])+")")==-1):

            print("Slot is empty. Cannot retrieve the product.")
            return -1
        elif(eval("self."+hx[0]+".retrieve"+"(\'"+_cmd +"\',"+str(hx[1])+","+str(hx[2])+")")==1):
            hx=self.hash2(_cmd)
            print("Retrieve by rehash...")

        print("Start to retrieve")
        self.links(hx[0],'FWD')
        print("Retriving a product id "+_cmd+" in warehouse "+str(ord(hx[0])-ord('A')+1)+": "+"row "+str(hx[1])+" slot "+str(hx[2]))
        self.links(hx[0],'BKD')
        print("Placing product id "+_cmd+" on the belt")
        self.belt.store(_cmd)
        print("Retrieving successfully!")

    def store(self,_cmd):
        if(_cmd in self.belt.element):
            print("Product is already on the belt")
            return -2
        if(_cmd in self.move_temp):
            print("Product has already added")
            return -3
        hx=self.hash(_cmd)
        st=eval("self."+hx[0]+".store"+"(\'"+_cmd+"\',"+str(hx[1])+','+str(hx[2])+")")
        #print(eval("self."+hx[0]+".store"+"(\'"+_cmd+"\',"+str(hx[1])+','+str(hx[2])+")"))
        if(st==-1):
            hx=self.hash2(_cmd)
            st=eval("self."+hx[0]+".store"+"(\'"+_cmd+"\',"+str(hx[1])+','+str(hx[2])+")")
            if(st==-1):
                print("Slot is occupied")
                return -1
            elif(st==1):
                    print("Product has already added")
                    return -3

        elif(st==1):
                print("Product has already added")
                return -3
        self.links(hx[0],'FWD')
        print("Storing a product id "+_cmd+" in warehouse "+str(ord(hx[0])-ord('A')+1)+": "+"row "+str(hx[1])+" slot "+str(hx[2]))
        self.links(hx[0],'BKD')
        print("Storing successfully!")
        
    def check(self,a):
        list0159 = [range(48, 58), range(65, 90), range(49, 54), range(48, 58), range(48, 58), range(65, 90), range(49, 54), range(48, 58), range(48, 58)]
        #list2 = [range(50, 51), range(49, 54), range(48,51), range(49, 54), range(48, 49), range(48, 49)]
        if(len(a) in [5,6,9]):
            if(a[0] in "0159"):
                if a[0] == '9' and len(a)!=9: return False
                for i in range(len(a)):
                    if(ord(a[i]) not in list0159[i]):
                        return False
                return True
            elif(a[0] in "2"):
                print("I'm currently checking in 2...")
                for i in range(len(a)):
                    if ord(a[1]) in range(ord('1'),ord('3')+1):
                        if ord(a[2]) not in range(ord('0'),ord('0')+1): return False
                        if ord(a[3]) not in range(ord('1'),ord('5')+1): return False
                        print("Passed 1...")
                    elif ord(a[1]) in range(ord('4'),ord('4')+1):
                        if ord(a[2]) not in range(ord('0'),ord('0')+1): return False
                        if ord(a[3]) not in range(ord('1'),ord('7')+1): return False
                        print("Passed 2...")
                    elif ord(a[1]) in range(ord('5'),ord('5')+1):
                        if ord(a[2]) not in range(ord('0'),ord('2')+1): return False
                        if ord(a[3]) not in range(ord('1'),ord('9')+1): return False 
                        if a[2] == '2' and a[3]!=0: return False
                        print("Passed 3...")
                    else: return False
                    #if (ord(a[i]) not in list2[i]):
                    #    return False
                return True
            elif(a[0] in "34"):
                if(a[1:] == "0000"):
                    return True
                return False
            else:
                return False
        return False
    
    move_temp={"A999":"B999"}
    def m_store(self,id,pos):
        hx=self.hash(id)
        if id in self.move_temp:
            if self.move_temp[id]=='-1':
                print("Cannot found the product with ID: "+id)
                return -1
            else:
                #print("id"+id)
                pos2=self.move_temp[id]
                #print("pos2"+pos2)
                del self.move_temp[pos2]
                hx=self.hash(pos2)
                eval("self."+hx[0]+".retrieve"+"(\'"+id+"\',"+str(hx[1])+","+str(hx[2])+")")
                #print("pos"+pos)
                self.move_temp[id]=pos
                hx=self.hash(pos)
                eval("self."+hx[0]+".store"+"(\'"+id+"\',"+str(hx[1])+','+str(hx[2])+")")
                #print("movetempid:"+self.move_temp[id])
                self.move_temp[pos]='-1'
                hx=self.hash(pos)
                eval("self."+hx[0]+".store"+"(\'"+"-1"+"\',"+str(hx[1])+','+str(hx[2])+")")
                #print("movetemppos:"+self.move_temp[pos])
                print("Move product "+id+" to "+pos)
                return 1
        if(eval("self."+hx[0]+".retrieve"+"(\'"+id+"\',"+str(hx[1])+","+str(hx[2])+")")==-1):
            print("Product id "+id+" not found")
            return -1
        hx=self.hash(pos)
        if(eval("self."+hx[0]+".store"+"(\'"+id+"\',"+str(hx[1])+','+str(hx[2])+")")==-1):
            print("Slot is occupied. Failed to move.")
            hx=self.hash(id)
            eval("self."+hx[0]+".store"+"(\'"+id+"\',"+str(hx[1])+','+str(hx[2])+")")
            return -1
        print("Move product "+id+" to "+pos)
        self.move_temp[id]=pos
        self.move_temp[pos]='-1'
        #print(self.move_temp)
    def m_move(self,id,pos):
        hx=self.hash(id)
        if id in self.move_temp:
            if self.move_temp[id]=='-1':
                print("Cannot found the product with ID: "+id)
                return -1
            else:
                #print("id"+id)
                pos2=self.move_temp[id]
                #print("pos2"+pos2)
                del self.move_temp[pos2]
                hx=self.hash(pos2)
                eval("self."+hx[0]+".retrieve"+"(\'"+id+"\',"+str(hx[1])+","+str(hx[2])+")")
                #print("pos"+pos)
                self.move_temp[id]=pos
                hx=self.hash(pos)
                eval("self."+hx[0]+".store"+"(\'"+id+"\',"+str(hx[1])+','+str(hx[2])+")")
                #print("movetempid:"+self.move_temp[id])
                self.move_temp[pos]='-1'
                hx=self.hash(pos)
                eval("self."+hx[0]+".store"+"(\'"+"-1"+"\',"+str(hx[1])+','+str(hx[2])+")")
                #print("movetemppos:"+self.move_temp[pos])
                print("Move product "+id+" to "+pos)
                return 1
        if(eval("self."+hx[0]+".retrieve"+"(\'"+id+"\',"+str(hx[1])+","+str(hx[2])+")")==-1):
            print("Product id "+id+" not found")
            return -1
        if(eval("self."+chr(ord('A')+int(pos[0])-1)+".store"+"(\'"+id+"\',"+str(int(pos[1:2]))+','+str(int(pos[3:]))+")")==-1):
            print("Slot is occupied. Failed to move.")#--------------------- i'm here
            return -1
        print("Move product "+id+" to "+pos)
        self.move_temp[id]=pos
        self.move_temp[pos]='-1'
        #print(self.move_temp)
    def sort(self,x,y):
        dup_product=[]
        for i in eval("self."+chr(ord(x)-ord('1')+ord('A'))+".row["+str(int(y)-1)+"]"):
            #print("1"+i)
            if i in self.move_temp:
                #print("2"+i)
                if(self.store(i)==-1):
                    dup_product.append(i)
                pos=self.move_temp[i]
                hx=self.hash(pos)
                del self.move_temp[i]

                del self.move_temp[pos]
                eval("self."+hx[0]+".retrieve"+"(\'"+i+"\',"+str(hx[1])+","+str(hx[2])+")")
                self.store(i)          
                
        print("Sorting process for warehouse "+str(int(x))+" is complete")
    def fill(self,i_fill_str):
        i_fill=int(i_fill_str)
        ocp=0
        i=0
        while(i < i_fill):
            product_type = chr(random.randint(ord('A'),ord('Y')))
            row = str(random.randint(1,5))
            slot1 = str(random.randint(0,9))
            slot2 = str(random.randint(0,9))
            print("1"+product_type+row+slot1+slot2)
            print("fill "+str(i+1)+" products")
            print("slot is occupied: "+str(ocp))
            store_st=self.store(product_type+row+slot1+slot2)
            if(store_st==-3): i+=0
            elif(store_st==-1): 
                ocp+=1
                
            else: i+=1
            '''if wh in range(1,4): row = random.randint(1,6)
            if wh in range(4,5): row = random.randint(1,8)
            if wh in range(5,6): row = random.randint(1,21)'''
            
    def search(self,_cmd):
        if _cmd in self.move_temp:
            if self.move_temp[_cmd]=='-1':
                print("Product not found")
                return -1
            hx=self.hash(self.move_temp[_cmd])
        else:
            hx=self.hash(_cmd)
        if(eval("self."+hx[0]+".search"+"("+str(hx[1])+","+str(hx[2])+")")==False):
            print("Product not found")
            return -1
        else: print("Found product at "+hx[0]+str(hx[1])+str(hx[2]))
    def command(self,_cmd):
        _cmd=_cmd.upper()
        print(_cmd[0])
        if _cmd[0]=='-':
            print("It's coming...")
            print(_cmd[1:6])
            if _cmd[1:6]=='FILL ':
                self.fill(_cmd[6:])
                return 1
            print("1-6 didn't work")

        if self.check(_cmd)==False:
            print("Wrong input \nDumb people!!! Didn't you read the intructions huh???")
            return -1
        print("input is right")
        #if (int(_cmd[2])>5 or int(_cmd[2])==0) :
        #    print("Wrong input!4")
        #    return -1
        
        fn=int(_cmd[0])
        if fn==0: self.retrieve(_cmd[1:5])
        elif fn==1: self.store(_cmd[1:5])
        elif fn==2: self.sort(_cmd[1],_cmd[2:4])
        elif fn==3: self.belt.retrieve()
        elif fn==4: self.summary()
        elif fn==5: self.search(_cmd[1:5])
        elif fn==6: print(self.move_temp)
        elif fn==9: self.m_move(_cmd[1:5],_cmd[5:])
        else:
            print("Wrong input!")
            return -1

        #self.A.store('A125',1,25)
        
class Warehouse():

    def __init__(self,name):

        #print(self.row)
        self.name=name
        self.number_of_product=0
        if(name=='A'or 'B' or 'C'):
            self.row=['']*5
            for row_index in range(len(self.row)):
                slot=[""]*100
                self.row[row_index]=slot
        if(name=='D'):
            self.row=['']*7
            for row_index in range(len(self.row)):
                slot=[""]*25
                self.row[row_index]=slot
        elif(name=='E'):
            self.row=['']*20
            for row_index in range(len(self.row)):
                slot=[""]*400
                self.row[row_index]=slot

    def summary(self):
        print("Warehouse "+str(ord(self.name)-ord('A')+1))
        print("Number of Rows: "+str(len(self.row)))
        print("Number of total product: "+str(self.number_of_product))
        for row_index in range(len(self.row)):
            print("Product in row "+str(row_index+1)+": ",end='')
            printed=0
            temp=''
            #print(self.row[row_index])
            for slot_index in range(len(self.row[row_index])):
                if(self.row[row_index][slot_index]!=''):
                    printed=1
                    if slot_index!=len(self.row[row_index]): temp=temp+self.row[row_index][slot_index]+','
            len_temp=len(temp)
            if len_temp>0:
                if(temp[len(temp)-1]==','):
                    temp=temp[:len(temp)-1]
                print(temp,end='')
            #print(temp,end='')    
            if(printed==0):print("-",end=" ")
            print("")
        print("")
        
    def store(self,product,row_index,slot_index):

        if self.row[row_index][slot_index]=="":
            self.row[row_index][slot_index]=product
            self.number_of_product+=1
        elif  self.row[row_index][slot_index]==product:
            return 1
            
        else: return -1
    def retrieve(self,id,row_index,slot_index):
        if self.row[row_index][slot_index]=="": return -1
        elif self.row[row_index][slot_index]!=id: return 1
        else: 
            self.row[row_index][slot_index]=""
            self.number_of_product-=1
    def search(self,row_index,slot_index):
        if self.row[row_index][slot_index]=="": return False


class beltCreator():
    element=[]
    def store(self,product):
        if(len(self.element)>=10):
            print("Belt is full. Cannot retrieve the product.")
        self.element.append(product)
        #print(belt.element)
        return True
    def retrieve(self):
        if len(self.element)==0:
            print("The belt is empty")
            return False
        pop_element=self.element.pop(0)
        if pop_element in WarehouseManage.move_temp:
            del WarehouseManage.move_temp[pop_element]
        print("Retrieve a product with id "+pop_element+" from the belt")
        print("The belt now have "+str(len(self.element))+" products on the line")


obj = WarehouseManage()

while(1):
    x=input("Please type a command...")
    obj.command(x)
    print("")
