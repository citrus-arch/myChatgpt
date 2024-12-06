from tkinter import *

first_number = second_number = operator = None #initialize 

def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text = new)

def clear():
    result_label.config(text='') #config used to dynamically change/update any attribute 

def get_operator(op):
    global first_number, operator
    first_number= int(result_label['text']) #stoblue first number in first_number
    operator = op #+-*/
    result_label.config(text='') #cleablue display 

def get_result():
    global first_number, second_number, operator
    second_number= int(result_label['text'])

    if operator=='+':
        result_label.config(text=str(first_number+second_number))
    elif operator=='-':
        result_label.config(text=str(first_number-second_number))
    elif operator=='*':
        result_label.config(text=str(first_number*second_number))
    else:
        result_label.config(text=str(round(first_number/second_number,2)))





root= Tk()
root.title('Calculator')
root.geometry('280x380')
root.resizable(0,0) #0 movement in x and y direction. fixed size 
root.configure(background='black')

result_label= Label(root, text='', bg='black', fg='white') #fg= font colour. label used to make static texts like title
result_label.grid(row=0,column=0,columnspan=5, pady=(50,25), sticky='w') #r=0, c=0 is to place the text top left corner. pady=borders 
result_label.config(font=('verdana',30, 'bold'))

#row 1. 7,8,9,+
btn7= Button(root, text= '7', bg= 'blue', fg= 'white', width=5, height=2, command= lambda :get_digit(7) ) #command to link a function with button
btn7.grid(row=1, column=0)
btn7.config(font=('verdana',14))

btn8= Button(root, text= '8', bg= 'blue', fg= 'white', width=5, height=2, command= lambda :get_digit(8))
btn8.grid(row=1, column=1)
btn8.config(font=('verdana',14))

btn9= Button(root, text= '9', bg= 'blue', fg= 'white', width=5, height=2, command= lambda :get_digit(9))
btn9.grid(row=1, column=2)
btn9.config(font=('verdana',14))

btn_add= Button(root, text= '+', bg= 'blue', fg= 'white', width=5, height=2, command= lambda :get_operator('+'))
btn_add.grid(row=1, column=3)
btn_add.config(font=('verdana',14))

#row 2. 4,5,6,-
btn4= Button(root, text= '4', bg= 'blue', fg= 'white', width=5, height=2, command= lambda :get_digit(4))
btn4.grid(row=2, column=0)
btn4.config(font=('verdana',14))

btn5= Button(root, text= '5', bg= 'blue', fg= 'white', width=5, height=2, command= lambda :get_digit(5))
btn5.grid(row=2, column=1)
btn5.config(font=('verdana',14))

btn6= Button(root, text= '6', bg= 'blue', fg= 'white', width=5, height=2,command= lambda :get_digit(6))
btn6.grid(row=2, column=2)
btn6.config(font=('verdana',14))

btn_sub= Button(root, text= '-', bg= 'blue', fg= 'white', width=5, height=2,command= lambda :get_operator('-'))
btn_sub.grid(row=2, column=3)
btn_sub.config(font=('verdana',14))

#row 3. 1,2,3,*
btn1= Button(root, text= '1', bg= 'blue', fg= 'white', width=5, height=2,command= lambda :get_digit(1))
btn1.grid(row=3, column=0)
btn1.config(font=('verdana',14))

btn2= Button(root, text= '2', bg= 'blue', fg= 'white', width=5, height=2,command= lambda :get_digit(2))
btn2.grid(row=3, column=1)
btn2.config(font=('verdana',14))

btn3= Button(root, text= '3', bg= 'blue', fg= 'white', width=5, height=2,command= lambda :get_digit(3))
btn3.grid(row=3, column=2)
btn3.config(font=('verdana',14))

btn_mul= Button(root, text= '*', bg= 'blue', fg= 'white', width=5, height=2,command= lambda :get_operator('*'))
btn_mul.grid(row=3, column=3)
btn_mul.config(font=('verdana',14))

#row 4. c,0,=,/
btnc= Button(root, text= 'C', bg= 'blue', fg= 'white', width=5, height=2,command= lambda :clear())
btnc.grid(row=4, column=0)
btnc.config(font=('verdana',14))

btn0= Button(root, text= '0', bg= 'blue', fg= 'white', width=5, height=2,command= lambda :get_digit(0))
btn0.grid(row=4, column=1)
btn0.config(font=('verdana',14))

btne= Button(root, text= '=', bg= 'blue', fg= 'white', width=5, height=2,command= lambda :get_result())
btne.grid(row=4, column=2)
btne.config(font=('verdana',14))

btn_div= Button(root, text= '/', bg= 'blue', fg= 'white', width=5, height=2,command= lambda :get_operator('/'))
btn_div.grid(row=4, column=3)
btn_div.config(font=('verdana',14))







root.mainloop()



