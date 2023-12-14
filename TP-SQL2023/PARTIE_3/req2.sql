-- ........................... Question 3 : Requête pour afficher le nom, poste, ... , matricule de chaque employé ........................... --
SELECT EMPNO, ENAME, JOB, HIREDATE
FROM EMP;

-- ........................... Question 4 : Requête pour afficher le nom et le job, les deux séparés par une virgule et un espace ........................... --
SELECT CONCAT(ENAME, ', ', JOB) AS 'Employee and Title'
FROM EMP;

-- ........................... Question 5 : Requête pour afficher les donnees de la table EMP en une seule colonne ........................... --
SELECT CONCAT(EMPNO, ',', ENAME, ',', JOB, ',', MGR, ',', HIREDATE, ',', SAL, ',', COMM, ',', DEPTNO) AS THE_OUTPUT
FROM EMP;

-- ........................... Question 6 : Requête pour afficher le nom et le numero de departement de l'employé ayant le matricule 7566 ........................... --
SELECT ENAME, DEPTNO
FROM EMP
WHERE EMPNO=7566;

-- ............. Question 7 : Requête pour afficher le nom et le salaire de tous les employés dont le salaire n'est pas compris entre $1500 et $2850 ............. --
SELECT ENAME, SAL
FROM EMP
WHERE SAL NOT BETWEEN 1500 AND 2850;

-- ....... Question 8 : Requête pour afficher le nom, le poste et la date d'entrée (hiredate) des employés embauchés entre le 20 février 1981 et le 1 mai 1981 ....... --
SELECT ENAME, JOB, HIREDATE
FROM EMP
WHERE HIREDATE BETWEEN '1981-02-20' AND '1981-05-01'
ORDER BY HIREDATE ASC;

-- Question 9 : Requête pour afficher le numéro de département et les noms de tous les employés des départements 10 et 30 classés par ordre alphabétique des noms --
SELECT DEPTNO, ENAME
FROM EMP
WHERE DEPTNO=10 OR DEPTNO=30
ORDER BY ENAME ASC;

-- ... Question 10 : Requête pour afficher la liste des noms et salaires des employés gagnant plus de $1500 et travaillant dans le département 10 ou 30 ... --
SELECT ENAME AS Employee, SAL AS 'Monthly Salary'
FROM EMP
WHERE SAL>1500 AND (DEPTNO=30 OR DEPTNO=30);

-- ... Question 11 : Requête pour afficher le nom et le poste de tous les employés n'ayant pas de manager ... --
SELECT ENAME, JOB 
FROM EMP
WHERE MGR IS NULL;

-- ... Question 12 : Requête pour afficher le nom, le salaire et la commission de tous les employés qui perçoivent des commissions ... --
SELECT ENAME, SAL, COMM
FROM EMP
WHERE COMM IS NOT NULL AND COMM>0
ORDER BY SAL + COMM DESC;

-- ... Question 13 : Requête pour afficher le nom de tous les employés dont la troisième lettre du nom est un A ... --
SELECT ENAME
FROM EMP
WHERE SUBSTRING(ENAME, 3, 1) = 'A';

-- Question 14 : Requête pour afficher le nom de tous les employés dont le nom contient deux L et travaillant dans le département 30 ou dont le manager est 7782 --
SELECT ENAME
FROM EMP
WHERE ENAME LIKE '%L%' AND (DEPTNO=30 OR MGR=7782);

-- Question 15 : Requête pour afficher le nom, le poste et le salaire de tous les ' CLERK' ou 'ANALYST' dont le salaire est différent de $1000, $3000 ou $5000 --
SELECT ENAME, JOB, SAL
FROM EMP
WHERE (JOB='CLERK' OR JOB='ANALYST' ) AND (SAL<>1000  AND SAL<>3000 AND SAL<>5000);

