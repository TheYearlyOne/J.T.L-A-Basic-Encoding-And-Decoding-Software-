from tkinter import *
import pyperclip
import time
e=""
d=""
def cop():
 global com
 pyperclip.copy(com)
 print(com)
 pyperclip.paste()
def cl():
 global output
 output.destroy()
def ou():
 global e,d
 global output,com
 output=Tk()
 output.title("OutPut")
 output.geometry("500x300")
 output.config(bg="Light Blue2")
 out=Label(output,text=com,wraplength=415,bg="Light Blue2",font=("Aleo",13),fg="White")
 out.place(x=20,y=20)
 close=Button(output,text="Close",bg="Light Blue2",command=cl,font=("Aleo",13))
 close.place(x=400,y=270)
 copy=Button(output,text="Copy OutPut",bg="Light Blue",command=cop,font=("Aleo",14))
 copy.place(x=20,y=260)
def encry():
 global e,com
 x=en.get()
 if len(x)>=1:
  x=x.upper()
  e=""
  s=-1
  for g in x:
   av=ord(g)
   d=av+(30*s)
   s*=-1
   e+=str(d)+" "
  e=e.rstrip()
  pyperclip.copy(e)
  pyperclip.paste()
  print(e)
  en.delete(0,END)
  com=e
  ou()
def decry():
 global d,com
 x=de.get()
 if len(x)>=1:
  x=x.rstrip()
  x+=" "
  d=""
  inp=""
  l=[]
  s=1
  for g in x:
   if g!=" ":
    inp+=g
   else:
    l.append(int(inp))
    inp=""
  for i in l:
   o=i+(30*s)
   s*=-1
   d+=chr(o)
  pyperclip.copy(d)
  pyperclip.paste()
  de.delete(0,END)
  print(d)
  com=d
  ou()
con=Tk()
con.geometry("420x300")
con.config(bg="Light Blue2")
con.title("JTL")
jtl=Label(text="JTL",font=("Aleo",30),bg="Light Blue2",fg="White")
jtl.place(x=160,y=20)
en=Entry(width=50,bd=2)
en.place(x=10,y=120)
enb=Button(text="Enconde Msg",bd=2,command=encry,bg="Light Blue2")
enb.place(x=323,y=118)
de=Entry(width=50,bd=2)
de.place(x=10,y=200)
deb=Button(text="Decode Msg",bd=2,command=decry,bg="Light Blue2")
deb.place(x=323,y=198)
ps=Label(text="OutPut Is Always Copied To ClipBoard,Just Use Paste Shortcut",wraplength=400,bg="Light Blue2",fg="White",font=("Aleo",14))
ps.place(x=20,y=240)
con.mainloop()
