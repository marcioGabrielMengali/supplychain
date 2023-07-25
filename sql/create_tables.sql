--CREATE SCHEMA supplychain
CREATE SCHEMA IF NOT EXISTS supplychain;

--FACT TABLES
CREATE TABLE IF NOT EXISTS supplychain.tb_fact_sales(
    orderid INTEGER,
    orderitem INTEGER,
    sales REAL,
    PRIMARY KEY(orderid, orderitem)
);

--DIM TABELS
CREATE TABLE IF NOT EXISTS supplychain.tb_dim_orders(
    orderid INTEGER,
    type VARCHAR(255),
    orderdate TIMESTAMP,
    orderstatus VARCHAR(255),
    market VARCHAR(255),
    orderregion VARCHAR(255),
    ordercountry VARCHAR(255),
    orderstate VARCHAR(255),
    ordercity VARCHAR(255),
    daysforshipping INTEGER,
    daysforshippiment INTEGER,
    deliverystatus VARCHAR(255),
    latedeliveryrisk INTEGER,
    shippingdate TIMESTAMP,
    shippingmode VARCHAR(255),
    customerid INTEGER,
    PRIMARY KEY(orderid)
);

CREATE TABLE IF NOT EXISTS supplychain.tb_dim_order_item(
    orderitemid INTEGER,
    orderitemdiscountrate FLOAT,
    orderitemprofitraio FLOAT,
    productid INTEGER,
    PRIMARY KEY(orderitemid)
);

CREATE TABLE IF NOT EXISTS supplychain.tb_dim_products(
    productid INTEGER,
    productname TEXT,
    productprice REAL,
    productstatus VARCHAR(255),
    productimage TEXT,
    categoryid INTEGER,
    PRIMARY KEY(productid)
);

CREATE TABLE IF NOT EXISTS supplychain.tb_dim_category(
    categoryid INTEGER,
    categoryname TEXT,
    departmentid INTEGER,
    PRIMARY KEY(categoryid)
);

CREATE TABLE IF NOT EXISTS supplychain.tb_dim_customers(
    customerid INTEGER,
    customerlastname TEXT,
    customerfirstname TEXT,
    customercountry VARCHAR(255),
    customerstate VARCHAR(255),
    customerzipcode VARCHAR(255),
    customercity VARCHAR(255),
    customerstreet VARCHAR(255),
    PRIMARY KEY(customerid)

);

CREATE TABLE IF NOT EXISTS supplychain.tb_dim_department(
    departmentid INTEGER,
    departmentname TEXT,
    PRIMARY KEY(departmentid)
);





`