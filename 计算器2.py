import tkinter as tk
num1=''
num2=''
result=''

def calculate():
    try:
         num1 = float(entry_num1.get())
         num2 = float(entry_num2.get())
         operator = entry_operator.get()
         if operator == '+':
            result = num1 + num2
         elif operator == '-':
            result = num1 - num2
         elif operator == '*':
            result = num1 * num2
         elif operator == '/':
            if num2 ==0:
                result = "除数不能为零！"
            else:
             result = num1 / num2
         else:
             result = "无效的运算符！"
             label_result.config(text=f"结果：{result}")
    except:
             label_result.config(text="输入有误！")



window = tk.Tk()
window.title("简单计算器")
window.geometry("300x200")

label_num1 = tk.Label(window, text="输入第一个数字：")
label_num1.pack()
entry_num1 = tk.Entry(window)
entry_num1.pack()

label_num2 = tk.Label(window, text="输入第二个数字：")
label_num2.pack()
entry_num2 = tk.Entry(window)
entry_num2.pack()

label_operator = tk.Label(window, text="输入运算符（+、-、*、/）：")
label_operator.pack()
entry_operator = tk.Entry(window)
entry_operator.pack()
label_result = tk.Label(window, text="")
label_result.pack()

button_calculate = tk.Button(window, text="计算", command=calculate())
button_calculate.pack()





window.mainloop()