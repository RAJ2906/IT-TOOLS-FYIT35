from tkinter import *

#Importing every method from tkinter module.

main_window = Tk()                                                                                                                   #Making the main window.
choice_variable = IntVar()
choice_variable.set = (0)                                                                                                             #Initializing the choice, that is python.
language_list = [("Pyhton",0),("WP",1),("jQuery",2),("Javascript",3)]

def show_the_user_selected_choice():

       #Shows the choice selected by the user.

       print("You have selected :",choice_variable .get())

label1 = Label(main_window, text = "select your favorite programming language: ")          #Making the label widget
label1.pack()

for text,value in language_list:
       radio_button = Radiobutton(main_window, text = f"option{value}",                            #Making the radiobutton widget
                                  variable = choice_variable,
                                  command = show_the_user_selected_choice, value = value)
       radio_button.pack()




