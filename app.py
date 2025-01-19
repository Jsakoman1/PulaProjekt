from flask import Flask, render_template, request, redirect, url_for
from tables_metadata import TABLES_METADATA  # Import metadata
from views_metadata import VIEWS_METADATA
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='34000',
        database='pulaprojekt2'
    )

@app.route('/')
def home():
    return render_template('index.html', entities=TABLES_METADATA.keys())

@app.route('/<string:entity>')
def index(entity):
    if entity not in TABLES_METADATA:
        return f"Entity '{entity}' not found.", 404
    
    metadata = TABLES_METADATA[entity]
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM {metadata['table_name']}")
    entries = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render_template('index.html', 
                           title=metadata['table_name'], 
                           entity_name=entity, 
                           entity_name_plural=entity + "s",
                           fields=[{'name': field, 'label': label, 'type': 'text', 'required': True} for field, label in zip(metadata['fields'], metadata['labels'])],
                           entries=entries,
                           table_headers=metadata['labels'],
                           table_keys=metadata['fields'],
                           primary_key=metadata['primary_key'],
                           add_url=f"/{entity}/create",
                           delete_url=f"/{entity}/delete",
                           entities=TABLES_METADATA.keys())

@app.route('/<string:entity>/create', methods=['POST'])
def create_entity(entity):
    if entity not in TABLES_METADATA:
        return f"Entity '{entity}' not found.", 404

    metadata = TABLES_METADATA[entity]
    conn = get_db_connection()
    cursor = conn.cursor()

    # Gather form data
    values = [request.form.get(field) for field in metadata['fields']]
    placeholders = ', '.join(['%s'] * len(metadata['fields']))
    query = f"INSERT INTO {metadata['table_name']} ({', '.join(metadata['fields'])}) VALUES ({placeholders})"

    try:
        cursor.execute(query, values)
        conn.commit()
    except Exception as e:
        conn.rollback()
        return f"An error occurred: {e}", 500
    finally:
        cursor.close()
        conn.close()

    return redirect(url_for('index', entity=entity))

@app.route('/<string:entity>/delete/<int:entry_id>', methods=['POST'])
def delete_entity(entity, entry_id):
    if entity not in TABLES_METADATA:
        return f"Entity '{entity}' not found.", 404

    metadata = TABLES_METADATA[entity]
    conn = get_db_connection()
    cursor = conn.cursor()

    query = f"DELETE FROM {metadata['table_name']} WHERE {metadata['primary_key']} = %s"

    try:
        cursor.execute(query, (entry_id,))
        conn.commit()
    except Exception as e:
        conn.rollback()
        return f"An error occurred: {e}", 500
    finally:
        cursor.close()
        conn.close()

    return redirect(url_for('index', entity=entity))


@app.route('/views')
def views():
    # Get all view names from VIEWS_METADATA
    return render_template('views.html', views=VIEWS_METADATA.keys())

@app.route('/views/<string:entity>')
def view(entity):
    if entity not in VIEWS_METADATA:
        return f"View '{entity}' not found.", 404
    
    metadata = VIEWS_METADATA[entity]
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM {metadata['view_name']}")
    entries = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('views.html', 
                           title=metadata['view_name'], 
                           entity_name=entity, 
                           entity_name_plural=entity + "s",
                           fields=[{'name': field, 'label': label, 'type': 'text', 'required': False} for field, label in zip(metadata['fields'], metadata['labels'])],
                           entries=entries,
                           table_headers=metadata['labels'],
                           table_keys=metadata['fields'],
                           primary_key=metadata['primary_key'])

if __name__ == '__main__':
    app.run(debug=True)
