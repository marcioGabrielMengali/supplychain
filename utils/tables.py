dict_tables = {
    'tb_fact_sales': {
        "flag": "fact",
        "columns":[
            'Order Id',
            'Order Item Id',
            'Sales'
        ],
        "subset":None
    },
    'tb_dim_orders': {
        "flag": "dim",
        "columns":['Order Id', 'Type', 'order date (DateOrders)', 'Order Status', 'Market',
       'Order Region', 'Order Country', 'Order State', 'Order City',
       'Days for shipping (real)', 'Days for shipment (scheduled)',
       'Delivery Status', 'Late_delivery_risk', 'shipping date (DateOrders)',
       'Shipping Mode', 'Customer Id'],
        "subset":['Order Id']
    },
    'tb_dim_order_item': {
        "flag": "dim",
        "columns":['Order Item Id', 'Order Item Discount Rate', 'Order Item Profit Ratio', 'Product Card Id'],
        "subset":None
    },
    'tb_dim_products': {
        "flag": "dim",
        "columns":['Product Card Id', 'Product Name', 'Product Price', 'Product Status', 'Product Image', 'Category Id'],
        "subset":['Product Card Id']
    },
    'tb_dim_category': {
        "flag": "dim",
        "columns":['Category Id', 'Category Name', 'Department Id'],
        "subset":['Category Id']
    },
    'tb_dim_customers': {
        "flag": "dim",
        "columns":['Customer Id', 'Customer Lname', 'Customer Fname', 'Customer Country', 'Customer State', 'Customer Zipcode', 'Customer City', 'Customer Street'],
        "subset":['Customer Id']
    },
    'tb_dim_departments': {
        "flag": "dim",
        "columns":['Department Id', 'Department Name'],
        "subset":['Department Id']
    }

}
