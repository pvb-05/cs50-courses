CREATE TABLE `users`(
    `id` INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    `first_name` VARCHAR(50) NOT NULL,
    `last_name` VARCHAR(50) NOT NULL,
    `username` VARCHAR(20) NOT NULL UNIQUE,
    `password` VARCHAR(128) NOT NULL
);

CREATE TABLE `schools`(
    `id` INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(50) NOT NULL UNIQUE,
    `type` ENUM("Primary", "Secondary", "Higher Education") NOT NULL,
    `location` VARCHAR(100) NOT NULL,
    `founded_year` SMALLINT UNSIGNED NOT NULL
);

CREATE TABLE `companies`(
    `id` INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(50) NOT NULL UNIQUE,
    `industry` ENUM("Technology", "Education", "Business") NOT NULL,
    `location` VARCHAR(100) NOT NULL
);

CREATE TABLE `follows`(
    `id` INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    `user_follower` INT UNSIGNED NOT NULL,
    `user_followed` INT UNSIGNED NOT NULL,
    FOREIGN KEY `follows`("user_follower") REFERENCES `users`("id"),
    FOREIGN KEY `follows`("user_followed") REFERENCES `users`("id")
);

CREATE TABLE `educations`(
    `id` INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    `user_id` INT NOT NULL,
    `school_id` INT NOT NULL,
    `attend_date` DATE NOT NULL,
    `graduate_date` DATE,
    `degree` VARCHAR(5) NOT NULL
    FOREIGN KEY `educations`("user_id") REFERENCES `users`("id"),
    FOREIGN KEY `educations`("school_id") REFERENCES `schools`("id")
);

CREATE TABLE `works`(
    `id` INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    `user_id` INT NOT NULL,
    `company_id` INT NOT NULL,
    `attend_date` DATE NOT NULL,
    `left_date` DATE,
    FOREIGN KEY `educations`("user_id") REFERENCES `users`("id"),
    FOREIGN KEY `educations`("company_id") REFERENCES `companies`("id")
);
