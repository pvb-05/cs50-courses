CREATE TABLE "ingredients"(
    "id" INT PRIMARY KEY,
    "name" TEXT NOT NULL UNIQUE,
    "price_per_unit" NUMERIC NOT NULL
);

CREATE TABLE "donuts"(
    "id" INT PRIMARY KEY,
    "name" TEXT NOT NULL UNIQUE,
    "gluten_free" BOOL NOT NULL,
    "price_per_donut" NUMERIC NOT NULL
);

CREATE TABLE "donut_ingredients"(
    "donut_id" INT,
    "ingredient_id" INT,
    FOREIGN KEY ("donut_id") REFERENCES "donuts"("id"),
    FOREIGN KEY ("ingredient_id") REFERENCES "ingredients"("id")
);

CREATE TABLE "orders"(
    "id" INT PRIMARY KEY,
    "number" INT NOT NULL,
    "customer_id" INT,
    FOREIGN KEY ("customer_id") REFERENCES "customers"("id")
);

CREATE TABLE "customers"(
    "id" INT PRIMARY KEY,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL
);

CREATE TABLE "order_details"(
    "order_id" INTEGER,
    "donut_id" INTEGER,
    "quantity" INTEGER NOT NULL,
    FOREIGN KEY ("order_id") REFERENCES "orders"("id"),
    FOREIGN KEY ("donut_id") REFERENCES "donuts"("id")
);
