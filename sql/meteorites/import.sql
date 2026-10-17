CREATE TABLE "temp"(
    name TEXT,
    id INT,
    nametype TEXT,
    class TEXT,
    mass NUMERIC,
    discovery TEXT,
    year NUMERIC,
    lat NUMERIC,
    long NUMERIC
);

.import --csv --skip 1 meteorites.csv "temp"

UPDATE "temp"
SET mass = NULL
WHERE mass = '';

UPDATE "temp"
SET year = NULL
WHERE year = '';

UPDATE "temp"
SET lat = NULL
WHERE lat = '';

UPDATE "temp"
SET long = NULL
WHERE long = '';

UPDATE "temp"
SET mass = ROUND(mass,2);

UPDATE "temp"
SET lat = ROUND(lat,2);

UPDATE "temp"
SET long = ROUND(long,2);

DELETE FROM "temp" WHERE nametype = 'Relict';

CREATE TABLE "meteorites"(
    id INTEGER PRIMARY KEY,
    name TEXT,
    class TEXT,
    mass NUMERIC,
    discovery TEXT,
    year NUMERIC,
    lat NUMERIC,
    long NUMERIC
);

INSERT INTO "meteorites" (name,class,mass,discovery,year,lat,long)
SELECT name,class,mass,discovery,year,lat,long
FROM "temp"
ORDER BY year ASC, name ASC;

DROP TABLE "temp";
