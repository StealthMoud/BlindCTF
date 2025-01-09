from flask import request, render_template, Blueprint, current_app

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/challenge', methods=['GET', 'POST'])
def challenge():
    if request.method == 'POST':
        user_input = request.form.get('input')

        # Intentional SQL Injection Vulnerability
        query = f"SELECT * FROM users WHERE username = '{user_input}'"

        try:
            connection = current_app.get_db_connection()
            cursor = connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            connection.close()

            if results:
                return f"Success! Data: {results}"
            else:
                return "No matching data found."
        except Exception as e:
            return f"Error: {str(e)}"

    return render_template('challenge.html')
