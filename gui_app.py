from csv import DictWriter
import os
import tkinter
from tkinter import messagebox as m_box
from tkinter import ttk



# win = tkinter.Tk()
# # win.iconbitmap(r'D:\python program\projects\data\Photo_Files\GUIAPPlogo.jpg')
# win.title("First GUI APP")

# # creating labels

# name_label = ttk.Label(win, text='Enter your Name ')
# name_label.grid(row=0, column=0, sticky=tkinter.W)


# email_label = ttk.Label(win, text="Enter your Email ")
# email_label.grid(row=1, column=0, sticky=tkinter.W)

# age_label = ttk.Label(win, text="Enter your Age ")
# age_label.grid(row=2, column=0, sticky=tkinter.W)

# gender_label = ttk.Label(win, text="Select your Gender ")
# gender_label.grid(row=3, column=0,sticky=tkinter.W)

# # entery box

# name_var = tkinter.StringVar()
# name_entery = ttk.Entry(win, width=20, textvariable=name_var)
# name_entery.focus()
# name_entery.grid(row=0, column=1)

# email_var = tkinter.StringVar()
# email_entery = ttk.Entry(win, width=20, textvariable=email_var)
# email_entery.grid(row=1, column=1)
# name_entery.delete(0,tkinter.END)

# age_var = tkinter.IntVar()
# age_entery = ttk.Entry(win, width=20, textvariable=age_var)
# age_entery.grid(row=2, column=1)


# # create combobox

# gender_var = tkinter.StringVar()
# gender_combo_box = ttk.Combobox(win, width=17, textvariable=gender_var, state='readonly')
# gender_combo_box['values'] = ('Select your gender','Male', 'Female', 'Other')
# gender_combo_box.current(0)
# gender_combo_box.grid(row=3, column=1)

# # create radio_button

# radio_var = tkinter.StringVar()
# radio_btn1 = ttk.Radiobutton(win, text='Student',value='Student',variable = radio_var)
# radio_btn1.grid(row=4,column=0)

# radio_btn2 = ttk.Radiobutton(win, text = 'Teacher', value='Teacher' ,variable= radio_var)
# radio_btn2.grid(row=4,column=1)

# # create check_button

# check_btn_var = tkinter.IntVar()
# check_btn = tkinter.Checkbutton(win,text="Don't show again",variable = check_btn_var)
# check_btn.grid(row=5,column=0)

# # Getting vaules

# def action():
#     name = name_var.get()
#     email = email_var.get()
#     age = age_var.get()
#     gender = gender_var.get()
#     profesion = radio_var.get() 
#     if check_btn_var.get()==1:
#         filling = " Yes"
#     else:
#         filling = "No"

#     print(f"Hello\nMr.{name} your age is {age}\nand email id is {email}\nGender is {gender}")
#     print(f"You are {profesion} of B.TECH {filling} you fill the form")

#     # with open(r"D:\python program\projects\new folder.txt",'a') as wf:
#     #     wf.write(f"Hello\nMr.{name} your age is {age}\nand email id is {email}\nGender is {gender}\nYou are {profesion} of B.TECH {filling} you fill the form")

#     name_entery.delete(0,tkinter.END)
#     email_entery.delete(0,tkinter.END)
#     name_entery.delete(0,tkinter.END)


# # create submit button

# submit_button = tkinter.Button(win,text='submit', command=action)
# submit_button.grid(row=6,columnspan=3)


# win.mainloop()


# ************************************************self_test***********************************************

window = tkinter.Tk()
window.title("Detail form ")
# window.iconbitmap(r'D:\python program\projects\data\logo_app.jpg')

head = tkinter.Label(window, text=("Pease fill the Form "))
head.grid(row=0,column=1)

name_label = ttk.Label(window, text="Enter your name ",)
name_label.grid(row=1 , column=0, sticky=tkinter.W)

name_var = tkinter.StringVar()
name_entry = tkinter.Entry(window,width=25,textvariable=name_var )
name_entry.focus()
name_entry.grid(row=1 , column=1)

number_label = tkinter.Label(window, text="Enter your mobile number ")
number_label.grid(row=2 , column=0, sticky=tkinter.W)
number_var = tkinter.StringVar()

number_entry = tkinter.Entry(window,width=25,textvariable=number_var)
number_entry.grid(row=2 , column=1)

adhress_label = tkinter.Label(window, text="Enter your Adhress ")
adhress_label.grid(row=3 , column=0, sticky=tkinter.W)
adhress_var = tkinter.StringVar()
adhress_entry = tkinter.Entry(window,width=25,textvariable=adhress_var)
adhress_entry.grid(row=3 , column=1)


# gender 

gender_label = tkinter.Label(window, text="Select your gender")
gender_label.grid(row=4,column=0,sticky=tkinter.W)

gender_var = tkinter.StringVar()

male = ttk.Radiobutton(window,width=20, value='Male' , text='Male' , variable=gender_label)
male.grid(row=4,column=1,sticky=tkinter.W)

female = ttk.Radiobutton(window, value='Female' , text='Female',variable=gender_label)
female.grid(row=4,column=2,sticky=tkinter.W)

other = ttk.Radiobutton(window, value='Other' , text='Other',variable=gender_label)
other.grid(row=5,column=1,sticky=tkinter.W)

# combobox 

qualification_var = tkinter.StringVar()

qualification_label = tkinter.Label(window, text="Select your Qualification ")
qualification_label.grid(row=6 , column=0 , sticky=tkinter.W)

qualification_entry = ttk.Combobox(window, width=20, textvariable=qualification_var , state='readonly')
qualification_entry['values'] =('MBA','B.TECH','BCA')
# qualification_entry.current(0)
qualification_entry.grid(row=6 , column=1)

notification_var = tkinter.IntVar()
notification = tkinter.Checkbutton(window, text="Don't show again ", variable= notification_var)
notification.grid(row=7, column=0 , sticky=tkinter.W)


# getting values 

def getting():
    name = name_var.get()
    number = number_var.get()
    adhress = adhress_var.get()
    gender = gender_var.get()
    qualification = qualification_var.get()
    print(name,number,gender,qualification,adhress)

    name_entry.delete(0, tkinter.END)
    adhress_entry.delete(0, tkinter.END)
    number_entry.delete(0, tkinter.END)

    if notification_var.get()==1:
        head.configure(text="You fill the form completly.\nThank You!!!")
    else:
        head.configure(text="Please fill the completly form Again")
    
    with  open(r"D:\python program\projects\data.csv",'a',newline="") as wf:
        write_data = DictWriter(wf,fieldnames=['Sname','Snumber','Sadhress','Sgender','Squalification'])
        if os.stat(r"D:\python program\projects\data.csv").st_size==0:
            write_data.writeheader()
        write_data.writerow(
            {
                'Sname'             : name,
                'Snumber'           : number,
                'Sadhress'          : adhress,
                'Sgender'           : gender,
                'Squalification'    : qualification
            }
        )
    m_box.showinfo('title','thank you ')


btn = tkinter.Button(window,width=16, text='Submit', command=getting)
btn.grid(row=8,column=1)

window.mainloop()