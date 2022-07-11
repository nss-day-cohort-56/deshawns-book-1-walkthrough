CREATE TABLE `walker` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name`    TEXT NOT NULL,
    `email`    TEXT NOT NULL
);

INSERT INTO `walker` VALUES (null, "Larry Fine", "larry@aol.com");
INSERT INTO `walker` VALUES (null, "Curly Howard", "curly@aol.com");
INSERT INTO `walker` VALUES (null, "Moe Howard", "moe@aol.com");

CREATE TABLE `dog` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name`    TEXT NOT NULL,
    `walker_id` INTEGER NOT NULL,
	FOREIGN KEY(`walker_id`) REFERENCES `walker`(`id`)
);

INSERT INTO `dog` VALUES (null, "Jack", 1);
INSERT INTO `dog` VALUES (null, "Eleanor", 2);
INSERT INTO `dog` VALUES (null, "Gracie", 3);
