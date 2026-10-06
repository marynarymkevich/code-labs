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



