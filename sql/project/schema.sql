-- Create Table
-- Create customers management table
CREATE TABLE `accounts`(
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(50) NOT NULL,
    `password` VARCHAR(127) NOT NULL,
    `email` VARCHAR(320) NOT NULL UNIQUE,
    `phone` VARCHAR(11) NOT NULL UNIQUE,
    `address` VARCHAR(100) NOT NULL,
    `created_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create items management table
CREATE TABLE `items`(
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(50) NOT NULL UNIQUE,
    `description` TEXT NOT NULL,
    `price` DECIMAL(15,2) NOT NULL CHECK(`price`>0),
    `inventory_quantity` SMALLINT NOT NULL CHECK(`inventory_quantity`>=0)
);

-- Create carts table
CREATE TABLE `carts`(
    `account_id` INT NOT NULL,
    `item_id` INT NOT NULL,
    `quantity` TINYINT NOT NULL,
    FOREIGN KEY (`account_id`) REFERENCES `accounts`(`id`) ON DELETE CASCADE,
    FOREIGN KEY (`item_id`) REFERENCES `items`(`id`) ON DELETE CASCADE,
    PRIMARY KEY (`account_id`, `item_id`)
);

-- Create rates table
CREATE TABLE `rates`(
    `account_id` INT NOT NULL,
    `item_id` INT NOT NULL,
    `comment` TINYTEXT NOT NULL,
    `rate` TINYINT NOT NULL,
    FOREIGN KEY (`account_id`) REFERENCES `accounts`(`id`) ON DELETE CASCADE,
    FOREIGN KEY (`item_id`) REFERENCES `items`(`id`) ON DELETE CASCADE,
    PRIMARY KEY (`account_id`, `item_id`)
);


-- Create transactions management table
CREATE TABLE `transactions`(
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `account_id` INT NOT NULL,
    `transaction_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `payment_method` ENUM("COD", "QR", "E-wallet") NOT NULL DEFAULT "QR",
    `state` ENUM("processing", "delivered", "canceled") NOT NULL DEFAULT "processing",
    FOREIGN KEY (`account_id`) REFERENCES `accounts`(`id`) ON DELETE CASCADE
);

-- Create transactions detail table
CREATE TABLE `transactions_detail`(
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `transaction_id` INT NOT NULL,
    `item_id` INT NOT NULL,
    `quantity` TINYINT NOT NULL,
    `current_price` DECIMAL(15,2) NOT NULL,
    FOREIGN KEY (`transaction_id`) REFERENCES `transactions`(`id`) ON DELETE CASCADE,
    FOREIGN KEY (`item_id`) REFERENCES `items`(`id`) ON DELETE CASCADE
);

-- Create views
-- Create `cart_detail` view
CREATE VIEW `cart_detail` AS
SELECT
    `a`.`id` AS `account_id`,
    `a`.`name` AS `account_name`,
    `a`.`phone` AS `account_phone`,
    `i`.`id` AS `item_id`,
    `i`.`name` AS `item_name`,
    `i`.`price` AS `item_price`,
    `c`.`quantity` AS `item_quantity`
FROM
    `carts` AS `c`
JOIN
    `accounts` AS `a` ON `c`.`account_id` = `a`.`id`
JOIN
    `items` AS `i` ON `c`.`item_id` = `i`.`id`;

-- Create `rate_detail` view
CREATE VIEW `rate_detail` AS
SELECT
    `a`.`id` AS `account_id`,
    `a`.`name` AS `account_name`,
    `a`.`phone` AS `account_phone`,
    `a`.`email` AS `account_email`,
    `i`.`id` AS `item_id`,
    `i`.`name` AS `item_name`,
    `r`.`comment` AS `comment`,
    `r`.`rate` AS `rate`
FROM
    `rates` AS `r`
JOIN
    `accounts` AS `a` ON `r`.`account_id` = `a`.`id`
JOIN
    `items` AS `i` ON `r`.`item_id` = `i`.`id`;

-- Create `transaction_history`
CREATE VIEW `transaction_history` AS
SELECT
    `a`.`id` AS `account_id`,
    `td`.`transaction_id` AS `transaction_id`,
    `t`.`transaction_date` AS `transaction_date`,
    `t`.`payment_method` AS `payment_method`,
    `t`.`state` AS `state`,
    `i`.`id` AS `item_id`,
    `i`.`name` AS `item_name`,
    `td`.`quantity` AS `buy_quantity`,
    `td`.`current_price` AS `price`
FROM
    `transactions` AS `t`
JOIN
    `accounts` AS `a` ON `t`.`account_id` = `a`.`id`
JOIN
    `transactions_detail` AS `td` ON `td`.`transaction_id` = `t`.`id`
JOIN
    `items` AS `i` ON `td`.`item_id` = `i`.`id`
ORDER BY
    `t`.`transaction_date` DESC;

-- Create a `total_bill` view
CREATE VIEW `total_bill` AS
SELECT
    `transaction_id`, SUM(`quantity`*`current_price`) AS `total_money`
FROM
    `transactions_detail`
GROUP BY
    `transaction_id`;


-- Create indexes
-- Create an covering index `idx_accounts_cover` on accounts table
CREATE INDEX `idx_accounts_cover`
ON `accounts`(`name`, `phone`, `email`);

-- Create an covering index `idx_items_cover` on items table
CREATE INDEX `idx_items_cover`
ON `items`(`price`, `name`);

-- Create an index `idx_rates` on rates table
CREATE INDEX `idx_rates`
ON `rates`(`rate`);

-- Create an index `idx_transactions` on transactions table
CREATE INDEX `idx_transactions`
ON `transactions`(`transaction_date`);

-- Create an covering index `idx_transactions_cover` on transactions table
CREATE INDEX `idx_transactions_cover`
ON `transactions`(`account_id`, `transaction_date`);

-- Create an covering index `idx_transactions_detail_cover` on transactions_detail table
CREATE INDEX `idx_transactions_detail_cover`
ON `transactions_detail`(`item_id`, `transaction_id`);


