-- Anna (customer 1) asks: 'Which products have I bought?' Write the query that answers her. Show
-- product names only, each once.
SELECT DISTINCT p.name
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
WHERE o.customer_id = 1;

--Erik says his email is wrong. Correct it to erik.johansson@example.com.
UPDATE customers 
SET email = 'erik.johansson@example.com' 
WHERE first_name = 'Erik';

--Create a view customer_overview that a support person can use: customer_id, first name, city and
--number of orders, but no email. Customers with no orders must also be shown.
CREATE VIEW customer_overview2 AS 
SELECT 
    c.customer_id, 
    c.first_name, 
    c.city, 
    COUNT(o.order_id) AS num_orders
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id;

SELECT * FROM customer_overview2;