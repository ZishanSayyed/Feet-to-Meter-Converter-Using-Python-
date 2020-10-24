from tkinter import Tk,Button,Label,DoubleVar,Entry   #DoubleVar is a data type in this case its a boolean

window=Tk()
window.title("Feet to Meter Converter App")
window.configure(background="sky blue")
window.geometry("320x220")
window.resizable(width=False,height=False)

def convert():
    value=float(ft_entry.get())   # value get enter
    meter=value*0.3048            #value converted
    met_value.set("%4f" % meter) # value displayed upto 4 decimal point


def clear():
    ft_value.set("")
    met_value.set("")

ft_lbl=Label(window,text="Feet",bg="black",fg="white",width=14) #fg is for ground property
ft_lbl.grid(column=0,row=0,padx=15,pady=15)   #the lable tab be at 0 column and 0 row posstion pad use for spaceing form x and y

ft_value=DoubleVar()  # Value which be in window is boolean
ft_entry=Entry(window,textvariable=ft_value,width=14)
ft_entry.grid(column=1,row=0)
ft_entry.delete(0,"end") #we get empty window every time we open the app

met_lbl=Label(window,text="Meter",bg="black",fg="white",width=14)
met_lbl.grid(column=0,row=1,padx=15,pady=15)

met_value=DoubleVar()  # Value which be in window is boolean
met_entry=Entry(window,textvariable=met_value,width=14)
met_entry.grid(column=1,row=1)
met_entry.delete(0,"end")

convert_btn=Button(window,text="Convert",bg="black",fg="white",width=14,command=convert)
convert_btn.grid(column=0,row=3,padx=15)


clear_btn=Button(window,text="Clear",bg="black",fg="white",width=14,command=clear)
clear_btn.grid(column=1,row=3,padx=15)



window.mainloop()  #run App
