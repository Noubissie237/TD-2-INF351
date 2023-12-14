-- ........................... Question 1 : Creation de la table MY_EMPLOYEE ........................... --
CREATE TABLE MY_EMPLOYEE(
    ID INTEGER(4) NOT NULL PRIMARY KEY,
    LAST_NAME VARCHAR(25),
    FIRST_NAME VARCHAR(25),
    USERID VARCHAR(8),
    SALARY INTEGER(9.2)
)