from flask import Flask, request, render_template_string

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        
        # Basic error handling
        if not name or not age or not age.isdigit():
            return "Invalid input. Please enter a valid name and numeric age.", 400
        
        return f"Hello, {name}! You are {age} years old."
    
    # HTML form
    html_form = '''
        <form method="POST">
            Name: <input type="text" name="name"><br>
            Age: <input type="text" name="age"><br>
            <input type="submit" value="Submit">
        </form>
    '''
    return render_template_string(html_form)

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=5000)