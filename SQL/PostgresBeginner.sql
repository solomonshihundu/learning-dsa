--creating a database --
CREATE DATABASE postgres
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

COMMENT ON DATABASE postgres
    IS 'default administrative connection database';
    
--Create schema plain --
CREATE SCHEMA test1;

--With Authorization to specifiy user onwner --
CREATE SCHEMA test2 AUTHORIZATION postgres;

--With schema elemnts --
CREATE SCHEMA test3 
CREATE TABLE temp1(first_name VARCHAR,age NUMERIC,pets VARCHAR[])
CREATE VIEW petowners AS SELECT first_name,age FROM temp1 WHERE pets IS NOT NULL;

--With exception handling --
CREATE SCHEMA IF NOT EXISTS test3 AUTHORIZATION postgres;


-- SELECT * FROM pg_catalog.pg_user;

SELECT schema_name, schema_owner
FROM information_schema.schemata;

SELECT * FROM test3.temp1;