from flask import Flask, render_template, request

app = Flask(__name__)

def sanitize_input(input_string):
    return input_string_replace('<', '&lt;').replace('>', '&gt;')

@app.route('/', methods=['GET', 'POST'])
def index():
    user_input = ''
    if request.method == 'POST':
        # Retrieve user input from the form
        user_input = request.form.get('user_input', '')

        # Display user input directly without proper sanitization (for demonstration purposes)
        return render_template('index.html', user_input=user_input, display_script=True)

    return render_template('index.html', user_input=user_input, display_script=False)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
