-- ........................... Question 2 : Insertion de la premiere ligne de données dans la table MY_EMPLOYEE ........................... --
INSERT INTO MY_EMPLOYEE VALUES (1, 'Patel', 'Ralph', 'Rpatel', 795);

-- ........................... Question 3 : Insertion de la deuxieme ligne de données dans la table MY_EMPLOYEE ........................... --
INSERT INTO MY_EMPLOYEE (ID, LAST_NAME, FIRST_NAME, USERID, SALARY) VALUES (2, 'Dancs', 'Betty', 'Bdancs', 860);
INSERT INTO MY_EMPLOYEE (ID, LAST_NAME, FIRST_NAME, USERID, SALARY) VALUES (3, 'Biri', 'Ben', 'Bbiri', 1100);
INSERT INTO MY_EMPLOYEE (ID, LAST_NAME, FIRST_NAME, USERID, SALARY) VALUES (4, 'Newman', 'Chad', 'Cnewman', 750);

-- ........................... Question 4 : Remplacement du nom de l'employé 3 par Drexler ........................... --
UPDATE MY_EMPLOYEE SET LAST_NAME='Drexler' WHERE ID=3;

-- ........................... Question 5 : Attribution d'un salaire de 1000 à tous les employés ayant un salaire inférieur à 900 ........................... --
UPDATE MY_EMPLOYEE SET SALARY=1000 WHERE SALARY<900;

-- ........................... Question 6 : Suppression de Betty Dancs de la table ........................... --
DELETE FROM MY_EMPLOYEE WHERE LAST_NAME='Dancs' AND FIRST_NAME='Betty';

-- ........................... Question 7 : Vidons entièrement la table ........................... --
TRUNCATE TABLE MY_EMPLOYEE;