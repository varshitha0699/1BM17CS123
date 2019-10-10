class bracket:
    def __init__(self,str):
        self.par=str
        self.i=0
    def validate(self):
        if len(self.par)%2==1:
            print("INVALID STRING")
            return
        else:
            for self.i in range(len(self.par)-1):
                if (self.par[self.i]=='('):
                    if (self.par[self.i+1]==')'):
                        pass
                    else:
                        print("INVALID STRING")
                        break
                elif self.par[self.i]=='{':
                    if self.par[self.i+1]=='}':
                        pass
                    else:
                        print("INVALID STRING")
                        break
                elif self.par[self.i]=='[':
                    if self.par[self.i+1]==']':
                        pass
                    else:
                        print("INVALID STRING")
                        break
                if (self.i==len(self.par)-2):
                    print("VALID")
        
      
str=input("enter the string:")
x=bracket(str)
x.validate()
            
                 
