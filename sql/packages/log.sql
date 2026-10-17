
-- *** The Lost Letter ***
    -- Tìm id của gói hàng được gửi:
        SELECT id FROM packages WHERE contents = '%Congratulatory%';
    -- Tìm id của địa chỉ mà gói hàng được thả:
        SELECT address_id FROM scans WHERE package_id = 384 AND "action" = 'DROP';
    -- Tìm địa chỉ dựa trên id của gói hàng được gửi:
        SELECT "address", "type" FROM addresses WHERE "id" IN (SELECT address_id FROM scans WHERE package_id = 384 AND "action" = 'Drop');

-- *** The Devious Delivery ***
    -- Tìm gói hàng có địa chỉ gửi không xác định
        SELECT * FROM packages WHERE from_address_id IS NULL;
    -- Tìm địa chỉ gói hàng đến
        SELECT "address" FROM "addresses" WHERE id IN (SELECT address_id FROM scans WHERE "action" = 'Drop' AND package_id = 5098);

-- *** The Forgotten Gift ***
    -- Tìm thông tin gói hàng gửi từ 109 Tileston đến 728 Maple Place
        SELECT * FROM packages WHERE from_address_id IN (SELECT id FROM addresses WHERE address = '109 Tileston Street') AND to_address_id IN (SELECT id FROM addresses WHERE address = '728 Maple Place');
    -- Gửi từ 2 tuần trước và sau 7 ngày ngày giao hàng chả có tin gì
        -- Tìm id người cầm cuối cùng
            SELECT * FROM scans WHERE package_id = 9523;
        -- Tìm thông tin người cầm cuối
            SELECT * FROM drivers WHERE id = 17;
