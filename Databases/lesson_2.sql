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
CREATE TABLE product_sizes (
    size_id INTEGER PRIMARY KEY,
    product_id INTEGER REFERENCES products(product_id),
    size TEXT CHECK (size IN ('S', 'M', 'L', 'XL')),
    stock INTEGER DEFAULT 0,
    UNIQUE (product_id, size)
);
INSERT INTO product_sizes (product_id, size, stock) VALUES (1, 'M', 10);
INSERT INTO product_sizes (product_id, size, stock) VALUES (2, 'L', 5);
-- INSERT INTO product_sizes (product_id, size, stock)  VALUES (1, 'M', 5); => Result: UNIQUE constraint failed: product_sizes.product_id, product_sizes.size

CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    title TEXT,
    manager_id INTEGER,
    FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
);
INSERT INTO employees (name, title, manager_id) VALUES ('Alice', 'CEO', NULL);
INSERT INTO employees (name, title, manager_id) VALUES ('Bob', 'Developer', 1), ('Anna', 'Designer', 1);

CREATE TABLE teams (
    team_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE players (
    player_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    team_id INTEGER,
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE
);
INSERT INTO teams (name) VALUES ('Team 1');
INSERT INTO teams (name) VALUES ('Team 2');
INSERT INTO teams (name) VALUES ('Team 3');
INSERT INTO players (name, team_id) VALUES ('Alex', 1), ('Ben', 1);
DELETE FROM teams WHERE team_id = 1;
SELECT * FROM players;