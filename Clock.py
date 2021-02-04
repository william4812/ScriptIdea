from datetime import *

try:
    #Python 3
    import tkinter as tk
except ImportError:

    #Python 2
    import Tkinter as tk

from tkinter import *


if __name__ == "__main__":

    root = Tk();
    root.title('Clock')


    def time():

        #print('*\n')
        string = datetime.today();
        lbl.config(text = string.strftime("%Y/%m/%d %H:%M:%S"));
        lbl.after(1000, time) #call time() after 1000 ms

    lbl = Label(root)

    lbl.pack(anchor = 'center');
    time();

    root.mainloop()
