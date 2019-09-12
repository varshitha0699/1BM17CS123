class student:
    def __init__(self):
        self.id=0
        self.age=0
        self.mark=0
    def set(self):
        self.id=int(input("enter id:"))
        self.age=int(input("enter age:"))
        self.mark=int(input("enter marks:"))
    def get(self):
        print("student details:\n")
        print("ID:",self.id)
        print("AGE:",self.age)
        print("MARKS:",self.mark)
    def validate_marks(self):
        if self.mark>=0 and self.mark<=100:
            return "true"
        else:
            return "false"
    def validate_age(self):
        if self.age>20:
            return "true"
        else:
            return "false"
    def check_qualification(self):
        n1=self.validate_marks()
        n2=self.validate_age()
        if(n1=="true" and n2=="true"):
            if(self.mark>=65):
                return "true"
            else:
                print("INVALID MARKS")
                return "false"
        else:
            print("INVALID MARKS OR AGE")
            return "false"
n=int(input("enter the number of students:"))
lobjects=[]
for i in range(n):
    lobjects.append(student())
for i in range(n):
    lobjects[i].set()
    l=lobjects[i].check_qualification()
    if l=="true":
        print("STUDENT IS ELIGIBLe")
        lobjects[i].get()
    else:
        print("STUDENT IS NOT ELIGIBLE")

        

