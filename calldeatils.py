class callDetail:
    
    def __init__(self,cfrom,cto,dur,ctype):
        self.callfrom=cfrom
        self.callto=cto
        self.duration=dur
        self.type=ctype
    def get(self):
        print("CALL FROM:",self.callfrom,"\nCALL TO:",self.callto,"\nDURATION:",self.duration,"\nTYPE:",self.type)
    def calculate(self):
        if self.type=="STD":
            return 0
        elif self.type=="ISD":
            return 1
        elif self.type=="local":
            return 2
        
class util:
    
    def __init__(self):
        self.list_of_call_objects=[]
    def parse_customers(self,list_of_call_string):
        std=local=isd=0
        for i in list_of_call_string:
            list=i.split(",")
            self.list_of_call_objects.append(callDetail(list[0],list[1],list[2],list[3]))
        for i in self.list_of_call_objects:
            i.get()
        for i in self.list_of_call_objects:
            if(i.calculate()==0):
               std+=1
            elif(i.calculate()==1):
                isd+=1
            else:
                local+=1
        print("number of std calls",std)
        print("number of isd calls",isd)

        print("number of local calls",local)

        
list_of_call_string=[]
n=int(input("enter the number of details:"))
for i in range(n):
    call=input("enter deatils separated by commas:")
    list_of_call_string.append(call)
util().parse_customers(list_of_call_string)

        



        
