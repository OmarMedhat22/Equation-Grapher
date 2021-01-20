from tkinter import *
import numpy as np  
import matplotlib.pyplot as plt




LARGE_FONT= ("Verdana", 12)

root = Tk()



label = Label(root,text = 'Enter your equation here ')
label.pack()

e  = Entry(root)
e.pack()


label = Label(root,text = 'Minimum Number')
label.pack()


Minimum  = Entry(root)
Minimum.pack()


label = Label(root,text = 'Maximum Number')
label.pack()


Maxiumum  = Entry(root)
Maxiumum.pack()


def click():
    
    equation =  e.get()
    try:
        x = np.linspace(float(Minimum.get()), float(Maxiumum.get()), 100)
        key = True
    except:
        key = False
        error = 'Wrong input ranges in Maxiumum or Minimum parameters'
        label = Label(root,text = error)
        label.pack()

    if key :
        try:
            y = eval(equation)
            key_2=True
        except:

            error = 'Wrong input in equation parameters enter it again '
            key_2=False

            label = Label(root,text = error)
            label.pack()

        if  key_2: 
            fig = plt.figure(figsize = (10, 5)) 
            plt.plot(x, y) 
              
            plt.show() 
            




button_1 = Button(root,text="Ok",command=click)
button_1.pack()

root.mainloop()
