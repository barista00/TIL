-- 문제1 테이블 products 에서 평균 MSRP 보다 큰 product 의 productCode , productName , MSRP 를 조회하시오.
-- SELECT * FROM products;

SELECT productCode, productName, MSRP
FROM products
WHERE MSRP > (
	SELECT AVG(MSRP)
    FROM products
)
ORDER BY
	MSRP;

-- 문제2 테이블 customers 에서 2003년 1월 6일과 2003년 3월 26일 사이에 주문(order)을 한 고객의 customerNumber, customerName 를 조회하시오.
SELECT * FROM customers;
SELECT * FROM orders;

SELECT customerNumber, customerName
FROM customers
WHERE EXISTS (
SELECT orderDate
FROM orders
WHERE 
	orderDate >= '2003-01-06' AND
	orderDate <= '2003-03-26' AND
	orders.customerNumber = customers.customerNumber
)
ORDER BY
	customerNumber;

-- 문제3 productLine 가 Classic Cars 인 제품(product) 중 MSRP가 가장 큰 제품의 
-- productCode , productName , productLine , MSRP 를 조회하시오.
SELECT * FROM products;
SELECT * FROM productlines;

SELECT productCode, productName, productLine, MSRP
FROM products
WHERE MSRP = (
	SELECT MAX(MSRP)
	FROM products
	WHERE
		productLine = 'Classic Cars'
);

-- 문제4 가장 많은 고객(customer)이 사는 나라(country)의 customerNumber , customerName , country 를 조회하시오.
SELECT * FROM customers;

SELECT customerNumber , customerName , country
FROM customers
WHERE
	country = (
		SELECT country
		FROM customers
		GROUP BY
			country
		ORDER BY
			COUNT(country) DESC
		LIMIT 1
)
ORDER BY
	customerNumber;

-- 문제5 가장 많은 주문(order)을 한 고객(customer)의 customerNumber , customerName , 주문 수(order_count) 를 조회하시오.
SELECT * FROM customers; -- 고유한 customerNumber
SELECT * FROM orders; -- 주문내역이라 여러번 주문한 경우 customerNumber가 여러번 나온다

SELECT customers.customerNumber, customerName, COUNT(customers.customerNumber) AS order_count
FROM customers
INNER JOIN orders
	ON customers.customerNumber = orders.customerNumber
WHERE customers.customerNumber = (
	SELECT customerNumber
	FROM orders
	GROUP BY
		customerNumber
	ORDER BY
		COUNT(customerNumber) DESC
	LIMIT 1
)
GROUP BY
	customerNumber;

-- 문제6 주문 날짜(orderDate)가 2004년인 주문(orderdetail) 제품(product)의 productCode , productName 를 조회하시오.
-- 주문 날짜 데이터는 orders 테이블, 주문 - 제품 데이터는 orderdetails 테이블, 제품 데이터는 products 테이블을 활용합니다.
SELECT productCode FROM orderdetails GROUP BY productCode;
SELECT * FROM products; -- productsCode
SELECT * FROM orderdetails; -- orderNumber, productsCode
SELECT * FROM orders; -- orderNumber

SELECT orderNumber
FROM orders
WHERE 
	year(orderDate) = '2004'; 

SELECT orderdetails.productCode, products.productName
FROM orderdetails
INNER JOIN products
	ON orderdetails.productCode = products.productCode
INNER JOIN orders
	ON orderdetails.orderNumber = orders.orderNumber
WHERE
	orders.orderNumber IN 
(
	SELECT orderNumber
	FROM orders
	WHERE 
		year(orderDate) = '2004'
)
GROUP BY
	productCode
ORDER BY
	productCode DESC;
    
