-- creates the table unique_id

CREATE TABLE IF NOT EXISTS `unique_id` (
	id int NOT NULL DEFAULT 1 UNIQUE,
	name VARCHAR(256)
	);
