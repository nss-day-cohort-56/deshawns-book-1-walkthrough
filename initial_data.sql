CREATE TABLE `city` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name`    TEXT NOT NULL
)

CREATE TABLE `walker` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name`    TEXT NOT NULL,
    `email`    TEXT NOT NULL,
    `city_id` INTEGER,
	FOREIGN KEY(`city_id`) REFERENCES `city`(`id`),
);

INSERT INTO `walker` VALUES (null, "Larry Fine", "larry@aol.com");
INSERT INTO `walker` VALUES (null, "Curly Howard", "curly@aol.com");
INSERT INTO `walker` VALUES (null, "Moe Howard", "moe@aol.com");

-- TODO: create the dog table and 3 insert statements
