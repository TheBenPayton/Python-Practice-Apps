import random
from tkinter import *


class Application(Frame):




    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgits()

    def create_widgits(self):


        #below begins the password text/button:

        self.welcome_statement = Label(self, text="Welcome! :)")
        self.welcome_statement.grid(row=2, column=3, columnspan=2, sticky=W)

        self.generate_button = Button(self, text="Generate!", command=self.reveal)
        self.generate_button.grid(row=2, column=0, sticky=W)

        self.text = Text(self, width=10, height=1, wrap=WORD)
        self.text.grid(row=3, column=0, columnspan=2, sticky=W)

        self.here_is_pass_statement = Label(self, text="<--Here is your password!")
        self.here_is_pass_statement.grid(row=3, column=3, columnspan=2, sticky=W)


    def reveal(self):
        a = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%*&"
        passlen = 8
        password = "".join(random.sample(a, passlen))
        print(password)
        self.text.delete(0.0, END)
        self.text.insert(0.0, password)


#root.geometry changes the frame/window size.
#keep everything behind the root.mainloop() function!!
#You can change the name of the window down below under root.title
#root.configure will change the background color of the created application.
root = Tk()
root.title("Payton's simple Password Generator")
root.geometry("350x150")
app = Application(root)
root.configure(background='blue')
root.mainloop()
