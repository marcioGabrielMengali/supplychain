--Sales Per Orders
SELECT
orderid, SUM(sales) AS total_sales
FROM supplychain.tb_fact_sales
GROUP BY orderid
ORDER BY total_sales DESC;

--Top products per order
WITH products_sales AS(
	SELECT sales.orderid, products.productname ,SUM(sales.sales) AS total_sales
	FROM supplychain.tb_fact_sales AS sales
	INNER JOIN supplychain.tb_dim_order_item AS orderitem
	ON sales.orderitemid = orderitem.orderitemid
	INNER JOIN supplychain.tb_dim_products AS products
	ON orderitem.productid = products.productid
	GROUP BY sales.orderid, products.productname
)

SELECT products_sales.*,
	DENSE_RANK() OVER(
		PARTITION BY orderid
		ORDER BY total_sales DESC
	) AS ranking
FROM products_sales
ORDER BY orderid, ranking ASC;

-- Top Products
WITH products_sales AS(
	SELECT products.productname, ROUND(SUM(sales.sales)::float) AS total_sales
	FROM supplychain.tb_fact_sales AS sales
	INNER JOIN supplychain.tb_dim_order_item AS orderitem
	ON sales.orderitemid = orderitem.orderitemid
	INNER JOIN supplychain.tb_dim_products AS products
	ON orderitem.productid = products.productid
	GROUP BY products.productname
)

SELECT products_sales.*,
	DENSE_RANK() OVER(
		ORDER BY total_sales DESC
	) AS ranking
FROM products_sales
ORDER BY ranking ASC;

-- Sales Country
SELECT orders.ordercountry, SUM(sales.sales)::float AS total_sales
FROM supplychain.tb_fact_sales AS sales
INNER JOIN supplychain.tb_dim_orders AS orders
ON sales.orderid = orders.orderid
GROUP BY orders.ordercountry
ORDER BY total_sales DESC;