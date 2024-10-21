from tkinter import *
import math 

def limpar():
    entrada.delete(0,'end')
    
def backspace():
    ultimo_num = len(entrada.get())-1
    entrada.delete(ultimo_num)

def pressionar(input):
    comprimento = len(entrada.get())
    entrada.insert(comprimento,input) #entrada.insert(indice, texto)
    
def adicao(a,b):
    return float(a)+float(b)

def subtracao(a,b):
    return float(a)-float(b)

def multiplicacao(a,b):
    return float(a)*float(b)

def divisao(a,b):
    return float(a)/float(b)

def separar_valores(simbolo,expressao):
    valores = expressao.split(simbolo,1) #duvidoso.. esclarecer dúvida
    return valores #lista de valores separados pelo símbolo

def cientifica(expressao):
    dado = separar_valores('(',expressao) #['tan','180']
    if dado[0] == 'tan':
        resultado = math.tan(float(dado[1]))
    elif dado[0] == 'cos':
        resultado = math.cos(float(dado[1]))
    elif dado[0] == 'sin':
        resultado = math.sin(float(dado[1]))
    elif dado[0] == 'log':
        resultado = math.log10(float(dado[1]))
    elif dado[0] == 'ln':
        resultado = math.log(float(dado[1])) #nao entendi
    elif dado[0] == 'deg':
        resultado = math.degrees(float(dado[1]))
    elif dado[0] == 'rad':
        resultado = math.radians(float(dado[1]))
    elif dado[0] == 'fac':
        resultado = math.factorial(float(dado[1]))
    return resultado

    

cor1 = '#FFFFFF' #branco
cor2 = '#4A4A4A' #cinza claro
cor3 = '#3b3a3a' #cinza escuro
cor4 = '#DA70D6' #rosa

janela = Tk()
janela.geometry('382x562')
janela.title('Calculadora')
janela.config(bg=cor2)
janela.resizable(False,False)

frame_cima = Label(janela,height=200)


entrada_str = StringVar() # Usada para gerenciar o valor de uma string de forma que você possa vincular essa string a um widget da interface gráfica, como uma Entry ou um Label.
entrada = Entry(janela,textvariable=entrada_str,fg=cor1,bg=cor2,font=('Arial',26,'bold'),border=0,justify=RIGHT)
entrada.grid(columnspan=4,ipady=20,pady=(30,0))

fontfamily= ('Arial',15,'bold')

btn_tan = Button(janela,text='tan',command=lambda:pressionar('tan('),fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_tan.grid(row=1,column=0,sticky=E+W,ipady=5)

btn_cos = Button(janela,text='cos',command=lambda:pressionar('cos('),fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_cos.grid(row=1,column=1,sticky=E+W,ipady=5)

btn_sin = Button(janela,text='sin',command=lambda:pressionar('sin('),fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_sin.grid(row=1,column=2,sticky=E+W,ipady=5)

btn_sqrt = Button(janela,text='sqrt',command=lambda:pressionar('sqrt('),fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_sqrt.grid(row=1,column=3,sticky=E+W,ipady=5)

btn_log = Button(janela,text='log',command=lambda:pressionar('log('),fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_log.grid(row=2,column=0,sticky=E+W,ipady=5)

btn_ln = Button(janela,text='ln',command=lambda:pressionar('ln('),fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_ln.grid(row=2,column=1,sticky=E+W,ipady=5)

btn_deg = Button(janela,text='deg',command=lambda:pressionar('deg('),fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_deg.grid(row=2,column=2,sticky=E+W,ipady=5)

btn_rad = Button(janela,text='rad',command=lambda:pressionar('rad('),fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_rad.grid(row=2,column=3,sticky=E+W,ipady=5)

btn_fac = Button(janela,text='fac',command=lambda:pressionar('fac('),fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_fac.grid(row=3,column=0,sticky=E+W,ipady=5)

btn_pow = Button(janela,text='pow',command=lambda:pressionar('pow'),fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_pow.grid(row=3,column=1,sticky=E+W,ipady=5)

btn_rem = Button(janela,text='rem',command=lambda:pressionar('rem'),fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_rem.grid(row=3,column=2,sticky=E+W,ipady=5)

btn_pi = Button(janela,text='π',command=lambda:pressionar(math.pi),fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_pi.grid(row=3,column=3,sticky=E+W,ipady=5)

btn_limpar = Button(janela,text='C',command=limpar,fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_limpar.grid(row=4,column=0,columnspan=2,sticky=E+W,ipady=5)

btn_backspace = Button(janela,text='⌫',command=backspace,fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_backspace.grid(row=4,column=2,columnspan=2,sticky=E+W,ipady=5)

btn_sete = Button(janela,text='7',command=lambda:pressionar('7'),fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_sete.grid(row=5,column=0,sticky=E+W,ipady=5)

btn_oito = Button(janela,text='8',command=lambda:pressionar('8'),fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_oito.grid(row=5,column=1,sticky=E+W,ipady=5)

btn_nove = Button(janela,text='9',command=lambda:pressionar('9'),fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_nove.grid(row=5,column=2,sticky=E+W,ipady=5)

btn_divisao = Button(janela,text='÷',command=lambda:pressionar('÷'),fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_divisao.grid(row=5,column=3,sticky=E+W,ipady=5)

btn_quatro = Button(janela,text='4',command=lambda:pressionar('4'),fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_quatro.grid(row=6,column=0,sticky=E+W,ipady=5)

btn_cinco = Button(janela,text='5',command=lambda:pressionar('5'),fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_cinco.grid(row=6,column=1,sticky=E+W,ipady=5)

btn_seis = Button(janela,text='6',command=lambda:pressionar('6'),fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_seis.grid(row=6,column=2,sticky=E+W,ipady=5)

btn_multiplicacao = Button(janela,text='×',command=lambda:pressionar('×'),fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_multiplicacao.grid(row=6,column=3,sticky=E+W,ipady=5)

btn_um = Button(janela,text='1',command=lambda:pressionar('1'),fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_um.grid(row=7,column=0,sticky=E+W,ipady=5)

btn_dois = Button(janela,text='2',command=lambda:pressionar('2'),fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_dois.grid(row=7,column=1,sticky=E+W,ipady=5)

btn_tres = Button(janela,text='3',command=lambda:pressionar('3'),fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_tres.grid(row=7,column=2,sticky=E+W,ipady=5)

btn_subtracao = Button(janela,text='–',command=lambda:pressionar('–'),fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_subtracao.grid(row=7,column=3,sticky=E+W,ipady=5)

btn_ponto = Button(janela,text='.',command=lambda:pressionar('.'),fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_ponto.grid(row=8,column=0,sticky=E+W,ipady=5)

btn_zero = Button(janela,text='0',command=lambda:pressionar('0'),fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_zero.grid(row=8,column=1,sticky=E+W,ipady=5)

btn_e = Button(janela,text='e',command=lambda:pressionar(math.e),fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_e.grid(row=8,column=2,sticky=E+W,ipady=5)

btn_adicao = Button(janela,text='+',command=lambda:pressionar('+'),fg=cor4,bg=cor3,activeforeground=cor4,activebackground=cor3,font=fontfamily,borderwidth=1,relief=SOLID)
btn_adicao.grid(row=8,column=3,sticky=E+W,ipady=5)

btn_igual = Button(janela,text='=',command='',fg=cor1,bg=cor4,activeforeground=cor1,activebackground=cor4,font=fontfamily,borderwidth=1,relief=SOLID)
btn_igual.grid(row=9,columnspan=4,sticky=E+W,ipady=5)




janela.mainloop()