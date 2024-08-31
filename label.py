import tkinter as tk

def show_output():
    number = int(number_input.get())

    if number == 0 :
        output_Lable.configure(text= 'nahhh')
        return


    output =''
    for i in range(1,13):
        output += str(number) + "x" + str(i)
        output += " = " + str(number*i) + '\n'
    output_Lable.configure(text=output)


window = tk.Tk()
window.title('label')
window.minsize(width=400 , height=400)

title_label = tk.Label(master=window,text='label')
title_label.pack(pady = 25)

number_input = tk.Entry(master=window)
number_input.pack(pady=15)

ok_Button = tk.Button(
    master = window , text = 'next' ,
    command = show_output,width = 10, height = 2
)
ok_Button.pack(pady =20)

output_Lable = tk.Label(master=window)
output_Lable.pack()



window.mainloop()