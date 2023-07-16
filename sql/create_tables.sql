DROP TABLE IF EXISTS public.tb_dim_customers;
DROP TABLE IF EXISTS public.tb_dim_category;


CREATE TABLE public.tb_dim_customers(
    customerid INTEGER PRIMARY KEY,
    firstname TEXT,
    lastname TEXT,
    email TEXT,
    password TEXT,
    segment TEXT,
    country TEXT,
    city TEXT,
    state TEXT,
    street TEXT,
    zipcode TEXT
);


CREATE TABLE public.tb_dim_category(
    categoryid INTEGER PRIMARY KEY,
    name TEXT
);