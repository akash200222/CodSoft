from tkinter import *
def btn_click(number):
    global bel
    bel=bel+str(number)
    data.set(bel)

def btnclean():
    global bel
    bel=" "
    data.set("")

def btneql():
    global bel
    returns=eval(bel)
    data.set(returns)
root = Tk()
root.title("MY CALCULATOR")
# size of calculator 
root.geometry("361x381+500+200")
# display viwe
bel=" "
data = StringVar()
display =  Entry(root,textvariable=data,bd=29,justify="right",bg="powder blue",font=("ariel",20))
display.grid(row=0,columnspan=4)

btn7=Button(root,text="7",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btn_click(7))
btn7.grid(row=1,column=0)
btn8=Button(root,text="8",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btn_click(8))
btn8.grid(row=1,column=1)
btn9=Button(root,text="9",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btn_click(9))
btn9.grid(row=1,column=2)
btn_div=Button(root,text="/",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btn_click('/'))
btn_div.grid(row=1,column=3)


btn4=Button(root,text="4",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btn_click(4))
btn4.grid(row=2,column=0)
btn5=Button(root,text="5",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btn_click(5))
btn5.grid(row=2,column=1)
btn6=Button(root,text="6",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btn_click(6))
btn6.grid(row=2,column=2)
btn_sub=Button(root,text="-",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btn_click('-'))
btn_sub.grid(row=2,column=3)

btn1=Button(root,text="1",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btn_click(1))
btn1.grid(row=3,column=0)
btn2=Button(root,text="2",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btn_click(2))
btn2.grid(row=3,column=1)
btn3=Button(root,text="3",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btn_click(3))
btn3.grid(row=3,column=2)
btn_mul=Button(root,text="*",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btn_click('*'))
btn_mul.grid(row=3,column=3)

btn_div=Button(root,text="/",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btn_click('/'))
btn_div.grid(row=1,column=3)
btn_c=Button(root,text="C",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=btnclean)
btn_c.grid(row=4,column=0)
btn0=Button(root,text="0",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btn_click(0))
btn0.grid(row=4,column=1)
btn_add=Button(root,text="+",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btn_click('+'))
btn_add.grid(row=4,column=2)
btn_eql=Button(root,text="=",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=btneql)
btn_eql.grid(row=4,column=3)

root.mainloop()