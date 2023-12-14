-- ........................... Question 1 : Creation de la table DEPARTEMENT ........................... --
CREATE TABLE DEPARTEMENT(
    ID INTEGER(7),
    NAME VARCHAR(25)
);

-- ........................... Question 3 : Creation de la table EMPLOYEE ........................... --
CREATE TABLE EMPLOYEE(
    ID INTEGER(7),
    LAST_NAME VARCHAR(25),
    FIRST_NAME VARCHAR(25),
    DEPT_ID INTEGER(7)
);

-- ........................... Question 5 : Creation de la table EMPLOYEE2 ........................... --
CREATE TABLE EMPLOYEE2(
    EMPNO INTEGER(7),
    ENAME VARCHAR(25),
    DEPTNO INTEGER(7)
);