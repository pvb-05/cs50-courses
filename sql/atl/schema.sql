CREATE TABLE "passengers"(
    "id" INT PRIMARY KEY,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "age" INT NOT NULL
);

CREATE TABLE "check_ins"(
    "id" INT PRIMARY KEY,
    "passenger_id" INT,
    "flight_id" INT,
    "date_time" TEXT NOT NULL,
    FOREIGN KEY ("passenger_id") REFERENCES passengers("id"),
    FOREIGN KEY ("flight_id") REFERENCES flights("id")
);

CREATE TABLE "airlines"(
    "id" INT PRIMARY KEY,
    "name" TEXT NOT NULL UNIQUE,
    "concourse" TEXT NOT NULL CHECK("concourse" IN ('A', 'B', 'C', 'D', 'E', 'F', 'T'))
);

CREATE TABLE "flights"(
    "id" INT PRIMARY KEY,
    "flight_number" INT NOT NULL,
    "airline" INT,
    "code_departing" TEXT NOT NULL,
    "code_heading" TEXT NOT NULL,
    "datetime_departing" TEXT NOT NULL,
    "datetime_heading" TEXT NOT NULL,
    FOREIGN KEY ("airline") REFERENCES airlines("id")
);
