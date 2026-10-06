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

