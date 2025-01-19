VIEWS_METADATA = {
        'ActiveClientsWithTotalOrders': {
            'view_name': 'ActiveClientsWithTotalOrders',
            'fields': ['client_id', 'client_name', 'contact_name', 'contact_phone', 'contact_email', 'total_orders', 'total_spent', 'last_order_date', 'client_status'],
            'labels': ['Client ID', 'Client Name', 'Contact Name', 'Phone', 'Email', 'Total Orders', 'Total Spent', 'Last Order Date', 'Status'],
            'primary_key': 'client_id'
        },
        'DepartmentSummary': {
            'view_name': 'DepartmentSummary',
            'fields': ['department_id', 'department_name', 'budget', 'active_employees', 'total_salary_expenditure', 'average_salary', 'budget_status'],
            'labels': ['Department ID', 'Department Name', 'Budget', 'Active Employees', 'Total Salary Expenditure', 'Average Salary', 'Budget Status'],
            'primary_key': 'department_id'
        },
        'EmployeeCarUsage': {
            'view_name': 'EmployeeCarUsage',
            'fields': ['employee_id', 'first_name', 'last_name', 'total_cars_assigned', 'car_models', 'car_registrations', 'car_statuses', 'first_car_assigned_date', 'last_car_assigned_date'],
            'labels': ['Employee ID', 'First Name', 'Last Name', 'Total Cars Assigned', 'Car Models', 'Car Registrations', 'Car Statuses', 'First Car Assigned Date', 'Last Car Assigned Date'],
            'primary_key': 'employee_id'
        },
        'ClientOrderDetails': {
            'view_name': 'ClientOrderDetails',
            'fields': ['client_id', 'client_name', 'contact_name', 'contact_phone', 'contact_email', 'total_orders', 'total_order_amount', 'products_ordered', 'suppliers'],
            'labels': ['Client ID', 'Client Name', 'Contact Name', 'Phone', 'Email', 'Total Orders', 'Total Order Amount', 'Products Ordered', 'Suppliers'],
            'primary_key': 'client_id'
        },
    }
