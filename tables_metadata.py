# tables_metadata.py
TABLES_METADATA = {
    'clients': {
        'table_name': 'Clients',
        'primary_key': 'client_id',
        'fields': ['name', 'contact_name', 'contact_phone', 'contact_email', 'address'],
        'labels': ['Name', 'Contact Name', 'Phone', 'Email', 'Address'],
    },
    'employees': {
        'table_name': 'Employees',
        'primary_key': 'employee_id',
        'fields': ['first_name', 'last_name', 'position', 'hire_date', 'salary'],
        'labels': ['First Name', 'Last Name', 'Position', 'Hire Date', 'Salary'],
    },
    'suppliers': {
        'table_name': 'Suppliers',
        'primary_key': 'supplier_id',
        'fields': ['name', 'contact_name', 'contact_phone', 'contact_email', 'address'],
        'labels': ['Name', 'Contact Name', 'Phone', 'Email', 'Address'],
    },
}
