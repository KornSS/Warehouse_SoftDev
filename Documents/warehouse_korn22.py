class WarehouseManage():

    def __init__(self):
        self.A = Warehouse('A')
        self.B = Warehouse('B')
        self.C = Warehouse('C')

        self.D = Warehouse('D')

        self.E = Warehouse('E')

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
        z=int(_cmd[2:])'''

        if ord(_cmd[0]) in range(ord('A'),ord('U')):
            z=int( str( int(_cmd[1])-1 ) + _cmd[2:4] )%400
            return 'E',ord(_cmd[0])-ord('A'),z

        elif ord(_cmd[0]) in range(ord('U'),ord('Z')):
            return chr(((ord(_cmd[0])-ord('U'))%3)+ord('A')),int(_cmd[1])-1,int(_cmd[2:4])
        else:
            print("Wrong input!")
            return -1
        #return x,y,z


        #hx1 if warehouse E not fulll
        #hx2 if warehouse E is full store in warehouse A-C
        #hx3 if wh A-C is full store in D
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
            print("Retreive by rehash...")

        print("Start to retreive")
        self.links(hx[0],'FWD')
        print("Retriving a product id "+_cmd+" in warehouse "+hx[0]+": "+"row "+str(hx[1])+" slot "+str(hx[2]))
        self.links(hx[0],'BKD')
        print("Placing product id "+_cmd+" on the belt")
        belt.store(_cmd)
        print("Retrieving successfully!")
    def store(self,_cmd):
        if(_cmd in belt.element):
            print("Product is already on the belt")
            return -1
        if(_cmd in self.move_temp):
            print("Product has already added")
            return -1
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
                    return -1

        elif(st==1):
                print("Product has already added")
                return -1
        self.links(hx[0],'FWD')
        print("Storing a product id "+_cmd+" in warehouse "+hx[0]+": "+"row "+str(hx[1])+" slot "+str(hx[2]))
        self.links(hx[0],'BKD')
        print("Storing successfully!")
        #for i in range()

    def sort(self,x,y):
        print("Sorting process for warehouse "+x+" is complete")
    move_temp={"A999":"B999"}
    def m_store(self,id,pos):
        hx=self.hash(id)
        if(eval("self."+hx[0]+".retrieve"+"("+str(hx[1])+","+str(hx[2])+")")==-1):
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
    def search(self,_cmd):
        if _cmd in self.move_temp:
            if self.move_temp[_cmd]=='-1':
                print("Product not found")
                return -1
            hx=self.hash(self.move_temp[_cmd])
        else:
            hx=self.hash(_cmd)
        if(eval("self."+hx[0]+".search"+"("+str(hx[1])+","+str(hx[2])+")")==-1):
            print("Product not found")
            return -1
        else: print("Found product at "+hx[0]+str(hx[1])+str(hx[2]))
    def command(self,_cmd):
        if (len(_cmd)!=5 and _cmd[0]!='9'):
            print("Wrong input!")
            return -1
        if not(ord(_cmd[1]) in range(ord('A'),ord('Z'))):
            print("Wrong input!")
            return -1
        if int(_cmd[2])>5 or int(_cmd[2])==0:
            print("Wrong input!")
            return -1
        fn=int(_cmd[0])
        if fn==0: self.retrieve(_cmd[1:5])
        elif fn==1: self.store(_cmd[1:5])
        elif fn==2: self.sort(_cmd[1],_cmd[2])
        elif fn==3: belt.retrieve()
        elif fn==4: self.summary()
        elif fn==5: self.search(_cmd[1:5])
        elif fn==6: print(self.move_temp)
        elif fn==9: self.m_store(_cmd[1:5],_cmd[5:9])

        #self.A.store('A125',1,25)
class Warehouse():

    def __init__(self,name):

        #print(self.row)
        self.name=name
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

        self.robot=False
        #print(self.row)
    def robotIn(self):
        return self.robot



    def summary(self):
        print("Warehouse "+self.name)
        print("Number of Rows: "+str(len(self.row)))
        total_p=0
        for row_index in  range(len(self.row)):
            for slot_index in range(len(self.row[row_index])):
                if(self.row[row_index][slot_index]!=''):total_p+=1
        print("Number of total product: "+str(total_p))
        for row_index in range(len(self.row)):
            print("Product in row "+str(row_index+1)+": ",end='')
            printed=0
            for slot_index in range(len(self.row[row_index])):
                if(self.row[row_index][slot_index]!=''):
                    printed=1
                    print(self.row[row_index][slot_index]+" ",end= ',' if slot_index!=len(self.row[row_index]) else '')
            if(printed==0):print("-",end=" ")
            print("")
        print("")
    def store(self,product,row_index,slot_index):

        if self.row[row_index][slot_index]=="":
            self.row[row_index][slot_index]=product
        elif  self.row[row_index][slot_index]==product:
            return 1
            #print("stored")
        else: return -1
    def retrieve(self,id,row_index,slot_index):
        if self.row[row_index][slot_index]=="": return -1
        elif self.row[row_index][slot_index]!=id: return 1
        else: self.row[row_index][slot_index]=""
    def search(self,row_index,slot_index):
        if self.row[row_index][slot_index]=="": return -1

# Create object using factory.
obj = WarehouseManage()

class belt():
    element=[]
    @staticmethod
    def store(product):
        if(len(belt.element)>=10):
            print("Belt is full. Cannot retrieve the product.")
        belt.element.append(product)
        #print(belt.element)
        return 1
    def retrieve():
        if len(belt.element)==0:
            print("The belt is empty")
            return -1
        pop_element=belt.element.pop(0)
        if pop_element in WarehouseManage.move_temp:
            del WarehouseManage.move_temp[pop_element]
        print("Retrieve a product with id "+pop_element+" from the belt")
        print("The belt now have "+str(len(belt.element))+" products on the line")

while(1):
    x=input("Please type a command...")
    obj.command(x)
    print("")
#obj.store('A125','A',1,25)
#obj.summary()
