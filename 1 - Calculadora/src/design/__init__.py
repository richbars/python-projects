from tkinter import *
from .. colors import Colors

class richbars:
    @staticmethod
    def Calculator():
        # - Configuring the window
        window = Tk()
        window.title("Calculadora")
        window.geometry("235x310") # Pixels
        window.config(bg=Colors.BLACK)

        frame_screen = Frame(window, width=235, height=50, bg=Colors.BLUE)
        frame_screen.grid(row=0, column=0)

        frame_body = Frame(window, width=235, height=268)
        frame_body.grid(row=1, column=0)

        # Configuring the buttons

        button1 = Button(frame_body, text="C", width=11, height=2, bg=Colors.GRAY, font=('Ivy 13 bold'), relief=RAISED,
                         overrelief=RIDGE)  # Clear
        button1.place(x=0, y=0)
        button2 = Button(frame_body, text="%", width=5, height=2, bg=Colors.GRAY, font=('Ivy 13 bold'), relief=RAISED,
                         overrelief=RIDGE)  # Percentage
        button2.place(x=118, y=0)
        button3 = Button(frame_body, text="/", width=5, height=2, bg=Colors.ORANGE, fg=Colors.WHITE, font=('Ivy 13 bold'),
                         relief=RAISED, overrelief=RIDGE)  # Division
        button3.place(x=177, y=0)

        button4 = Button(frame_body, text="7", width=5, height=2, bg=Colors.GRAY, font=('Ivy 13 bold'), relief=RAISED,
                         overrelief=RIDGE)  # 7
        button4.place(x=0, y=52)
        button5 = Button(frame_body, text="8", width=5, height=2, bg=Colors.GRAY, font=('Ivy 13 bold'), relief=RAISED,
                         overrelief=RIDGE)  # 8
        button5.place(x=59, y=52)
        button6 = Button(frame_body, text="9", width=5, height=2, bg=Colors.GRAY, font=('Ivy 13 bold'), relief=RAISED,
                         overrelief=RIDGE)  # 9
        button6.place(x=118, y=52)

        button7 = Button(frame_body, text="*", width=5, height=2, bg=Colors.ORANGE, fg=Colors.WHITE, font=('Ivy 13 bold'),
                         relief=RAISED, overrelief=RIDGE)  # Multiplication
        button7.place(x=177, y=52)
        button8 = Button(frame_body, text="4", width=5, height=2, bg=Colors.GRAY, font=('Ivy 13 bold'), relief=RAISED,
                         overrelief=RIDGE)  # 4
        button8.place(x=0, y=104)
        button5 = Button(frame_body, text="5", width=5, height=2, bg=Colors.GRAY, font=('Ivy 13 bold'), relief=RAISED,
                         overrelief=RIDGE)  # 5
        button5.place(x=59, y=104)

        button6 = Button(frame_body, text="6", width=5, height=2, bg=Colors.GRAY, font=('Ivy 13 bold'), relief=RAISED,
                         overrelief=RIDGE)  # 6
        button6.place(x=118, y=104)
        button7 = Button(frame_body, text="-", width=5, height=2, bg=Colors.ORANGE, fg=Colors.WHITE, font=('Ivy 13 bold'),
                         relief=RAISED, overrelief=RIDGE)  # Subtraction
        button7.place(x=177, y=104)
        button8 = Button(frame_body, text="1", width=5, height=2, bg=Colors.GRAY, font=('Ivy 13 bold'), relief=RAISED,
                         overrelief=RIDGE)  # 1
        button8.place(x=0, y=156)

        button9 = Button(frame_body, text="2", width=5, height=2, bg=Colors.GRAY, font=('Ivy 13 bold'), relief=RAISED,
                         overrelief=RIDGE)  # 2
        button9.place(x=59, y=156)
        button9 = Button(frame_body, text="3", width=5, height=2, bg=Colors.GRAY, font=('Ivy 13 bold'), relief=RAISED,
                         overrelief=RIDGE)  # 3
        button9.place(x=118, y=156)
        button10 = Button(frame_body, text="+", width=5, height=2, bg=Colors.ORANGE, fg=Colors.WHITE, font=('Ivy 13 bold'),
                          relief=RAISED, overrelief=RIDGE)  # Addition
        button10.place(x=177, y=156)

        button11 = Button(frame_body, text="0", width=11, height=2, bg=Colors.GRAY, font=('Ivy 13 bold'), relief=RAISED,
                          overrelief=RIDGE)  # 0
        button11.place(x=0, y=208)
        button12 = Button(frame_body, text=".", width=5, height=2, bg=Colors.GRAY, font=('Ivy 13 bold'), relief=RAISED,
                          overrelief=RIDGE)  # Point
        button12.place(x=118, y=208)
        button13 = Button(frame_body, text="=", width=5, height=2, bg=Colors.ORANGE, fg=Colors.WHITE, font=('Ivy 13 bold'),
                          relief=RAISED, overrelief=RIDGE)  # Result
        button13.place(x=177, y=208)

        # Configuring label

        app_label = Label(frame_screen, text="123456789", width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT,
                          font=('Ivy 18 bold'), bg=Colors.BLUE, fg=Colors.WHITE)
        app_label.place(x=0, y=0)


        window.mainloop()

    def __init__(self):
        self.mensagem = "olá"

    def saudar(self):
        print(self.mensagem)