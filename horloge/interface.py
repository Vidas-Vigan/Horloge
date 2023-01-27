from tkinter import Label, Tk
import time
import winsound

# Titre et taille de la police
app_fenetre = Tk()
app_fenetre.title("Digital Clock")
app_fenetre.geometry("420x150")
app_fenetre.resizable(1, 1)

# Police de l'heure et ses couleurs
text_font = ("Boulder", 68, 'bold' )
background = "green"
foreground = "Blue"
border_width = 25

# combinaison de toutes les éléments pour définir le label de nos éléments
label = Label(app_fenetre, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)

# Définition de la fonction principale de l'horloge
def digital_clock():
    temps = time.strftime("%H:%M:%S")
    label.config(text=temps)

# Definition de l'alarme    
label.after(200, digital_clock)
app_fenetre.mainloop()
