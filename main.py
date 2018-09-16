
from datetime import datetime

class Product:
    def __init__(self,_name,_c_date=None,_e_date=None):
        self.name=_name
        self.c_date=_c_date
        self.e_date=_e_date
       
    def isExpired(self,_today):
        fmt= '%d/%m/%Y'
        delta=datetime.strptime(_today,fmt)-datetime.strptime(self.e_date,fmt)
        return delta.days>0

    def __str__(self):
        return self.name +' mdf:'+ self.c_date +' exp:'+ self.e_date

class Warehouse:
    
    def __init__(self):
        self.row = []         #This represents a list of rows in a warehouse.
    
    def addRow(self):
        self.row.append([])

    def addProduct(self, r=0, product=None):
        self.row[r].append(product)

    def removeProduct(self, r):
        product=self.row[r].pop(0)
        return product

    def getRidOfTrashes(self,_date):
    
        for the_row in range (len(self.row)):
            row_temp=[]
            for the_product in range(len(self.row[the_row])):
               if not self.row[the_row][the_product].isExpired(_date): 
                   row_temp.append(self.row[the_row][the_product])
            self.row[the_row]=row_temp
                
            
    
    def summary(self):
        
        print ("------------------------------")
        for i in range (len(self.row)):
            for j in self.row[i]: 
                print (j,end='')
                print (', ',end='') if j!=self.row[i][len(self.row[i])-1] else print ('')             
        print ("------------------------------")


w=Warehouse()

w.addRow()

p1=Product("Chit","12/11/1999","1/8/2100")
w.addProduct(0,p1)

p2=Product("Chit2","12/11/2002","1/8/2200")
w.addProduct(0,p2)

p3=Product("Chit3","12/11/2005","1/8/2300")
print(p3.isExpired("12/11/2205"))
w.addProduct(0,p3)

w.summary()

w.getRidOfTrashes("12/7/2101")
w.summary()