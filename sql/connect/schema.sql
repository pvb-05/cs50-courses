CREATE TABLE "users"(
    "id" INT PRIMARY KEY,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "username" TEXT NOT NULL UNIQUE,
    "password" TEXT NOT NULL
);

CREATE TABLE "schools"(
    "id" INT PRIMARY KEY,
    "name" TEXT NOT NULL UNIQUE,
    "type" TEXT NOT NULL,
    "location" TEXT NOT NULL,
    "year" INT NOT NULL
);

CREATE TABLE "companies"(
    "id" INT PRIMARY KEY,
    "name" TEXT NOT NULL UNIQUE,
    "industry" TEXT NOT NULL,
    "location" TEXT NOT NULL
);

CREATE TABLE "follower"(
    "user_id_following" INT,
    "user2_id_followed" INT,
    FOREIGN KEY ("user_id_following") REFERENCES users("id"),
    FOREIGN KEY ("user2_id_followed") REFERENCES users("id")
);

CREATE TABLE "education"(
    "id" INT PRIMARY KEY,
    "school_id" INT,
    "user_id" INT,
    "date_attending" TEXT NOT NULL,
    "date_guaranting" TEXT NOT NULL,
    "degree" TEXT NOT NULL,
    FOREIGN KEY ("school_id") REFERENCES schools("id"),
    FOREIGN KEY ("user_id") REFERENCES users("id")
);

CREATE TABLE "employment"(
    "id" INT PRIMARY KEY,
    "company_id" INT,
    "user_id" INT,
    "date_start" TEXT NOT NULL,
    "date_left" TEXT NOT NULL,
    "title" TEXT NOT NULL,
    FOREIGN KEY ("company_id") REFERENCES companies("id"),
    FOREIGN KEY ("user_id") REFERENCES users("id")
);
