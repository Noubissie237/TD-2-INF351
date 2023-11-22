import mysql.connector as nk

dbname = "TD2-INF351-FILM"
connexion = nk.connect(user="root", password="", host="localhost", database=dbname)
cursor = connexion.cursor()

def question1():
    print("\n\t\t\t#####################################")
    print("\t\t\t# NOMBRE DE FILM PRODUITS PAR GENRE #")
    print("\t\t\t#####################################")

    print("\n")

    req = cursor.execute("""
    SELECT GenreFilm.libelle AS Genre, 
    COUNT(Film.IdFilm) AS nbre
    FROM GenreFilm
    LEFT JOIN Film ON GenreFilm.idGenre = Film.idGenre
    GROUP BY GenreFilm.idGenre, GenreFilm.libelle
    """)

    response = cursor.fetchall()
    print("|nbre de Film |      Genre \t     |\n")
    for elt in response:
        print("|     {}      ==> \t{}".format(elt[1], elt[0]))

    print("\n......................... FIN ...........................\n")

def question2():
    print("\n\t\t\t#####################################")
    print("\t\t\t# NOMBRE DE FILM PRODUITS PAR GENRE #")
    print("\t\t\t#####################################")

    print("\n")



    cursor.close()
    connexion.close()
    print("\n......................... FIN ...........................\n")

def question3():
    print("\n\t\t\t########################################################################")
    print("\t\t\t# PERSONNES AYANT JOUÉ DANS UN FILM LORSQU'ILS AVAIENT MOINS DE 21 ANS #")
    print("\t\t\t########################################################################")

    print("\n")

    req = cursor.execute("""
    SELECT Personne.nom, YEAR(CURDATE()) - YEAR(Personne.dateNaissance) AS age,
    Film.titre AS Film
    FROM Personne
    JOIN RoleFilm ON RoleFilm.idPersonne = Personne.idPersonne
    JOIN Film ON Film.idFilm = RoleFilm.idFilm
    WHERE YEAR(CURDATE()) - YEAR(Personne.dateNaissance) < 21
    """)

    response = cursor.fetchall()
    for elt in response:
        print("|||--------''{}'' a joué dans ''{}'' lorsqu'il/lorsqu'elle avait ''{} ans''\n".format(elt[0].upper(), elt[2].upper(), elt[1]))

    print("\n......................... FIN ...........................\n")
    
def question4():
    print("\n\t\t\t#####################################")
    print("\t\t\t# NOMBRE DE FILM PRODUITS PAR GENRE #")
    print("\t\t\t#####################################")

    print("\n")


    cursor.close()
    connexion.close()
    print("\n......................... FIN ...........................\n")

def question5():
    print("\n\t\t\t#####################################")
    print("\t\t\t# NOMBRE DE FILM PRODUITS PAR GENRE #")
    print("\t\t\t#####################################")

    print("\n")


    cursor.close()
    connexion.close()
    print("\n......................... FIN ...........................\n")

def question6():
    print("\n\t\t\t#####################################")
    print("\t\t\t# NOMBRE DE FILM PRODUITS PAR GENRE #")
    print("\t\t\t#####################################")

    print("\n")


    cursor.close()
    connexion.close()
    print("\n......................... FIN ...........................\n")

def question7():
    print("\n\t\t\t#####################################")
    print("\t\t\t# NOMBRE DE FILM PRODUITS PAR GENRE #")
    print("\t\t\t#####################################")

    print("\n")


    cursor.close()
    connexion.close()
    print("\n......................... FIN ...........................\n")

def question8():
    print("\n\t\t\t#####################################")
    print("\t\t\t# NOMBRE DE FILM PRODUITS PAR GENRE #")
    print("\t\t\t#####################################")

    print("\n")


    cursor.close()
    connexion.close()
    print("\n......................... FIN ...........................\n")

def question9():
    print("\n\t\t\t#####################################")
    print("\t\t\t# NOMBRE DE FILM PRODUITS PAR GENRE #")
    print("\t\t\t#####################################")

    print("\n")


    cursor.close()
    connexion.close()
    print("\n......................... FIN ...........................\n")

def question10():
    print("\n\t\t\t#####################################")
    print("\t\t\t# NOMBRE DE FILM PRODUITS PAR GENRE #")
    print("\t\t\t#####################################")

    print("\n")


    cursor.close()
    connexion.close()
    print("\n......................... FIN ...........................\n")

def Error():
    print("Erreur : Veuillez choisir un nombre entre 1 et 10 selon l'action voulu; ou alors entrez 0 pour sortir du programme")
    cursor.close()
    connexion.close()