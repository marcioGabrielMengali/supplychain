--ADD COnstraints
ALTER TABLE supplychain.tb_fact_sales
ADD CONSTRAINT fk_sales_orders
FOREIGN KEY(orderid)
REFERENCES supplychain.tb_dim_orders (orderid);

ALTER TABLE supplychain.tb_fact_sales
ADD CONSTRAINT fk_sales_order_item
FOREIGN KEY(orderitemid)
REFERENCES supplychain.tb_dim_order_item (orderitemid);

ALTER TABLE supplychain.tb_dim_category
ADD CONSTRAINT fk_category_department
FOREIGN KEY (departmentid)
REFERENCES supplychain.tb_dim_departments (departmentid);

ALTER TABLE supplychain.tb_dim_order_item
ADD CONSTRAINT fk_order_item_product
FOREIGN KEY (productid)
REFERENCES supplychain.tb_dim_products (productid);

ALTER TABLE supplychain.tb_dim_orders
ADD CONSTRAINT fk_order_customers
FOREIGN KEY (customerid)
REFERENCES supplychain.tb_dim_customers (customerid);

ALTER TABLE supplychain.tb_dim_products
ADD CONSTRAINT fk_products_category
FOREIGN KEY (categoryid)
REFERENCES supplychain.tb_dim_category (categoryid);