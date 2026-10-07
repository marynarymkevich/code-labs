SELECT COUNT(*) FROM orders;

INSERT INTO customers (customer_id, first_name, last_name, email, city, joined_date) VALUES (11, 'Maryna', 'Rymkevich', 'marinastr.ms@gmail.com', 'Stockholm', '2026-10-07');
INSERT INTO products (name, category, price, stock) VALUES  ('Scarf', 'Accessories', 229.00, 15), ('Gloves', 'Accessories', 199.00, 20);
INSERT INTO orders (order_id, customer_id, order_date, status) VALUES (16, 7, '2026-10-07', 'new');
INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES (16, 10, 2, 179.00);
-- INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES (16, 1, 0, 599.00); => Result: CHECK constraint failed: quantity > 0
UPDATE orders SET status='shipped' WHERE order_id=12;
UPDATE products SET stock=50  WHERE product_id=5;
UPDATE products set price=price*1.1 WHERE category='Accessories';