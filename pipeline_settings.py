config = {
    'pipeline': 'daily_sales',
    'source': 'type: csv',
    'path': '/data/in/sales.csv',
    'delimiter': ',',
    'target': {'db': 'internal', 'port': 5432},
    'table': 'stage_sales',
    'columns': ['order_id', 'amount'],
    'store': True,
    'amount': True,
    'active': True
}

print(config['path'])
host = config['target']['db']
port = config['target']['port']
print("host =", "db." + host, ", port =", port)
config['table'] = 'stage_sales_v2'
print(config['table'])
config['columns'].append('sale_date')
print(config['columns'])
print("amount:", config['amount'], "discount:", config.get('discount', False))
config['retries'] = 3
print("retries:", config['retries'])
print(list(config.keys()))