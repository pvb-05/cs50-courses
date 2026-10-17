-- Add a new account to `accounts` table when created
INSERT INTO `accounts` (`name`, `password`, `email`, `phone`, `address`)
VALUES ("Phan Văn Bắc", "hashed_password_6", "bac.phan@example.com", "0328966859", "18 Ngõ 32 Phú Hải 2, Quận Dương Kinh, Hải Phòng");

-- Add a new item to `items` table
INSERT INTO `items` (`name`, `description`, `price`, `inventory_quantity`)
VALUES ("Áo Lá 3 Dây", "Áo ngực dành cho trẻ con, tặng kèm quần lót dễ thương", 180000.00, 200);

-- Delete item
DELETE FROM `items`
WHERE `id` = 1;

-- Add items to `carts`
-- Bắc's cart
INSERT INTO `carts` (`account_id`, `item_id`, `quantity`)
VALUES (6, 9, 1);

-- An's carts
INSERT INTO `carts` (`account_id`, `item_id`, `quantity`)
VALUES (1, 1, 2);

-- Display user's cart
SELECT `account_name`, `account_phone`, `item_name`, `item_price`, `item_quantity`
FROM `cart_detail`
WHERE `account_id` = 6
ORDER BY `item_name` ASC;


-- Add reviews to `rates` table (only review after buy items)
INSERT INTO `rates` (`account_id`, `item_id`, `comment`, `rate`)
VALUES (6, 10, 'Quần tất siêu xinh luôn các nàng.', 5);

-- Display rates detail
SELECT *
FROM `rate_detail`;

-- Dispaly total money of transaction
SELECT *
FROM `total_bill`
WHERE transaction_id = ?;


-- Add transaction when customer buy all item in cart
BEGIN TRANSACTION `buy`;

INSERT INTO `transactions`(`account_id`, `payment_method`)
VALUES (?, ?);

-- Loop add item to cart and update inventry quantity
INSERT INTO `transactions_detail`(`transaction_id`, `item_id`, `quantity`, `current_price`)
VALUES (?, ?, ?, ?);

UPDATE `items`
SET `inventory_quantity` = ?
WHERE id = (
    SELECT `item_id`
    FROM `transactions_detail`
    WHERE `transaction_id` = ?
);

DELETE FROM `carts`
WHERE `account_id` = ?

COMMIT;

