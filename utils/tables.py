dict_tables = {
    'tb_fact_sales': {
        "flag": "fact",
        "columns": [
            'Order Id',
            'Order Item Id',
            'Sales'
        ],
        "renamed_columns": {
            'Order Id': 'orderid',
            'Order Item Id': 'orderitemid',
            'Sales': 'sales'
        },
        "subset": None
    },
    'tb_dim_orders': {
        "flag": "dim",
        "columns": ['Order Id', 'Type', 'order date (DateOrders)', 'Order Status', 'Market',
                    'Order Region', 'Order Country', 'Order State', 'Order City',
                    'Days for shipping (real)', 'Days for shipment (scheduled)',
                    'Delivery Status', 'Late_delivery_risk', 'shipping date (DateOrders)',
                    'Shipping Mode', 'Customer Id'],
        "renamed_columns": {
            'Order Id': 'orderid',
            'Type': 'type',
            'order date (DateOrders)': 'orderdate',
            'Order Status': 'orderstatus',
            'Market': 'market',
            'Order Region': 'orderregion',
            'Order Country': 'ordercountry',
            'Order State': 'orderstate',
            'Order City': 'ordercity',
            'Days for shipping (real)': 'daysforshipping',
            'Days for shipment (scheduled)': 'daysforshippiment',
            'Delivery Status': 'deliverystatus',
            'Late_delivery_risk': 'latedeliveryrisk',
            'shipping date (DateOrders)': 'shippingdate',
            'Shipping Mode': 'shippingmode',
            'Customer Id': 'customerid'
        },
        "subset": ['Order Id']
    },
    'tb_dim_order_item': {
        "flag": "dim",
        "columns": ['Order Item Id', 'Order Item Discount Rate', 'Order Item Profit Ratio', 'Product Card Id'],
        "renamed_columns": {
            'Order Item Id': 'orderitemid',
            'Order Item Discount Rate': 'orderitemdiscountrate',
            'Order Item Profit Ratio': 'orderitemprofitratio',
            'Product Card Id': 'productid'
        },
        "subset": None
    },
    'tb_dim_products': {
        "flag": "dim",
        "columns": ['Product Card Id', 'Product Name', 'Product Price', 'Product Status', 'Product Image', 'Category Id'],
        "renamed_columns": {
            'Product Card Id': 'productid',
            'Product Name': 'productname',
            'Product Price': 'productprice',
            'Product Status': 'productstatus',
            'Product Image': 'productimage',
            'Category Id': 'categoryid'
        },
        "subset": ['Product Card Id']
    },
    'tb_dim_category': {
        "flag": "dim",
        "columns": ['Category Id', 'Category Name', 'Department Id'],
        "renamed_columns": {
            'Category Id': 'categoryid',
            'Category Name': 'categoryname',
            'Department Id': 'departmentid'
        },
        "subset": ['Category Id']
    },
    'tb_dim_customers': {
        "flag": "dim",
        "columns": ['Customer Id', 'Customer Lname', 'Customer Fname', 'Customer Country', 'Customer State', 'Customer Zipcode', 'Customer City', 'Customer Street'],
        "renamed_columns": {
            'Customer Id': 'customerid',
            'Customer Lname': 'customerlastname',
            'Customer Fname': 'customerfirstname',
            'Customer Country': 'customercountry',
            'Customer State': 'customerstate',
            'Customer Zipcode': 'customerzipcode',
            'Customer City': 'customercity',
            'Customer Street': 'customerstreet'
        },
        "subset": ['Customer Id']
    },
    'tb_dim_departments': {
        "flag": "dim",
        "columns": ['Department Id', 'Department Name'],
        "renamed_columns": {
            'Department Id': 'departmentid',
            'Department Name': 'departmentname'
        },
        "subset": ['Department Id']
    }

}
