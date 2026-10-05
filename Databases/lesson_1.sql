SELECT first_name, email FROM customers;
SELECT  *  FROM products WHERE category='Shoes';
SELECT * FROM customers WHERE city='Uppsala';
SELECT  *  FROM products WHERE price=199;
SELECT  *  FROM products ORDER BY name;
SELECT  *  FROM customers ORDER BY joined_date;
SELECT  *  FROM products WHERE stock=0;
SELECT  *  FROM customers ORDER BY joined_date DESC LIMIT 3;
SELECT * FROM customers WHERE city IN ('Stockholm', 'Göteborg');
SELECT name AS product, price AS price_sek FROM products;

-- Bonus questions
SELECT * FROM products WHERE (category = 'Clothing' OR category = 'Shoes') AND price > 1000;
SELECT * FROM products WHERE category = 'Clothing' OR category = 'Shoes' AND price > 1000;
SELECT name, price, stock, (price * stock) AS stock_value FROM products WHERE stock > 0 ORDER BY stock_value DESC;
SELECT * FROM customers WHERE first_name LIKE '____';
SELECT * FROM products ORDER BY price ASC LIMIT 5 OFFSET 5;
SELECT * FROM customers WHERE joined_date < '2025-01-01'  AND city != 'Uppsala' ORDER BY city ASC, last_name ASC;

