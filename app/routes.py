from flask import request, render_template, Blueprint, current_app, jsonify

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/items')
def items():
    # Render the page to display items (availability status shown dynamically)
    return render_template('items.html')

@main.route('/get_item', methods=['GET'])
def get_item():
    # Get the 'id' parameter from the query string
    item_id = request.args.get('id')

    if not item_id:
        return jsonify({"error": "Missing 'id' parameter"}), 400

    # Intentional SQL Injection Vulnerability
    query = f"SELECT status FROM items WHERE id = {item_id}"

    try:
        # Connect to the database
        connection = current_app.get_db_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchone()  # Fetch a single row
        connection.close()

        if result:
            # Return the status (e.g., 'available', 'not available')
            return jsonify({"result": result[0]})
        else:
            # Item does not exist
            return jsonify({"result": "not available"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@main.route('/test_db')
def test_db():
    try:
        connection = current_app.get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT 1")  # Basic query to test connection
        connection.close()
        return "Database connection successful!"
    except Exception as e:
        return f"Database connection failed: {str(e)}"

