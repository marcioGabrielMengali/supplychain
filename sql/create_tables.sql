DROP TABLE IF EXISTS PUBLIC.tb_dim_customers;


DROP TABLE IF EXISTS PUBLIC.tb_dim_category;


CREATE TABLE PUBLIC.tb_dim_customers(
    customerid INTEGER PRIMARY KEY,
    firstname TEXT,
    lastname TEXT,
    email TEXT,
    PASSWORD TEXT,
    segment TEXT,
    country TEXT,
    city TEXT,
    state TEXT,
    street TEXT,
    zipcode TEXT
);


CREATE TABLE PUBLIC.tb_dim_category(
    categoryid INTEGER PRIMARY KEY,
    name TEXT
);