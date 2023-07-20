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
        "columns":[
            'Order Id', 'order date (DateOrders)', 'Order Status', 'Market',
            'Order Region', 'Order Country', 'Order State', 'Order City',
            'Customer Id'
        ],
        "subset":['Order Id']
    }

}
