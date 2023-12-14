-- ........................... Question 2 : Remplissage de la table DEPARTEMENT ........................... --
INSERT INTO DEPARTEMENT (ID, NAME) VALUES (10, 'ACCOUNTING');
INSERT INTO DEPARTEMENT (ID, NAME) VALUES (20, 'RESEARCH');
INSERT INTO DEPARTEMENT (ID, NAME) VALUES (30, 'SALES');
INSERT INTO DEPARTEMENT (ID, NAME) VALUES (40, 'OPERATIONS');

-- ........................... Question 4 : Modification de la table EMPLOYEE pour allonger les noms de famille ........................... --
ALTER TABLE EMPLOYEE MODIFY COLUMN LAST_NAME VARCHAR(50);

-- ........................... Question 6 : Renommage des colonnes de la nouvelle table en ID, LAST_NAME, DEPT_ID ........................... --
ALTER TABLE EMPLOYEE2 CHANGE COLUMN EMPNO ID INTEGER(7);
ALTER TABLE EMPLOYEE2 CHANGE COLUMN ENAME LAST_NAME VARCHAR(25);
ALTER TABLE EMPLOYEE2 CHANGE COLUMN DEPTNO DEPT_ID INTEGER(7);

-- ........................... Question 8 : Renommage de la table EMPLOYEE2 en EMPLOYEE ........................... --
ALTER TABLE EMPLOYEE2 RENAME TO EMPLOYEE;

-- ........................... Question 9 : Ajout d'une contrainte PRIMARY KEY dans la table EMPLOYEE ........................... --
ALTER TABLE EMPLOYEE MODIFY COLUMN ID INTEGER(7) PRIMARY KEY;

-- ........................... Question 10 : Ajout d'une contrainte PRIMARY KEY dans la table DEPARTEMENT ........................... --
ALTER TABLE DEPARTEMENT MODIFY COLUMN ID INTEGER(7) PRIMARY KEY;

-- ........................... Question 11 : Ajout d'une cle étrangère dans la table EMPLOYEE ........................... --
ALTER TABLE EMPLOYEE ADD FOREIGN KEY (DEPT_ID) REFERENCES DEPARTEMENT(ID);