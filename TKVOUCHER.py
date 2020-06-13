
from tkinter import *

with open('voucher.txt', 'r') as info:

    voucher = info.read()

root = Tk()



root.title('TICKET VOUCHER: PAKISTAN RAILWAY RESERVATION')
root.geometry('650x650+360+10')


background_image= PhotoImage(file= 'logo.png')
background_image1= PhotoImage(file= 'logo.png')
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)



label_1 = Button(root, text='TICKET VOUCHER', bg="white",fg='green', font=('Times New Roman','25','bold'),)
label_1.pack()


label_1 = Label(root, text=voucher,fg='black', bg='white', font=('Times New Roman','18','underline'),)
label_1.pack()

label_1 = Label(root, text="TERMS AND CONDITONS: \n 1)Show this Voucher on counter for payment. \n 2) Voucher is valid for SINGLE USE only. \n 3) Travelling without payment is illegal. \n 4) NO Arms and Drugs allowed in train. \n 5) NO pets are allowed.",fg='black', bg='white', font=('Times New Roman','18','underline'),)
label_1.pack()








root.mainloop()