-- Question 16 : Requête pour afficher le nom, le salaire et la commission de tous les employés dont le montant de commission est de plus de 10% supérieur au salaire --
SELECT ENAME, SAL, COMM 
FROM EMP
WHERE COMM > ((SAL*10)/100);

-- Question 17 : Requête pour afficher le matricule, le nom en minuscules concaténé à son poste, la longueur du nom, le salaire et le salaire augmenté de 15%--
SELECT EMPNO AS 'MATRICULE', CONCAT(LOWER(ENAME), ',', JOB) AS 'NAME AND JOB', LENGTH(ENAME) AS 'NAME LENGTH', SAL, ROUND(SAL * 1.15) AS 'New Salary'
FROM EMP
WHERE 1;

-- Question 18 : Requête pour modifiez notre requête en ajoutant une colonne dans laquelle l'ancien salaire est soustrait du nouveau salaire--
SELECT EMPNO AS 'MATRICULE', CONCAT(LOWER(ENAME), ',', JOB) AS 'NAME AND JOB', LENGTH(ENAME) AS 'NAME LENGTH', SAL, ROUND(SAL * 1.15) AS 'New Salary', ROUND(SAL * 1.15)-SAL AS 'Increase'
FROM EMP
WHERE 1;

-- Question 19 : Requête pour afficher les données concernant les employés dont le nom se termine par un N--
SELECT * 
FROM EMP
WHERE SUBSTRING(ENAME, LENGTH(ENAME), 1)='N';

-- Question 20 : Requête pour afficher le nom et la date d'embauche de chaque employé ainsi que la date de révision du salaire qui sera le premier lundi tombant après 6 mois d'activité--
SELECT ENAME, HIREDATE, DATE_FORMAT(DATE_ADD(DATE_ADD(HIREDATE, INTERVAL 6 MONTH), INTERVAL (8-DAYOFWEEK(DATE_ADD(HIREDATE, INTERVAL 6 MONTH))) % 7 DAY), '%W, the %D of %M, %Y') AS REVIEW
FROM EMP
WHERE 1;

-- Question 21 : Requête pour afficher les informations suivantes pour chaque employé : <employee name> earns <salary> monthly but wants <3 times salary>--
SELECT CONCAT(ENAME, ' earns ', SAL, ' monthly but wants ', SAL*3) AS 'Dream Salaries'
FROM EMP
WHERE 1;

-- Question 22 : Requête pour afficher le nom, la date d'embauche ainsi que le jour de la semaine où l'employé à débuté --
SELECT ENAME, HIREDATE, DAYNAME(HIREDATE) AS DAY
FROM EMP
WHERE 1;

-- Question 23 : Requête pour afficher le nom et le montant de la commission de chaque employé --
SELECT ENAME, COALESCE(COMM, 'No Commission') AS COMM
FROM EMP
WHERE 1;

-- Question 24 : Requête pour afficher le salaire maximum, le salaire minimum, la somme des salaires et le salaire moyen de tous les employés --
SELECT MAX(SAL) AS Maximum, MIN(SAL) AS Minimum, SUM(SAL) AS Sum, AVG(SAL) AS Average
FROM EMP
WHERE 1;

-- Question 25 : Requête pour afficher le nombre de personnes qui occupent le même poste--
SELECT JOB, COUNT(*) AS number_of_person
FROM EMP
GROUP BY JOB;

-- Question 26 : Requête pour afficher le nombre de managers sans en donner la liste--
SELECT COUNT(*) AS 'Number of Managers'
FROM EMP;

-- Question 27 : Requête pour afficher la différence existant entre le salaire maximum et le salaire minimum--
SELECT MAX(SAL) - MIN(SAL) AS DIFFERENCE
FROM EMP;

-- Question 28 : Requête pour afficher le matricule des différents managers et le niveau de salaire le plus bas de leurs employés--
SELECT MGR, SAL
FROM EMP
WHERE (MGR IS NOT NULL) AND (SAL>1000)
ORDER BY SAL ASC;

