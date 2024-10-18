from tkinter import *
import math 

cor1 = '#FFFFFF' #branco
cor2 = '#4A4A4A' #cinza claro
cor3 = '#3b3a3a' #cinza escuro
cor4 = '#DA70D6' #rosa

janela = Tk()
janela.geometry('382x600')
janela.title('Calculadora')
janela.config(bg=cor3)
janela.resizable(False,False)

entrada_str = StringVar() # Usada para gerenciar o valor de uma string de forma que você possa vincular essa string a um widget da interface gráfica, como uma Entry ou um Label.
entrada = Entry(janela,textvariable=entrada_str,fg=cor1,bg=cor2,font=('Arial',26,'bold'),border=0)
entrada.grid(columnspan=4,ipady=20)

fontfamily= ('Arial',15,'bold')

btn_tan = Button(janela,text='tang',fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_tan.grid(row=1,column=0,sticky=E+W,ipady=5)

btn_cos = Button(janela,text='cos',fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_cos.grid(row=1,column=1,sticky=E+W,ipady=5)

btn_sin = Button(janela,text='sin',fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_sin.grid(row=1,column=2,sticky=E+W,ipady=5)

btn_sqrt = Button(janela,text='sqrt',fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_sqrt.grid(row=1,column=3,sticky=E+W,ipady=5)

btn_log = Button(janela,text='log',fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_log.grid(row=2,column=0,sticky=E+W,ipady=5)

btn_ln = Button(janela,text='ln',fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_ln.grid(row=2,column=1,sticky=E+W,ipady=5)

btn_deg = Button(janela,text='deg',fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_deg.grid(row=2,column=2,sticky=E+W,ipady=5)

btn_rad = Button(janela,text='rad',fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_rad.grid(row=2,column=3,sticky=E+W,ipady=5)

btn_fac = Button(janela,text='fac',fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_fac.grid(row=3,column=0,sticky=E+W,ipady=5)

btn_pow = Button(janela,text='pow',fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_pow.grid(row=3,column=1,sticky=E+W,ipady=5)

btn_rem = Button(janela,text='rem',fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_rem.grid(row=3,column=2,sticky=E+W,ipady=5)

btn_pi = Button(janela,text='pi',fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_pi.grid(row=3,column=3,sticky=E+W,ipady=5)




janela.mainloop()