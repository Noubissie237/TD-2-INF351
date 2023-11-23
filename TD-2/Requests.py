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
    print("\n\t\t\t######################################################################################################")
    print("\t\t\t# POUR CHAQUE GENRE ET CHAQUE ANNEE, LE NOMBRE DE FILMS PRODUITS DANS CE GENRE ET DEPUIS CETTE ANNEE #")
    print("\t\t\t######################################################################################################")

    req = cursor.execute("""
    SELECT GenreFilm.libelle, Film.annee, COUNT(*) AS nbrefilms
    FROM Film
    JOIN GenreFilm ON Film.idGenre = GenreFilm.idGenre
    WHERE Film.annee >= (SELECT MIN(annee) FROM Film)
    GROUP BY GenreFilm.libelle, Film.annee;
    """)

    resultat = cursor.fetchall()

    print("\n| nbreFilm | Année|\t Genre\n")
    for elt in resultat:
        print("|   {}  \t   | {} |\t{}".format(elt[2], elt[1], elt[0]))

    print("\n")

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
    print("\n\t\t\t##################################################")
    print("\t\t\t# FILMS N'AYANTS AUCUN ACTEUR DE MOINS DE 25 ANS #")
    print("\t\t\t##################################################")

    print("\n")

    req = cursor.execute("""
    SELECT Film.titre
    FROM Film 
    WHERE Film.idFilm NOT IN (
    SELECT DISTINCT RoleFilm.idFilm
    FROM Personne
    JOIN RoleFilm ON RoleFilm.idPersonne = Personne.idPersonne
    WHERE YEAR(CURDATE())- YEAR(Personne.dateNaissance)<25)
    """)

    resultat = cursor.fetchall()
    for elt in resultat:
        print("|---------- TITRE :\t{} ".format(elt[0]))

    print("\n......................... FIN ...........................\n")

def question5():
    print("\n\t\t\t##########################################################################")
    print("\t\t\t# GENRE DE FILM DANS LESQUELS ON RETROUVE LE MOINS DE PERSONNAGE FEMININ #")
    print("\t\t\t##########################################################################")

    print("\n")

    req = cursor.execute("""
    SELECT GenreFilm.libelle AS Genre, COUNT(DISTINCT RoleFilm.idPersonne) AS nbre
    FROM RoleFilm
    JOIN Personne ON RoleFilm.idPersonne = Personne.idPersonne
    JOIN Film ON RoleFilm.idFilm = Film.idFilm
    JOIN GenreFilm ON Film.idGenre = GenreFilm.idGenre
    WHERE Personne.sexe = 'F'
    GROUP BY GenreFilm.idGenre
    ORDER BY nbre ASC
    LIMIT 1
    """)

    resultat = cursor.fetchall()

    print("|nbre de femme |      Genre \t     |\n")
    for elt in resultat:
        print("|      {}       |      {}".format(elt[1], elt[0]))

    print("\n......................... FIN ...........................\n")

def question6():
    print("\n\t\t\t#########################################################################")
    print("\t\t\t# GENRE DE FILM DANS LESQUELS ON RETROUVE LE PLUS DE PERSONNAGE FEMININ #")
    print("\t\t\t#########################################################################")

    print("\n")

    req = cursor.execute("""
    SELECT GenreFilm.libelle AS Genre, COUNT(DISTINCT RoleFilm.idPersonne) AS nbre
    FROM RoleFilm
    JOIN Personne ON RoleFilm.idPersonne = Personne.idPersonne
    JOIN Film ON RoleFilm.idFilm = Film.idFilm
    JOIN GenreFilm ON Film.idGenre = GenreFilm.idGenre
    WHERE Personne.sexe = 'F'
    GROUP BY GenreFilm.idGenre
    ORDER BY nbre DESC
    LIMIT 3
    """)

    resultat = cursor.fetchall()

    print("|nbre de femme |      Genre \t     |\n")
    for elt in resultat:
        print("|      {}       |      {}".format(elt[1], elt[0]))

    print("\n......................... FIN ...........................\n")

