import json
import sys
import re

def read_orders(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)

def format_phone_number(phone):
    digits = re.sub(r'\D', '', phone)
    return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}" if len(digits) == 10 else phone

def extract_customers(orders):
    customers = {}
    for order in orders:
        name = next((order.get(key) for key in ['customer', 'customer_name', 'name'] if order.get(key)), None)
        phone = order.get('phone')

        if not name or not phone:
            print(f"Warning: Missing 'name' or 'phone' in order: {order}")
            continue

        phone = format_phone_number(phone)
        customers[phone] = name
    return customers

def extract_items(orders):
    items = {}
    for order in orders:
        for item in order.get('items', []):
            name = item.get('name')
            price = item.get('price')

            if not name or price is None:
                print(f"Warning: Missing 'name' or 'price' in item: {item}")
                continue
            
            price = float(price)  # Ensure price is a number
            
            if name not in items:
                items[name] = {'price': price, 'orders': 0}
            items[name]['orders'] += 1
    
    return items

def write_json(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <orders_file.json>")
        sys.exit(1)

    orders_file = sys.argv[1]
    try:
        orders = read_orders(orders_file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading '{orders_file}': {e}")
        sys.exit(1)

    customers = extract_customers(orders)
    items = extract_items(orders)

    write_json(customers, 'customers.json')
    write_json(items, 'items.json')
    
    print("customers.json and items.json have been created.")

if __name__ == "__main__":
    main()
