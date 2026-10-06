CREATE TABLE books (
	book_id INTEGER PRIMARY KEY ,
	title TEXT NOT NULL,
	author TEXT,
    year INTEGER
);

DROP TABLE IF EXISTS books;

CREATE TABLE books (
	book_id INTEGER PRIMARY KEY ,
	title TEXT NOT NULL,
	author TEXT,
    year INTEGER CHECK (year > 1400)
);

ALTER TABLE books ADD isbn TEXT;

DROP TABLE IF EXISTS books;

CREATE TABLE reviews(
	review_id INTEGER PRIMARY KEY ,
	product_id INTEGER,
	rating INTEGER CHECK (rating >= 1 AND rating <= 5),
	comment TEXT,
	FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- INSERT INTO reviews (product_id, rating, comment) VALUES (1, 6, 'Great product'); => Result: CHECK constraint failed: rating >= 1 AND rating <= 5

-- INSERT INTO reviews (product_id, rating, comment) VALUES (50, 5, 'Great product!'); => Result: FOREIGN KEY constraint failed

--- EXTRA CHALLENGES
-- LEVEL 1
CREATE TABLE suppliers (
	supplier_id INTEGER PRIMARY KEY,
	name TEXT NOT NULL UNIQUE,
	country TEXT DEFAULT 'Sweden',
	email TEXT
);

INSERT INTO suppliers (name, email) VALUES ('Nick', 'nick@gmail.com');
SELECT * FROM suppliers;

-- INSERT INTO suppliers (name, email) VALUES ('Nick', 'nick22@gmail.com'); => Result: UNIQUE constraint failed: suppliers.name

CREATE TABLE coupons (
    code TEXT PRIMARY KEY,
    discount_percent INTEGER CHECK (discount_percent BETWEEN 1 AND 90),
    valid_until TEXT NOT NULL
);
-- INSERT INTO coupons (code, discount_percent, valid_until) VALUES ('SUMMER95', 95, '2025-08-31'); => Result: CHECK constraint failed: discount_percent BETWEEN 1 AND 90

-- LEVEL 2
INSERT INTO suppliers (name, email) VALUES ('Marina', 'mar@gmail.com');
SELECT * FROM suppliers; -- => supplier_id = 2

ALTER TABLE suppliers RENAME COLUMN email TO contact_email;
PRAGMA table_info(products);
CREATE TABLE product_suppliers (
	purchase_price REAL CHECK (purchase_price > 0),
	product_id INTEGER REFERENCES products(product_id),
	supplier_id INTEGER REFERENCES suppliers(supplier_id),
	PRIMARY KEY (product_id, supplier_id)
);
-- INSERT INTO product_suppliers (product_id, supplier_id, purchase_price) VALUES (1, 99, 15.5); => Result: FOREIGN KEY constraint failed

CREATE TABLE campaigns (
    campaign_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL,
    CHECK (end_date >= start_date)
);
-- INSERT INTO campaigns (name, start_date, end_date)  VALUES ('Summer sale', '2025-07-28', '2025-07-20'); => Result: CHECK constraint failed: end_date >= start_date

-- Level 3