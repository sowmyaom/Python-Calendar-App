from tkinter import *
import sys
import re
import calendar
from datetime import datetime
from math import ceil

def printy(current_year, current_month):
    i =0 	
    s = calendar.month(current_year, current_month)
    t=''
    ans = ''
    for i in s:
        if i!=' ':
            t+=i	
        else:
            if t=="":
                ans+=i
            else:
                try:	
                    if int(t)==today.day:
                        ans+= t
                        t=''
                    else:
                        ans+=t
                except:
                    ans+=t
                t=""
                ans+=i
                
    if t=="":
        ans+=i
    else:
        try:	
            if int(t)==today.day:
                ans+= t
                t=''
            else:
                ans+=t
        except:
            ans+=t
        t=""
        ans+=i

    return ans
        
class MyWindow:
    
    def __init__(self, win, initial_var):
        self.lbl1=Label(win, text='Enter a number')
        self.t1=Entry(bd=3)
        self.lbl1.place(x=30, y=50)
        self.t1.place(x=150, y=50)
        self.b1= Button(win, text='Calendar', command=self.cal)
        self.b2= Button(win, text='Help' , command=self.help)
        self.b1.place(x=100, y=100)
        self.b2.place(x=230, y=100)

        self.scroll_bar = Scrollbar(win) 
        self.scroll_bar.place(x=350,y=150,height= 200)  
        self.t3 = Text(win, yscrollcommand = self.scroll_bar.set ) 
         
        self.t3.place(x=50,y=150,height=200,width=300) 
        self.scroll_bar.config( command = self.t3.yview) 
        self.s_tag= ["1.0","1.0"]
        self.t3.tag_configure("hl",background="blue", foreground="yellow")

        if(initial_var == 0):
            self.cal(0)
            initial_var= "Done"
        elif(initial_var == 'h'):
            self.help()
            initial_var = "Done"
        elif(isinstance(initial_var,int)):
            self.cal(initial_var)
            initial_var = "Done"
        

    def help(self):
        self.t3.delete(1.0, END)
        info = "\n  Welcome to Python Calendar App\n"+ "\nThis app shows in the calendar, the present month and year with the day highlighted. "
        info+= "On entering a number, the app shows you the month obtained on moving from the present month by the given count.\n"
        info+= "\nSteps:\n1.Enter a number bewteen -12 to 12\n2.Press 'Calendar'\n"
        self.t3.insert(END, info)

    def cal(self,num1=None):
        self.t3.delete(1.0, END)

        if(num1 == None):
            try:
                temp = self.t1.get()
                try:
                    int(temp)
                    num1= int(temp)
                except ValueError:
                    num1 = -16
            except:
                num1=0
        if(num1<-12 or num1>12):
            info="\nNumber entered should be in between -12 and 12\n"
            self.t3.insert(INSERT, info)
        
        else:
            today = datetime.today()
            current_month = today.month
            current_year = today.year
            current_date = str(today.day)
        
            current_month = current_month+ num1
            if current_month<=0:
                current_month = 12 + current_month
                current_year = current_year-1
            if current_month>12:
                current_month = current_month-12
                current_year = current_year+1	

            calendar.setfirstweekday(calendar.SUNDAY)
            ans= printy(current_year, current_month)
            afteryr= re.search(str(current_year),ans).end()
            cr= afteryr
            st= re.search(current_date,ans[cr:]).start()
            en= re.search(current_date,ans[cr:]).end()
            while st < afteryr:
                cr=en
                st= re.search(current_date,ans[cr:]).start()
                en= re.search(current_date,ans[cr:]).end()
            st += cr
            en += cr
            
            self.s_tag[0] ="1.0+" + str(st) + "c"
            self.s_tag[1] ="1.0+" + str(en) + "c"
            self.t3.insert(END, ans)  
            self.t3.tag_add("hl", self.s_tag[0], self.s_tag[1])
            self.t3.tag_configure("hl",background="black", foreground="white")
            
args_list= sys.argv
if(len(args_list)==1):
    initial_var = 0
else:
    if(args_list[1]== "-help"):
        initial_var = 'h'
    else:
        initial_var = int(args_list[1])

window=Tk()
mywin=MyWindow(window,initial_var)
window.title('Python Calender App')
window.geometry("400x400+10+10")
window.mainloop()