-- Question 29 : Requête pour afficher le numéro du département, le nombre d'employés et le salaire moyen pour tous les employés de ce département--
SELECT DEPTNO AS 'Number of dept', COUNT(*) AS 'Number of People', ROUND(AVG(SAL)) AS 'Salary'
FROM EMP
GROUP BY DEPTNO;

-- Question 30 : Requête pour afficher le nombre total d'employés puis, parmi ces employés, ceux qui ont été embauchés en 1980, 1981, 1982 et 1983--
SELECT COUNT(*) AS 'TOTAL EMPLOYEE'
FROM EMP;
SELECT *
FROM EMP
WHERE HIREDATE BETWEEN '1980-01-01' AND '1983-12-31';

-- Question 31 : Requête pour afficher les postes, le salaire de ces postes par numéro de département et le salaire total de ces postes incluant tous les départements--
SELECT JOB AS 'POSTE', DEPTNO AS 'DEPARTEMENT', SUM(SAL) AS 'Salary by dept'
FROM EMP
GROUP BY JOB, DEPTNO;

-- Question 32 : Requête pour afficher le nom, le numéro de département de tous les employés--
SELECT ENAME, DEPTNO
FROM EMP
WHERE 1;

-- Question 33 : Requête pour afficher une liste unique de tous les postes du département 30--
SELECT JOB
FROM EMP
WHERE DEPTNO=30;

-- Question 34 : Requête pour afficher le nom, le poste, le numéro de département et le nom du département de tous les employés basés à DALLAS--
SELECT ENAME, JOB, EMP.DEPTNO, DEPT.DNAME
FROM EMP, DEPT
WHERE DEPT.LOC='DALLAS';

-- Question 35 : Requête pour afficher le nom et le matricule des employés et de leur manager--
SELECT ENAME AS 'Emp#', EMPNO, MGR AS 'Mgr#'
FROM EMP
WHERE 1;

-- Question 36 : Requête pour afficher le nom, le poste, le département, le salaire et l'échelon de tous les employés--
SELECT ENAME, JOB, DEPTNO, SAL, DEPT.LOC
FROM EMP, DEPT
WHERE 1; 

-- Question 37 : Requête pour afficher le nom et la date d'embauche de tous les employés arrivés après l'employé Blake--
SELECT ENAME, HIREDATE
FROM EMP
WHERE HIREDATE > (SELECT HIREDATE FROM EMP WHERE ENAME='Blake');

-- Question 38 : Requête pour afficher le nom et la date d'embauche de tous les employés travaillant dans le même département que Blake, à l'exclusion de Blake--
SELECT EMP.ENAME AS 'NOM', EMP.HIREDATE AS 'Date_embauche'
FROM EMP 
JOIN DEPT ON EMP.DEPTNO = DEPT.DEPTNO
WHERE EMP.DEPTNO=(SELECT DEPTNO FROM EMP WHERE ENAME='Blake') AND ENAME != 'Blake';

-- Question 39 : Requête pour afficher le matricule et le nom de tous les employés qui gagnent plus que le salaire moyen--
SELECT ENAME, EMPNO
FROM EMP
WHERE SAL> (SELECT AVG(SAL) FROM EMP);

-- Question 40 : Requête pour afficher le matricule et le nom de tous les employés qui travaillent dans le même département que tout employé dont le nom contient un T--
SELECT EMPNO, ENAME
FROM EMP
JOIN DEPT ON EMP.DEPTNO=DEPT.DEPTNO
WHERE EMP.ENAME LIKE '%T%';

-- Question 41 : Requête pour afficher le numéro de département, le nom et le poste de tous les employés travaillant dans le département des ventes ('SALES')--
SELECT EMPNO, ENAME, JOB
FROM EMP
JOIN DEPT ON DEPT.DEPTNO=EMP.DEPTNO
WHERE DEPT.DNAME='SALES';