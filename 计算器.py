import tkinter as tk
window=tk.Tk()
window.title("计算器")
text=tk.Entry(window,width=50,font=("Arial",20))
text.pack(side='top',pady=10 )
result=0.0
operator=""
num=""
num1=""
num2=""


def add_num(num):
    global operator
    global num1
    global result
    global num2



    if operator=="":
        num1+=str(num)
        text.insert(tk.END,num)
    else:
        num2+=str(num)
        text.insert(tk.END,num)
btn1 = tk.Button(window, text="1", width=5, height=2, command=lambda: add_num(1))
btn1.pack(side='left')
btn2 = tk.Button(window, text="2", width=5, height=2, command=lambda: add_num(2))
btn2.pack(side='left')
btn3 = tk.Button(window, text="3", width=5, height=2, command=lambda: add_num(3))
btn3.pack(side='left')
btn4 = tk.Button(window, text="4", width=5, height=2, command=lambda: add_num(4))
btn4.pack(side='left')
btn5 = tk.Button(window, text="5", width=5, height=2, command=lambda: add_num(5))
btn5.pack(side='left')
btn6 = tk.Button(window, text="6", width=5, height=2, command=lambda: add_num('6'))
btn6.pack(side='left')
btn7 = tk.Button(window, text="7", width=5, height=2, command=lambda: add_num('7'))
btn7.pack(side='left')
btn8 = tk.Button(window, text="8", width=5, height=2, command=lambda: add_num('8'))
btn8.pack(side='left')
btn9 = tk.Button(window, text="9", width=5, height=2, command=lambda: add_num('9'))
btn9.pack(side='left')
btn0 = tk.Button(window, text="0", width=5, height=2, command=lambda: add_num('0'))
btn0.pack(side='left')


def add_operator(op):
    global operator
    global num1
    global result
    global num2
    global num
    if num1=="":
        num1=num
        operator=op
        num=""
    else:
        num2=num
    if operator=="+":
       result+=float(num1)+float(num2)
    elif operator=="-":
            result-=float(num1)-float(num2)
    elif operator=="*":
            result*=float(num1)*float(num2)
    elif operator=="/":
            result/=float(num1)/float(num2)
    text.delete(0,tk.END)
    text.insert(tk.END,str(result))
    num1=str(result)
    num2=""
    operator=op
    num=""
btnadd=tk.Button(window,text="+",width=5,height=2, command=lambda:add_operator("+"))
btnadd.pack(side=tk.LEFT,padx=10,pady=10)
btnsub=tk.Button(window,text="-",width=5,height=2, command=lambda:add_operator("-"))
btnsub.pack(side=tk.LEFT,padx=10,pady=10)
btnmul=tk.Button(window,text="*",width=5,height=2, command=lambda:add_operator("*"))
btnmul.pack(side=tk.LEFT,padx=10,pady=10)
btndiv=tk.Button(window,text="/",width=5,height=2, command=lambda:add_operator("/"))
btndiv.pack(side=tk.LEFT,padx=10,pady=10)

def clear():
    global result
    global num1
    global num2
    global num
    global operator
    num=""
    num1=""
    num2=""
    operator=""
    result=0.0
    text.delete(0,tk.END)
btnclear=tk.Button(window,text="clear",width=5,height=2, command=clear)
btnclear.pack(side=tk.LEFT,padx=10,pady=10)
btnequal=tk.Button(window,text="=",width=5,height=2, command=lambda:add_operator)
btnequal.pack(side=tk.LEFT,padx=10,pady=10)

window.mainloop()



