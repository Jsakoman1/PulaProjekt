TABLES_METADATA = {
    'Clients': {
        'table_name': 'Clients',
        'fields': ['client_id', 'name', 'contact_name', 'contact_phone', 'contact_email', 'address'],
        'labels': ['Client ID', 'Name', 'Contact Name', 'Contact Phone', 'Contact Email', 'Address'],
        'primary_key': 'client_id',
    },
    'Suppliers': {
        'table_name': 'Suppliers',
        'fields': ['supplier_id', 'name', 'contact_name', 'contact_phone', 'contact_email', 'address'],
        'labels': ['Supplier ID', 'Name', 'Contact Name', 'Contact Phone', 'Contact Email', 'Address'],
        'primary_key': 'supplier_id',
    },
    'Departments': {
        'table_name': 'Departments',
        'fields': ['department_id', 'name', 'description', 'manager_id', 'location', 'budget', 'established', 'is_active', 'created_at', 'updated_at'],
        'labels': ['Department ID', 'Name', 'Description', 'Manager ID', 'Location', 'Budget', 'Established', 'Is Active', 'Created At', 'Updated At'],
        'primary_key': 'department_id',
    },
    'Employees': {
        'table_name': 'Employees',
        'fields': ['employee_id', 'first_name', 'last_name', 'position', 'hire_date', 'salary', 'department_id', 'status', 'phone_number', 'address', 'email', 'date_of_birth'],
        'labels': ['Employee ID', 'First Name', 'Last Name', 'Position', 'Hire Date', 'Salary', 'Department ID', 'Status', 'Phone Number', 'Address', 'Email', 'Date of Birth'],
        'primary_key': 'employee_id',
    },
    'Products': {
        'table_name': 'Products',
        'fields': ['product_id', 'name', 'description', 'category', 'price', 'stock', 'supplier_id', 'promotion_start', 'promotion_end', 'is_active', 'created_at', 'updated_at'],
        'labels': ['Product ID', 'Name', 'Description', 'Category', 'Price', 'Stock', 'Supplier ID', 'Promotion Start', 'Promotion End', 'Is Active', 'Created At', 'Updated At'],
        'primary_key': 'product_id',
    },
    'Orders': {
        'table_name': 'Orders',
        'fields': ['order_id', 'order_date', 'client_id', 'total_amount', 'status', 'shipping_address', 'shipping_date'],
        'labels': ['Order ID', 'Order Date', 'Client ID', 'Total Amount', 'Status', 'Shipping Address', 'Shipping Date'],
        'primary_key': 'order_id',
    },
    'Order_Products': {
        'table_name': 'Order_Products',
        'fields': ['order_product_id', 'order_id', 'product_id', 'quantity'],
        'labels': ['Order Product ID', 'Order ID', 'Product ID', 'Quantity'],
        'primary_key': 'order_product_id',
        'foreign_keys': {
            'order_id': 'Orders(order_id)',
            'product_id': 'Products(product_id)',
        },
    },
    'Place': {
        'table_name': 'Place',
        'fields': ['place_id', 'employee_id', 'iznos', 'datum_isplate', 'status'],
        'labels': ['Place ID', 'Employee ID', 'Amount', 'Payment Date', 'Status'],
        'primary_key': 'place_id',
    },
    'Sluzbeni_Automobili': {
        'table_name': 'Sluzbeni_Automobili',
        'fields': ['car_id', 'employee_id', 'model_automobila', 'registarski_broj', 'datum_dodjele', 'status'],
        'labels': ['Car ID', 'Employee ID', 'Car Model', 'License Plate', 'Assignment Date', 'Status'],
        'primary_key': 'car_id',
    },
    'Oprema': {
        'table_name': 'Oprema',
        'fields': ['oprema_id', 'naziv', 'tip', 'serijski_broj', 'datum_nabave', 'stanje'],
        'labels': ['Equipment ID', 'Name', 'Type', 'Serial Number', 'Purchase Date', 'Condition'],
        'primary_key': 'oprema_id',
    },
}