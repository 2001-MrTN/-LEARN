
from tkinter import *
import webbrowser


def open_link_youtube():
    webbrowser.open_new("https://www.youtube.com/watch?v=wxnXNcU-YBQ&list=PLjrnnc4BZaRCR5eOXSTAgKJpBl62Y7o45")

# Create the main window
windows = Tk()

#persommaliser cette fenetre
windows.title("Mon interface Arduino")
windows.geometry("720x480")     
windows.minsize(480, 360)
icon_path = r"C:\Users\hp\Downloads\logo-arduino.ico"
windows.iconbitmap(icon_path)
windows.config(background='#55B77F')

#creer un frame
frame = Frame(windows, bg='#55B77F', bd=1, relief=SUNKEN)

#Ajouter un premier texte
Label_title = Label( text="Bienvenue sur mon interface Arduino", font=("Arial", 20, "italic bold"), bg='#55B77F', fg='white')
Label_title.pack()

#Ajouter un sous titre
Label_subtitle = Label(frame, text="Cette interface nous permet de visualiser certaines donnees de capteurs ardiono", font=("Arial", 10), bg='#55B77F', fg='white')
Label_subtitle.pack()

#Ajouter un bouton
y_button = Button(frame, text="Clique ici", font=("Arial", 10, "bold"), bg='white', fg='#55B77F', command = open_link_youtube)
y_button.pack(pady=25, padx=25)


#ajouter le frame
frame.pack(side=TOP, padx=10, pady=10)

#creer une barre de menu
menu_bar = Menu(windows)
#creer un premier menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Valeurs Capteurs", command=open_link_youtube)
file_menu.add_command(label="Quitter", command=windows.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)
#configurer la fenetre pour ajouter cette menu bar
windows.config(menu=menu_bar)

#afficher
windows.mainloop()