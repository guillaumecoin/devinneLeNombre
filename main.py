import random
import mysql.connector
import sys
import tkinter

root = tkinter.Tk()

# déclaration des variables
niveau = (10, 20, 30, 40, 50)
indexNiveau = int(input("Saisissez un niveau : "))
tours = 1
response = 0
nombre = int(input("Saisissez un entier : "))
nombreADeviner = random.randint(0, niveau[indexNiveau])

# vérification des entrées
if nombre == nombreADeviner:
    print("Vous avez réussi en " + str(tours) + " tours")
else:
    while nombre != nombreADeviner:
        if nombre > nombreADeviner:
            print("trouver un nombre plus petit")
            nombre = int(input("Saisissez un entier : "))
            tours += 1
        elif nombre < nombreADeviner:
            print("trouver un nombre grand")
            nombre = int(input("Saisissez un entier : "))
            tours += 1

print("Vous avez réussi en " + str(tours) + " tours")

# connection a la base de données + récupération du meilleur score par niveau
try:
    conn = mysql.connector.connect(host="127.0.0.1",
                                   user="root", password="",
                                   database="python")
    cursor = conn.cursor()
    requestSelect = "SELECT meilleur_score FROM meilleurscore WHERE niveau_score={index:}"
    cursor.execute(requestSelect.format(index=indexNiveau))
    rows = cursor.fetchall()
    for row in rows:
        response = row[0]


except mysql.connector.errors.InterfaceError as e:
    print("Error %d: %s" % (e.args[0], e.args[1]))
    sys.exit(1)
finally:
    # On ferme la connexion
    if conn:
        conn.close()
        print(response)

# connection a la base de données + modification du meilleur score si inférieur par niveau

def recuperation(indexNiveau):
 try:
    conn = mysql.connector.connect(host="127.0.0.1",
                                   user="root", password="",
                                   database="python")
    cursor = conn.cursor()
    requestSelect = "SELECT meilleur_score FROM meilleurscore WHERE niveau_score={index:}"
    cursor.execute(requestSelect.format(index=indexNiveau))
    rows = cursor.fetchall()
    for row in rows:
        response = row[0]


 except mysql.connector.errors.InterfaceError as e:
    print("Error %d: %s" % (e.args[0], e.args[1]))
    sys.exit(1)
 finally:
    # On ferme la connexion
    if conn:
        conn.close()
        return (response)



if tours < recuperation(indexNiveau):
    nom = input("Saisissez votre prénom ")
    try:
        conn = mysql.connector.connect(host="127.0.0.1",
                                       user="root", password="",
                                       database="python")
        cursor = conn.cursor()
        request = "update meilleurscore \
           set meilleur_score = %s, nom_score = %s  \
           where niveau_score = %s"
        params = (tours,nom, indexNiveau)
        cursor.execute(request, params)
        conn.commit()
    except mysql.connector.errors.InterfaceError as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
        sys.exit(1)
    finally:
        # On ferme la connexion
        if conn:
            conn.close()

# connection a la base de données + récupération du meilleur score par niveau
try:
    conn = mysql.connector.connect(host="127.0.0.1",
                                   user="root", password="",
                                   database="python")
    cursor = conn.cursor()

    cursor.execute("SELECT niveau_score,meilleur_score FROM meilleurscore ORDER BY niveau_score ASC")
    rows = cursor.fetchall()
    for row in rows:
        print('Niveau {0} à pour score {1} '.format(row[0], row[1], ))


except mysql.connector.errors.InterfaceError as e:
    print("Error %d: %s" % (e.args[0], e.args[1]))
    sys.exit(1)
finally:
    # On ferme la connexion
    if conn:
        conn.close()
        print(response)