def question7():
    print("\n\t\t\t#############################")
    print("\t\t\t# NOMBRE D'ACTEURS PAR FILM #")
    print("\t\t\t#############################")

    print("\n")

    req = cursor.execute("""
    SELECT Film.titre, COUNT(DISTINCT RoleFilm.idPersonne) AS nbre
    FROM Film
    JOIN RoleFilm ON Film.idFilm = RoleFilm.idFilm
    GROUP BY Film.idFilm, Film.titre
    """)

    resultat = cursor.fetchall()

    print("|nbre d'acteurs |      Titre du film \t            |\n")
    for elt in resultat:
        print("|      {}        |      {}".format(elt[1], elt[0]))

    print("\n......................... FIN ...........................\n")

def question8():
    print("\n\t\t\t##################################")
    print("\t\t\t# NOMBRE MOYEN D'ACTEUR PAR FILM #")
    print("\t\t\t##################################")

    req = cursor.execute("""
    SELECT ROUND(AVG(nbrePersonne)) AS nbreMoyenDePersonne
    FROM (
        SELECT COUNT(DISTINCT RoleFilm.idPersonne) AS nbrePersonne
        FROM Film
        JOIN RoleFilm ON Film.idFilm = RoleFilm.idFilm
        GROUP BY Film.idFilm
        ) AS subquery
    """)

    resultat = cursor.fetchall()

    print(f"\n\n**************** | Il y'an en moyenne {resultat[0][0]} acteurs par film | *******************")

    print("\n")



    print("\n......................... FIN ...........................\n")

def question9():
    print("\n\t\t\t######################################################")
    print("\t\t\t# GENRE DE FILM AYANT LE PLUS GRAND NOMBRE D'ACTEURS #")
    print("\t\t\t######################################################")

    req = cursor.execute("""
    SELECT GenreFilm.libelle AS Genre, 
    COUNT(DISTINCT RoleFilm.idPersonne) AS nbrePersonne
    FROM GenreFilm
    JOIN Film ON GenreFilm.idGenre = Film.idGenre
    JOIN RoleFilm ON Film.idFilm = RoleFilm.idFilm
    GROUP BY GenreFilm.idGenre
    ORDER BY nbrePersonne DESC
    LIMIT 2
    """)

    resultat = cursor.fetchall()

    print(f"\n\n**************** | Les films du style {resultat[0][0].upper()} et {resultat[1][0].upper()} ont le plus grand nombre d'acteurs. | *******************")

    print("\n")


    print("\n......................... FIN ...........................\n")

def question10():
    print("\n\t\t\t#############################################################################")
    print("\t\t\t# LES 05 FILMS AYANT LE MOINS D'ACTEURS FEMININS (AVEC LE NOMBRE D'ACTEURS) #")
    print("\t\t\t#############################################################################")

    req = cursor.execute("""
    SELECT Film.titre, COUNT(CASE WHEN Personne.sexe = 'F' THEN 1 END) AS nombre_personnes_feminin, COUNT(RoleFilm.idPersonne) AS nombre_total_personnes
    FROM Film
    JOIN RoleFilm ON Film.idFilm = RoleFilm.idFilm
    JOIN Personne ON RoleFilm.idPersonne = Personne.idPersonne
    GROUP BY Film.idFilm, Film.titre
    ORDER BY nombre_personnes_feminin ASC
    LIMIT 5;
    """)

    resultat = cursor.fetchall()

    print("\nnbreF \t|\t nbreT \t\t|\t titre\n")
    for elt in resultat:
        print("  {}     | \t  {}\t\t| \t{}".format(elt[1], elt[2], elt[0]))

    print("\n")


    print("\n......................... FIN ...........................\n")

def Error():
    print("\nErreur : Veuillez choisir un nombre entre 1 et 10 selon l'action voulu; ou alors entrez 0 pour sortir du programme\n")