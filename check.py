import pip
from tkinter import *
from tkinter.ttk import *

def installing():
    package1='selenium'
    package2='apscheduler'
    package3='dhooks'
    package4='pillow'
    pip.main(['install',package1])
    pip.main(['install',package2])
    pip.main(['install',package3])
    pip.main(['install',package4])

def check():
    try:
        import selenium
        import apscheduler
        import dhooks
        message_root = Tk()
        message_root.geometry("420x60")
        message_root.resizable(width=False,height=False)
        message_root.title("Wizard")
        exit_button = Button(message_root, text="Close", command=message_root.destroy)
        exit_button.pack(side="bottom") 
        final_message=Label(text="Sucessfully installed : )")
        final_message.pack()
        message_root.mainloop()   
    except ModuleNotFoundError:
        message_root = Tk()
        message_root.geometry("420x60")
        message_root.resizable(width=False,height=False)
        message_root.title("Wizard")
        exit_button = Button(message_root, text="Close", command=message_root.destroy)
        exit_button.pack(side="bottom")
        final_message=Label(text="Installation Failed : )")
        final_message.pack()
        message_root.mainloop()

installing()
check()
