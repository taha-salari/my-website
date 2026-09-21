from tkinter import *
#================create window================
root = Tk()
root.title('میانگین نمرات')
root.geometry('1000x700')
root.minsize(500,600)
root.maxsize(1500,800)
#===========commands=================
lb1 = Label (root , text = 'میانگین نمرات :' , fg = 'black' , font = ('Times' , 20 , 'bold'))
lb2_m = Label(root , text= 'نمره درس ریاضی : ' , fg = 'black' , font = ('Times' , 17))
lb4_o = Label(root , text = 'نمره درس علوم :' , fg = 'black' , font = ('Times' , 17))
name = Label(root , text = 'نام : ' , fg = 'black' , font = ('Times' , 17))
l_name = Label(root , text = ' نام خانوادگی :  ' , fg = 'black' , font = ('Times' , 17))
lb_c = Label(root , text = 'لطفا کادر ها را پر کنید ' , font=('Times' , 17) ,  fg = 'black')
#==================================
en1_m = Entry(root , fg = 'white' , bg= 'black' , font = ('Times' , 17))
en2_o = Entry(root , fg = 'white'  , bg = 'black' , font =('Times' , 17))
en_na = Entry(root , fg = 'white' , bg = 'black' , font =('Times' , 17))
en_lna = Entry(root , fg = 'white' , bg = 'black' , font = ('Times' , 17))
#======================================
def average():
    try : 
        math = float(en1_m.get())
        olom = float(en2_o.get())
        name = en_na.get()
        last_name = en_lna.get()

        if math == '' or olom == '' or name =='' or last_name == '':
            lb_c.config(text = 'لطفا همه ی کادر ها را پر کنید' , fg = 'red')


        elif name.isdigit() :
            lb_c.config(text = 'لطفا نام  خود را حروف وارد کنید' , fg = 'red' )

            
        elif last_name.isdigit():
            lb_c.config(text = 'لطفا نام خانوادگی خود را حروف وارد کنید' , fg = 'red' )


    
        elif math < 0 :
            lb_c.config(text = 'نمرات را بالاتر از صفر وارد کنید' , fg = 'red')


        elif olom < 0:
            lb_c.config(text = 'نمرات را بالاتر از صفر وارد کنید' , fg = 'red')


        elif math > 20 :
            lb_c.config(text = 'نمره وارد شده از 20 بیشتر است' , fg = 'red')


        elif olom > 20 :
            lb_c.config(text = 'نمره وارد شده از 20 بیشتر است' , fg = 'red')


        else :

            jam = (olom + math)
            average_obj = jam / 2
            lb_c.config(text = f'اطلاعات {en_na.get()} {en_lna.get()} با موفقیت ثبت شد' , fg = 'black')
            with open ('text.csv' , 'a' , encoding = 'utf-8') as file :
                file.write(f'----------------------------------------------\n نام : {en_na.get()} \n نام خانوادگی : {en_lna.get()} \n نمره ریاضی : {en1_m.get()} \n نمره علوم : {en2_o.get()} \n میانگین نمرات : {average_obj}')
            en1_m.delete(0 , 'end')
            en2_o.delete(0 , 'end')
            en_na.delete(0 , 'end')
            en_lna.delete(0 , 'end')
    except Exception as e :
        lb_c.config(text = 'یک مشکلی در ثبت پیش آمده است !' , font =('Times' , 17) , fg = 'red')
        print('Error',e)

#==============define========================
btn = Button(root , text = 'ثبت نمرات 💎' , fg = 'white' , bg = 'black' , font = ('Times' , 17) , command= average)
#==============place=========================
lb1.grid(row = 0 , column =0 , padx =10 , pady = 10)
name.grid(row = 1 , column = 0 , pady = 10 , padx =10)
en_na.grid(row = 1 , column = 1 , padx =10 , pady =10)
l_name.grid(row =1 , column=  2 , pady = 10 , padx =10)
en_lna.grid(row = 1 , column= 3 , pady =10 , padx =10)
lb2_m.grid(row = 2 , column= 0 , pady = 10 , padx =10)
en1_m.grid(row = 2 , column = 1 , pady = 10 , padx =10)
lb4_o.grid(row = 2 , column = 2 , pady = 10 ,  padx =10)
en2_o.grid(row = 2 , column= 3 , padx= 10 , pady= 10)
lb_c.grid(row = 3 , column= 2 , padx= 10 ,pady= 10)
btn.grid(row = 4 , column= 2 ,padx= 10 , pady= 10)
root.mainloop()