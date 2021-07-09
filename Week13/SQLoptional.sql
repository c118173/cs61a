-- Create Table
CREATE TABLE numbers (n, note);
CREATE TABLE numbers (n UNIQUE, note);
CREATE TABLE numbers (n, note DEFAULT "No comment");

-- Drop Tables
DROP TABLE IF EXISTS numbers;

-- Modifying Tables
CREATE TABLE primes(n UNIQUE, prime DEFAULT 1);
INSERT INTO primes VALUES (2, 1), (3, 1);
SELECT * FROM primes;
INSERT INTO primes(n) VALUES (4), (5), (6), (7);
INSERT INTO primes(n) SELECT n+6 FROM primes;
INSERT INTO primes(n) SELECT n+12 FROM primes;

UPDATE primes SET prime=0 WHERE n>2 AND n%2=0;
UPDATE primes SET prime=0 WHERE n>3 AND n%3=0;
UPDATE primes SET prime=0 WHERE n>5 AND n%5=0;

DELETE FROM primes WHERE prime=0;
SELECT * FROM primes;
