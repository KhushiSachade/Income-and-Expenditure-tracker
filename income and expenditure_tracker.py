import numpy as np
import matplotlib.pyplot as plt
import time
from tkinter import *

root = Tk()

def getvals():

    root.destroy()    

    i=[IM1value.get(), IM2value.get(), IM3value.get()]
    e=[EM1value.get(), EM2value.get(), EM3value.get()]

    localtime = time.asctime(time.localtime(time.time()))

    with open("records.txt", "a") as f:
        f.write(f"Time: {localtime} ->Income of M1:{IM1value.get()}, Expense of M1: {EM1value.get()}, Income of M2: {IM2value.get()}, Expense of M2: {EM2value.get()}, Income of M3: {IM3value.get()}, Expense of M2: {EM3value.get()}\n ")

    # set width of bar
    barWidth = 0.25
    fig = plt.subplots(figsize =(12, 8))

    # set height of bar
    Income = i
    Expenditure = e

    # Set position of bar on X axis
    br1 = np.arange(len(Income))
    br2 = [x + barWidth for x in br1]

    # Make the plot
    plt.bar(br1, Income, color ='grey', width = barWidth,
            edgecolor ='black', label ='Income')
    plt.bar(br2, Expenditure, color ='brown', width = barWidth,
            edgecolor ='black', label ='Expenditure')

    # Adding Xticks
    plt.xlabel('Monthly status', fontweight ='bold', fontsize = 15)
    plt.ylabel('Amount', fontweight ='bold', fontsize = 15)
    plt.xticks([r + barWidth for r in range(len(Income))],
            ['m1', 'm2', 'm3'])

    plt.legend()
    plt.show()


root.geometry("644x344")
#Heading
Label(root, text="Income-Expenditure Report", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

#Text for our form
im1 = Label(root, text="Income for M1")
em1 = Label(root, text="Expense for M1")
im2 = Label(root, text="Income for M2")
em2 = Label(root, text="Expense for M2")
im3 = Label(root, text="Income for M3")
em3 = Label(root, text="Expense for M3")

#Pack text for our form
im1.grid(row=1, column=2)
em1.grid(row=2, column=2)
im2.grid(row=3, column=2)
em2.grid(row=4, column=2)
im3.grid(row=5, column=2)
em3.grid(row=6, column=2)

# Tkinter variable for storing entries
IM1value = IntVar()
EM1value = IntVar()
IM2value = IntVar()
EM2value = IntVar()
IM3value = IntVar()
EM3value = IntVar()

#Entries for our form
im1entry = Entry(root, textvariable=IM1value)
em1entry = Entry(root, textvariable=EM1value)
im2entry = Entry(root, textvariable=IM2value)
em2entry = Entry(root, textvariable=EM2value)
im3entry = Entry(root, textvariable=IM3value)
em3entry = Entry(root, textvariable=EM3value)

# Packing the Entries
im1entry.grid(row=1, column=3)
em1entry.grid(row=2, column=3)
im2entry.grid(row=3, column=3)
em2entry.grid(row=4, column=3)
im3entry.grid(row=5, column=3)
em3entry.grid(row=6, column=3)

#Button & packing it and assigning it a command
Button(text="Display Graph", command=getvals).grid(row=7, column=3)

root.mainloop()