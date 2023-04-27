-- 문제1 테이블 employees 과 테이블 offices 를 officeCode 기준으로 INNER JOIN 한 데이터를 조회하시오.
SELECT employeeNumber, lastName, firstName, city
FROM employees
INNER JOIN offices
	ON employees.officeCode = offices.officeCode
ORDER BY
	employeeNumber;

SELECT * FROM employees;
SELECT * FROM offices;

-- 문제2 테이블 customers 와 테이블 offices 를 city 기준으로 LEFT JOIN 한 데이터를 조회하시오.
SELECT customerNumber, officeCode, customers.city, offices.city
FROM customers
LEFT JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;

-- 문제3 테이블 customers 와 테이블 offices 를 city 기준으로 RIGHT JOIN 한 데이터를 조회하시오.
SELECT customerNumber , officeCode, customers.city, offices.city 
FROM customers
RIGHT JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;

-- 문제4 테이블 customers 와 테이블 offices 를 city 기준으로 INNER JOIN 한 데이터를 조회하시오.
SELECT customerNumber , officeCode, customers.city, offices.city 
FROM customers
INNER JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;

-- 문제5 문제 2, 문제 3, 문제 4 의 조회 결과가 다른 이유를 작성하시오.
-- 2,3번의 경우 2개의 테이블에서 fk, pk값이 동일한 레코드와 그렇지 않은 레코드를 같이 출력하는데(LEFT의 경우 왼쪽의 모든 레코드, RIGHT는 오른쪽 테이블의 모든 레코드)
-- JOIN하는 테이블, 메인테이블에서 fk,pk가 다른 경우 LEFT와 RIGHT에 따라 NULL을 출력하기 때문에 
-- fk, pk가 같은 레코드만 출력하는 4번과 차이가있다

-- 문제6 테이블 customers 와 테이블 offices 를 city 기준으로 FULL OUTER JOIN 한 데이터를 조회하시오.
SELECT customerNumber , officeCode, customers.city, offices.city 
FROM customers
LEFT JOIN offices
	ON customers.city = offices.city
UNION
SELECT customerNumber , officeCode, customers.city, offices.city 
FROM customers
RIGHT JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;

-- 문제7 테이블 orderdetails 와 테이블 orders 를 INNER JOIN 한 데이터를 조회하시오.
SELECT * FROM orderdetails;
SELECT * FROM orders;
SELECT orderdetails.orderNumber, orderDate
FROM orderdetails
INNER JOIN orders
	ON orderdetails.orderNumber = orders.orderNumber
ORDER BY
	orderNumber;

-- 문제8 테이블 orderdetails 와 테이블 products 을 INNER JOIN 한 데이터를 조회하시오.
SELECT orderNumber, orderdetails.productCode, productName
FROM orderdetails
INNER JOIN products
	ON orderdetails.productCode = products.productCode
ORDER BY
	orderNumber;

-- 문제9 테이블 orderdetails , 테이블 orders , 테이블 products 를 INNER JOIN 한 데이터를 조회하시오.
SELECT orders.orderNumber, orderdetails.productCode, orders.orderDate, productName
FROM orders
INNER JOIN orderdetails
	ON orders.orderNumber = orderdetails.orderNumber
INNER JOIN products
	ON products.productCode = orderdetails.productCode
ORDER BY
	orderNumber;
SELECT * FROM orders; -- orderNumber
SELECT * FROM orderdetails; -- orderNumber, productCode
SELECT * FROM products; -- productCode

SELECT orders.orderNumber, orderdetails.productCode, orders.orderDate, productName
FROM orderdetails
INNER JOIN orders
	ON orders.orderNumber = orderdetails.orderNumber
INNER JOIN products
	ON orderdetails.productCode = products.productCode
ORDER BY
	orderNumber;