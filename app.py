from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',  # MySQL host
        user='root',  # MySQL username
        password='34000',  # MySQL password
        database='pulaprojekt2'  # Database name
    )
    return connection

app = Flask(__name__)

# Home route (root)
@app.route('/')
def home():
    return render_template('index.html')  # Render a home page template

# Clients Routes
@app.route('/clients')
def index_clients():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM Clients')
    clients = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('clients.html', clients=clients)

@app.route('/clients/create', methods=['POST'])
def create_client():
    name = request.form['name']
    contact_name = request.form['contact_name']
    contact_phone = request.form['contact_phone']
    contact_email = request.form['contact_email']
    address = request.form['address']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Clients (name, contact_name, contact_phone, contact_email, address)
        VALUES (%s, %s, %s, %s, %s)
    ''', (name, contact_name, contact_phone, contact_email, address))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index_clients'))


@app.route('/clients/delete/<int:client_id>', methods=['POST'])
def delete_client(client_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Clients WHERE client_id = %s', (client_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index_clients'))

# Employees Routes
@app.route('/employees')
def index_employees():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM Employees')
    employees = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('employees.html', employees=employees)


@app.route('/employees/create', methods=['GET', 'POST'])
def create_employee():
    if request.method == 'POST':
        # Safely get values from form fields, defaulting to None if empty
        first_name = request.form.get('first_name', None) or None
        last_name = request.form.get('last_name', None) or None
        position = request.form.get('position', None) or None
        hire_date = request.form.get('hire_date', None) or None
        salary = request.form.get('salary', None) or None
        department_id = request.form.get('department_id', None) or None
        status = request.form.get('status', None)  # If empty, it will be None
        if status == "":  # Explicitly set empty string to None for ENUM fields
            status = None
        phone_number = request.form.get('phone_number', None) or None
        address = request.form.get('address', None) or None
        email = request.form.get('email', None) or None
        date_of_birth = request.form.get('date_of_birth', None) or None

        # Ensure required fields are provided
        if not first_name or not last_name:
            return "First name and last name are required", 400
        
        # Proceed with the database insertion
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Employees (first_name, last_name, position, hire_date, salary, department_id, status,
                                   phone_number, address, email, date_of_birth)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (first_name, last_name, position, hire_date, salary, department_id, status, phone_number, address, email, date_of_birth))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('index_employees'))
    
    return render_template('create_employee.html')

@app.route('/employees/delete/<int:employee_id>', methods=['POST'])
def delete_employee(employee_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Employees WHERE employee_id = %s', (employee_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index_employees'))

# Suppliers Routes
@app.route('/suppliers')
def index_suppliers():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM Suppliers')
    suppliers = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('suppliers.html', suppliers=suppliers)

@app.route('/suppliers/create', methods=['POST'])
def create_supplier():
    name = request.form['name']
    contact_name = request.form['contact_name']
    contact_phone = request.form['contact_phone']
    contact_email = request.form['contact_email']
    address = request.form['address']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Suppliers (name, contact_name, contact_phone, contact_email, address)
        VALUES (%s, %s, %s, %s, %s)
    ''', (name, contact_name, contact_phone, contact_email, address))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index_suppliers'))

@app.route('/suppliers/delete/<int:supplier_id>', methods=['POST'])
def delete_supplier(supplier_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Suppliers WHERE supplier_id = %s', (supplier_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index_suppliers'))

if __name__ == '__main__':
    app.run(debug=True)