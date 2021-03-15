from tkinter import *
from functions import *


def replace_with_path(): 
	e.delete












# Window settings
root = Tk()
root.geometry("640x480")
root.resizable(0, 0)

# Creating a input widget
e = Entry(root, width=50)
e.insert(0, 'Enter the path of the file:')


# Buttons
zip_Button = Button(text="Zip", command=lambda: zip())
unzip_Button = Button(text="Unzip", command=lambda: unzip())
search_Button = Button(text='Search', command=lambda: find_files())

# Placing widgets to the screen
e.grid(row=0, column=1, padx=20, pady=10, columnspan=2)
zip_Button.grid(row=1, column=1)
unzip_Button.grid(row=1, column=2)
search_Button.grid(row=0, column=4)




# Mainloop
root.mainloop()





