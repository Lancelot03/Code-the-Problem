import math
class diff_table:
    def __init__(self):
        self.main_List = []
        self.frst=[]
        self.snd=[]
        self.thrd=[]
        self.frth=[]
        self.lenn=input("Total number of digits:")
    def takingInputs(self):
        i=0
        while(i<int(self.lenn)):
            self.main_List.append(input("enter : "))
            print("\n")
            i=i+1
    def frstt(self):
        i=0
        ft=self.main_List
        while(i<(int(self.lenn)-1)):
           self.frst.append(float(ft[i+1])-float(ft[i]))
           i=i+1
        return self.frst
    def sndd(self):
        i=0
        ft=self.frst
        while(i<(int(self.lenn)-2)):
           self.snd.append(float(ft[i+1])-float(ft[i]))
           i=i+1
        return self.snd      
    def thrdd(self):
        i=0
        ft=self.snd
        while(i<(int(self.lenn)-3)):
           self.thrd.append(float(ft[i+1])-float(ft[i]))
           i=i+1
        return self.thrd   
    def frthh(self):
        i=0
        ft=self.thrd
        while(i<(int(self.lenn)-4)):
           self.frth.append(float(ft[i+1])-float(ft[i]))
           i=i+1
        return self.frth   
            
            
        
        


obj = diff_table()
obj.takingInputs()
print(obj.frstt())
print(obj.sndd())
print(obj.thrdd())
print(obj.frthh())
