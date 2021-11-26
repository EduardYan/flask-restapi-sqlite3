BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `book` (
	`id`	integer PRIMARY KEY AUTOINCREMENT,
	`name`	varchar ( 50 ) NOT NULL,
	`price`	integer NOT NULL
);
COMMIT;
