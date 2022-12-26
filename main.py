from tkinter import *
import tkinter as tk
import random
import mysql.connector
import sys
niveau = (0,10,50,100,500,1000,5000,10000,20000,40000,50000)
response = 0
gui = tk.Tk()
gui.geometry("500x500")
gui.title('AkiNumber!')

from tkinter import *
def retourBdd (selected_niveau):

    try:
        conn = mysql.connector.connect(host="127.0.0.1",
                                       user="root", password="",
                                       database="python")
        cursor = conn.cursor()
        requestSelect = "SELECT meilleur_score FROM meilleurscore WHERE niveau_score={index:}"
        cursor.execute(requestSelect.format(index=selected_niveau))
        rows = cursor.fetchall()
        for row in rows:
            reponse = row[0]

    except mysql.connector.errors.InterfaceError as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)
    finally:
        # On ferme la connexion
        if conn:
            conn.close()
            return reponse

response = retourBdd(1)
fenetre = Tk()

label = Label(fenetre, text=response)
label.pack()

fenetre.mainloop()

canvas = tk.Canvas(gui, width=500, height=55, bg='black')
canvas.create_text(50, 10, text= "Niveau 1: 0 à 10",fill="white",font=('Helvetica 9 bold'))
canvas.create_text(50, 20, text= "Niveau 2: 0 à 50",fill="white",font=('Helvetica 9 bold'))
canvas.create_text(53, 30, text= "Niveau 3: 0 à 100",fill="white",font=('Helvetica 9 bold'))
canvas.create_text(53, 40, text= "Niveau 4: 0 à 500",fill="white",font=('Helvetica 9 bold'))
canvas.create_text(57, 50, text= "Niveau 5: 0 à 1000",fill="white",font=('Helvetica 9 bold'))
canvas.create_text(400, 10, text= "Niveau 6: 0 à 5000",fill="white",font=('Helvetica 9 bold'))
canvas.create_text(403, 20, text= "Niveau 7: 0 à 10000",fill="white",font=('Helvetica 9 bold'))
canvas.create_text(403, 30, text= "Niveau 8: 0 à 20000",fill="white",font=('Helvetica 9 bold'))
canvas.create_text(403, 40, text= "Niveau 9: 0 à 40000",fill="white",font=('Helvetica 9 bold'))
canvas.create_text(407, 50, text= "Niveau 10: 0 à 50000",fill="white",font=('Helvetica 9 bold'))
canvas.pack(anchor=tk.NW, expand=True)
Text_Resultat = tk.StringVar()
Text_NbrCoups = tk.StringVar()
NombreDeCoups =0
def Start():
    global NombreDeCoups
    NombreDeCoups = NombreDeCoups + 1
    Nombre = int(MonNombre.get())
    if Nombre == nombreADeviner :
        Text_Resultat.set("Victoire!")
        MonNom.pack(pady=20)
        Send.pack()
    else:
        if Nombre > nombreADeviner:
            Text_Resultat.set("Chercher un nombre plus petit")

        elif Nombre < nombreADeviner:
            Text_Resultat.set("Chercher un nombre plus grand")
    Text_NbrCoups.set("Nombre de coups actuel: " + str(NombreDeCoups))

def items_selected(event):
    # get all selected indices
    selected_indices = liste.curselection()
    # get selected items
    global  selected_niveau
    selected_niveau = ",".join([liste.get(i) for i in selected_indices])
    #print(selected_niveau)
    global nombreADeviner
    nombreADeviner = random.randint(0, niveau[int(selected_niveau)])
    Text_Resultat.set(" ")
def envoieBdd(NombreDeCoups, Nom, selected_niveau):
    # connection a la base de données + modification du meilleur score si inférieur par niveau
    conn = mysql.connector.connect(host="127.0.0.1",
                                           user="root", password="",
                                           database="python")
    cursor = conn.cursor()
    request = "update meilleurscore \
                       set meilleur_score = %s, nom_score = %s  \
                       where niveau_score = %s"
    params = (NombreDeCoups, Nom, int(selected_niveau))
    cursor.execute(request, params)
    conn.commit()
       # On ferme la connexion
    if conn:
        conn.close()


# connection a la base de données + récupération du meilleur score par niveau
def retourBdd (NombreDeCoups,selected_niveau):

    try:
        conn = mysql.connector.connect(host="127.0.0.1",
                                       user="root", password="",
                                       database="python")
        cursor = conn.cursor()
        requestSelect = "SELECT meilleur_score FROM meilleurscore WHERE niveau_score={index:}"
        cursor.execute(requestSelect.format(index=selected_niveau))
        rows = cursor.fetchall()
        for row in rows:
            reponse = row[0]

    except mysql.connector.errors.InterfaceError as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)
    finally:
        # On ferme la connexion
        if conn:
            conn.close()
            return reponse







label_NbrCoups = tk.Label(gui, textvariable=Text_NbrCoups)
label_NbrCoups.pack()
MonNom = tk.Entry(gui, width=15)
MonNom.pack_forget()
Send = tk.Button(gui, height=1, width=10, text="Envoyer", command=envoieBdd)
Send.pack_forget()
label_Niveau = Label(gui, text="Selectionner le niveau")
label_Niveau.pack()
liste = Listbox(gui)
liste.insert(1, " 1")
liste.insert(2, " 2")
liste.insert(3, " 3")
liste.insert(4, " 4")
liste.insert(5, " 5")
liste.insert(6, " 6")
liste.insert(7, " 7")
liste.insert(8, " 8")
liste.insert(9, " 9")
liste.insert(10, " 10")
liste.pack()

MonNombre = tk.Entry(gui, width=15)
MonNombre.pack(pady=20)
btn = tk.Button(gui, height=1, width=10, text="Start", command=Start)
btn.pack()
label_Resultat = tk.Label(gui, textvariable=Text_Resultat)
label_Resultat.pack()
liste.bind('<<ListboxSelect>>', items_selected)

gui.mainloop()