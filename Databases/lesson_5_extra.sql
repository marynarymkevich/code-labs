SELECT COUNT(*) FROM orders;

-- Show products in Clothing or Accessories that cost between 150 and 500 kr. Most expensive first.
SELECT * FROM products WHERE (category='Clothing' OR  category ='Accessories' ) AND price BETWEEN 150 AND 500 ORDER BY price DESC;

-- Which orders were placed in February 2026 and are not cancelled?
SELECT * FROM orders WHERE strftime('%m', order_date) = '02' AND strftime('%Y', order_date) = '2026' AND status != 'cancelled'

-- Show every order line with the order_id, product name, quantity and line total (quantity times unit
-- price). Only show lines where the line total is more than 500 kr. Biggest first.
SELECT oi.order_id, p.name, oi.quantity, oi.quantity*p.price AS total FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
WHERE (oi.quantity * p.price) > 500 ORDER BY total DESC;

-- Which customers from Uppsala or Stockholm have placed at least one order? Each customer only once.
SELECT DISTINCT c.customer_id, c.first_name, c.last_name, c.city FROM customers c
JOIN orders o ON o.customer_id=c.customer_id
WHERE (city='Uppsala' OR city='Stockholm')