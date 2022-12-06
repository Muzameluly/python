from tkinter import * 
root = Tk()
root.title("Raim")

c = Canvas(root, width=850, height=700, bg='black')
c.pack()

c.create_oval(220, 100, 620, 500, width=5, outline='gold4')


c.create_line(290, 180, 290, 350, width=5, fill='yellow')
c.create_line(290, 180, 380, 180, width=5, fill='yellow')

c.create_line(290, 255, 380, 255, width=5, fill='yellow')
c.create_line(380, 180, 380, 255, width=5, fill='yellow')
c.create_line(290, 255, 380, 350, width=5, fill='yellow')

c.create_line(420, 255, 390, 390, width=5, fill='yellow')
c.create_line(420, 255, 480, 350, width=5, fill='yellow')
c.create_line(530, 255, 480, 350, width=5, fill='yellow')
c.create_line(530, 255, 565, 390, width=5, fill='yellow')

root.mainloop()