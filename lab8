import sqlite3
conn=sqlite3.connect('text.db')
c=conn.cursor()
def select():
  c.execute('''SELECT * FROM STUDENT''')
  print(c.fetchall())
  conn.commit()
  #conn.close()
def insert(idno,sname):
  c.execute("INSERT INTO STUDENT(ID,NAME) VALUES(%d,'%s')"%(idno,sname))
  conn.commit()
  #conn.close()
def delete(idno):
  c.execute("DELETE FROM STUDENT WHERE ID=%d" %(idno))
  conn.commit()
def update(idno,sname):
  c.execute('''UPDATE STUDENT SET NAME='%s' WHERE ID=%d'''%(sname,idno))
  conn.commit()
def selectid(idno):
  #print(idno)
  c.execute("SELECT * FROM STUDENT WHERE ID=%d " %(idno))
  print(c.fetchall())
  conn.commit()
while(1):
    choice=int(input("enter choice\n 1-insert\n2-delete\n3-update\n4-display\n5-display specificc student"))
    if(choice==1):
        stname=input("enter name")
        idno=int(input("enter id"))
        insert(idno,stname)
    if(choice==2):
        #tname=input("enter name")
        idno=int(input("enter id"))
        delete(idno)
    if(choice==3):
        stname=input("enter new name")
        idno=int(input("enter id"))
        update(idno,stname)
    if(choice==4):
        select()
    if(choice==5):
        #tname=input("enter name")
        idno=int(input("enter id"))
        selectid(idno)

