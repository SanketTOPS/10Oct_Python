import tkinter
from tkinter import ttk,messagebox

window=tkinter.Tk()
window.config(background='gold')
window.title("FirstApp")
window.geometry("400x600")

lbl_fnm=tkinter.Label(text="Firstname:",bg='gold',fg='red',font='Dubai 15 bold')
#lbl_fnm.pack()
#lbl_fnm.place(x=0,y=0)
lbl_fnm.grid(row=0,column=0,sticky='W')

lbl_lnm=tkinter.Label(text="Lastname:",bg='gold',fg='red',font='Dubai 15 bold')
#lbl_lnm.pack()
#lbl_lnm.place(x=0,y=20)
lbl_lnm.grid(row=1,column=0,sticky='W')

txt_fnm=tkinter.Entry(font='Dubai 12 bold')
txt_fnm.grid(row=0,column=1,sticky='W')

txt_lnm=tkinter.Entry(font='Dubai 12 bold')
txt_lnm.grid(row=1,column=1,sticky='W')

male=tkinter.Radiobutton(value=0,text="Male",bg='gold',fg='red',font='Dubai 15 bold')
male.grid(row=2,column=0,sticky='W')

female=tkinter.Radiobutton(value=1,text="Female",bg='gold',fg='red',font='Dubai 15 bold')
female.grid(row=2,column=1,sticky='W')

opt1=tkinter.Checkbutton(text="Python",bg='gold',fg='red',font='Dubai 15 bold')
opt1.grid(row=3,column=0,sticky='W')

opt2=tkinter.Checkbutton(text="PHP",bg='gold',fg='red',font='Dubai 15 bold')
opt2.grid(row=4,column=0,sticky='W')

opt3=tkinter.Checkbutton(text="JAVA",bg='gold',fg='red',font='Dubai 15 bold')
opt3.grid(row=5,column=0,sticky='W')

opt4=tkinter.Checkbutton(text="HTML",bg='gold',fg='red',font='Dubai 15 bold')
opt4.grid(row=6,column=0,sticky='W')

city=['Ahmedabad','Rajkot','Baroda','Surat','Jamnagar','Bhavnagar']
citycombo=ttk.Combobox(values=city)
citycombo.grid(row=7,column=0,sticky='W')

def btnclick():
    #print("Button Clicked!")
    fnm=txt_fnm.get()
    lnm=txt_lnm.get()
    print("Firstname:",fnm)
    print("Lastname:",lnm)


    #messagebox.showerror("Error","Something went wrong...try again!")
    #messagebox.showinfo("Success","Your data has been saved!")
    messagebox.showwarning("Warning","Your disk is full!")


btn=tkinter.Button(text="Submit",font='Dubai 15 bold',command=btnclick)
#btn.grid(row=9,column=0)
btn.place(x=170,y=380)

window.mainloop()
