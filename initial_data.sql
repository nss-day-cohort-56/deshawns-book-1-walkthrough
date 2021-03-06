-- DROP TABLE dog;
DROP TABLE walker;
DROP TABLE city;

CREATE TABLE `city` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name`    TEXT NOT NULL
);

INSERT INTO `city` VALUES (null, "Nashville");
INSERT INTO `city` VALUES (null, "Hermitage");
INSERT INTO `city` VALUES (null, "Bellevue");

CREATE TABLE `walker` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name`    TEXT NOT NULL,
    `email`    TEXT NOT NULL,
    `city_id` INTEGER,
	FOREIGN KEY(`city_id`) REFERENCES `city`(`id`)
);

INSERT INTO `walker` VALUES (null, "Larry Fine", "larry@aol.com", 1);
INSERT INTO `walker` VALUES (null, "Curly Howard", "curly@aol.com", 2);
INSERT INTO `walker` VALUES (null, "Moe Howard", "moe@aol.com", 3);

CREATE TABLE `dog` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name`    TEXT NOT NULL,
    `walker_id` INTEGER NOT NULL,
	FOREIGN KEY(`walker_id`) REFERENCES `walker`(`id`)
);

INSERT INTO `dog` VALUES (null, "Jack", 1);
INSERT INTO `dog` VALUES (null, "Eleanor", 2);
INSERT INTO `dog` VALUES (null, "Gracie", 3);
