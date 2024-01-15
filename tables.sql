CREATE TABLE Immeubles (
    nomImm VARCHAR(50) NOT NULL PRIMARY KEY,
    adresse VARCHAR(100),
    nbEtages INTEGER,
    anneeConstruction INT(4),
    nomGerant VARCHAR(100)
);

CREATE TABLE Appartements (
    nomImm VARCHAR(50),
    noApp INTEGER NOT NULL PRIMARY KEY,
    superficie INTEGER,
    nbEtages INTEGER,
    etage INTEGER,
    FOREIGN KEY (nomImm) REFERENCES Immeubles(nomImm)
);

CREATE TABLE Personnes (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(20),
    age INTEGER,
    profession VARCHAR(50)
);

CREATE TABLE Occupants (
    nomImm VARCHAR(50),
    noApp INTEGER,
    nomOcc INT,
    anneeArrivee INTEGER,
    FOREIGN KEY (nomImm) REFERENCES Immeubles(nomImm),
    FOREIGN KEY (noApp) REFERENCES Appartements(noApp),
    FOREIGN KEY (nomOcc) REFERENCES Personnes(id),
    PRIMARY KEY (nomImm, noApp, nomOcc)
);