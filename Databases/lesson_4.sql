SELECT COUNT(*) FROM orders;

-- Show every order with the customer's first name, last name and the order status.
SELECT 
	o.order_id,
	c.first_name,
	c.last_name,
	o.status
FROM orders o 
JOIN customers c
ON o.customer_id = c.customer_id;

-- Show all orders made by Erik
SELECT * FROM orders o JOIN customers c ON o.customer_id = c.customer_id WHERE c.first_name = 'Erik';

-- Show all orders from customers in Göteborg, newest first
SELECT * FROM orders o JOIN customers c ON o.customer_id = c.customer_id WHERE c.city = 'Göteborg' ORDER BY o.order_date DESC;

-- Show every order item with the product name and category
SELECT oi.order_id, pr.name, pr.category FROM order_items oi 
JOIN products pr ON oi.product_id = pr.product_id;

-- Which orders contained Shoes? Show order_id and product name
SELECT oi.order_id, pr.name FROM order_items oi
JOIN products pr ON oi.product_id = pr.product_id
WHERE pr.category = 'Shoes';

-- Show the full receipt for order 10: product name, quantity, unit price and line total
SELECT oi.order_id, pr.name, oi.quantity, pr.price, oi.quantity* pr.price as total 
FROM order_items oi
JOIN products pr ON oi.product_id = pr.product_id
WHERE oi.order_id = 10

-- Show which customers have bought a Hoodie Black (first name and order date)
SELECT c.first_name, o.order_date FROM orders o 
JOIN customers c ON o.customer_id = c.customer_id 
JOIN order_items oi ON o.order_id = oi.order_id 
JOIN products p ON oi.product_id = p.product_id
WHERE p.name = 'Hoodie Black'

