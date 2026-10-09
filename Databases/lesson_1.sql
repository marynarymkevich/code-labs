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

-- EXTRA CHALLENGES
-- Level 1
SELECT * FROM products WHERE category !='Accessories' AND stock > 0 AND name LIKE '% %' ORDER BY category, price DESC;
SELECT * FROM customers WHERE city LIKE 'S%' OR city LIKE 'M%' OR city is NULL;
SELECT * FROM products WHERE category = 'Shoes' ORDER BY price DESC LIMIT 1 OFFSET 1;
SELECT * FROM customers WHERE  joined_date LIKE '2024%' OR joined_date LIKE '2025%' ORDER BY joined_date DESC LIMIT 3;

-- Level 2
SELECT first_name || ' ' || last_name AS full_name FROM customers ORDER BY last_name;
SELECT *,
       CASE 
           WHEN price < 200 THEN 'budget'
           WHEN price <= 799 THEN 'mid'
           ELSE 'premium'
       END AS price_level
FROM products;
SELECT first_name, COALESCE(city, 'Unknown') AS city FROM customers;
SELECT * FROM customers WHERE strftime('%m', joined_date) BETWEEN '01' AND '06';
SELECT * FROM products ORDER BY LENGTH(name) DESC LIMIT 1;
SELECT substr(customers.email, 1, (instr(customers.email, '@') -1)) AS username FROM customers;

-- Which products cost more than the average price? Don't type the average yourself: let SQL calculate it inside the query.
SELECT p.name, p.price FROM products p
WHERE p.price > (SELECT AVG(price) FROM products);

-- "Socks 3-pack costs 129 kr"
SELECT p.name || ' costs ' || CAST(p.price AS INT) || ' kr'  AS product_info FROM products p
WHERE p.stock > 0 ORDER BY price ASC;

-- How many customers live in each city? Biggest city first.
SELECT city, COUNT(*) AS customers_number 
FROM customers
GROUP BY city
ORDER BY customers_number DESC;

