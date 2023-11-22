import mysql.connector, json, Requests
#Connexion à la base de données
dbname = "TD2-INF351-FILM"
connexion = mysql.connector.connect(user="root", password="", host="localhost", database=dbname)
cursor = connexion.cursor()

def automaticFilling():

    with open('data.json', 'r') as myData:
        data = json.load(myData)
        
    for elt in data['GenreFilm']:
        pushData = "INSERT INTO GenreFilm (libelle) VALUES (%s)"
        bib = (elt['libelle'],)
        cursor.execute(pushData, bib)
        connexion.commit()

    for elt in data['Personne']:
        pushData = "INSERT INTO Personne (nom, dateNaissance, bio, sexe) VALUES (%s, %s, %s, %s)"
        bib = (elt['nom'], elt['dateNaissance'], elt['bio'], elt['sexe'])
        cursor.execute(pushData, bib)
        connexion.commit()

    for elt in data['Film']:
        pushData = "INSERT INTO Film (titre, annee, description, idGenre) VALUES (%s, %s, %s, %s)"
        bib = (elt['titre'], elt['annee'], elt['description'], elt['idGenre'])
        cursor.execute(pushData, bib)
        connexion.commit()

    return True

def prog():
    choix = -1
    while(choix != 0): 
        print("Quelle requête souhaitez vous effectuer ?\n")
        print("\t0. Quitter le programme")
        print("\t1. Nombre de films produits par genre")
        print("\t2. Pour chaque genre et chaque années, nombre de films produits dans ce genre et depuis cette année")
        print("\t3. Personnes ayant joué dans un film lorsqu'il avait moins de 21 ans")
        print("\t4. Films qui n'ont aucun acteur de moins de 25 ans")
        print("\t5. Le genre de film dans lequel on retrouve le moins de personnage féminin")
        print("\t6. Le film qui a le plus grand nombre de personnage féminin")
        print("\t7. Le nombre d'acteurs par film")
        print("\t8. Le nombre moyen d'acteurs par film")
        print("\t9. Le genre de film ayant le plus grand nombre d'acteurs")
        print("\t10. Les 05 films ayant le moins d'acteurs féminins (avec le nombre d'acteurs)")

        try:
            choix = int(input("Choix de requête : "))
            if(choix == 0):
                print("Fin du programme ...")
            elif(choix == 1):
                Requests.question1()
            elif(choix == 2):
                Requests.question2()
            elif(choix == 3):
                Requests.question3()
            elif(choix == 4):
                Requests.question4()
            elif(choix == 5):
                Requests.question5()
            elif(choix == 6):
                Requests.question6()
            elif(choix == 7):
                Requests.question7()
            elif(choix == 8):
                Requests.question8()
            elif(choix == 9):
                Requests.question9()
            elif(choix == 10):
                Requests.question10()
            else:
                Requests.Error()
        
        except:
            print("\n### Valeur invalide, veuillez entrer un entier ### \n")

def main():

    #Requêtes de test, pour verifier les tables sont déjà crées dans la BD
    GenreFilmCheck = "SELECT * FROM GenreFilm WHERE idGenre"

    try: #Testons si les requêtes fonctionnent
        cursor.execute(GenreFilmCheck)

    except: #Si les requêtes ne fonctionnent pas, alors les tables n'existent pas. On les crées nous même

        # ---------- CREATION DES TABLES ---------- #
        create_GenreFilm = """
        CREATE TABLE GenreFilm(
        idGenre INT AUTO_INCREMENT PRIMARY KEY,
        libelle VARCHAR(20) NOT NULL
        )
        """

        create_Personne = """
        CREATE TABLE Personne(
        idPersonne INT AUTO_INCREMENT PRIMARY KEY,
        nom VARCHAR(50) NOT NULL,
        dateNaissance DATE NOT NULL,
        bio VARCHAR(250) NULL,
        sexe CHAR(1) NOT NULL CHECK(sexe IN ('M', 'F'))
        )
        """

        create_Film = """
        CREATE TABLE Film(
        idFilm INT AUTO_INCREMENT,
        titre VARCHAR(100) NOT NULL,
        annee YEAR NOT NULL,
        description VARCHAR(100) NULL,
        idGenre INT NOT NULL,
        FOREIGN KEY(idGenre) REFERENCES GenreFilm(idGenre),
        PRIMARY KEY(idFilm, idGenre)
        )
        """

        create_RoleFilm = """
        CREATE TABLE RoleFilm(
        idFilm INT NOT NULL,
        idPersonne INT NOT NULL,
        FOREIGN KEY(idFilm) REFERENCES Film(idFilm),
        FOREIGN KEY(idPersonne) REFERENCES Personne(idPersonne),
        personnage VARCHAR(250) NULL,
        PRIMARY KEY(idFilm, idPersonne)
        )
        """

        cursor.execute(create_GenreFilm)
        cursor.execute(create_Personne)
        cursor.execute(create_Film)
        cursor.execute(create_RoleFilm)
        connexion.commit()

        print("........................................................................................................................................")
        print(". Les tables ont nouvellement été créées, souhaitez vous les remplir automatiquement via le fichier data, ou les remplir manuellement? .".upper())
        print("........................................................................................................................................")

        print("\t1.Remplir automatiquement (Conseillé !)")
        print("\t2.Remplir manuellement")
        try:
            choix = int(input("\nChoix : "))
            
            if(choix == 1):
                if(automaticFilling()):
                    print("\n ---------- Remplissage effectué avec succes ! ----------\n")
                else:
                    print("Une erreur est survenue !")
                    return
            elif(choix == 2):
                print(f"Bien noté, veuillez vous rendre à l'adresse http://127.0.0.1/phpmyadmin/ et remplissez la base de donnée <<<{dbname}>>> manuellement, puis relancez le programme")
                print("À très bientôt...")
                connexion.commit()
                cursor.close()
                return
            else:
                print("Erreur: Vous avez entré une mauvaise valeur\nFin du programme...")
                connexion.commit()
                cursor.close()
                return

        except:
            print("Erreur, le nombre attendu est un entier")
            connexion.commit()
            cursor.close()
            return

    prog()

main()