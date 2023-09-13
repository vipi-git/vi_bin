from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store survey responses in a list (you may use a database for a real application)
survey_responses = []

@app.route('/', methods=['GET', 'POST'])
def survey():
    thank_you_message = None
    
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        tasks = [
            request.form.get('task1'),
            request.form.get('task2'),
            request.form.get('task3')
        ]

        # Create a dictionary to store survey responses
        response = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'tasks': tasks
        }

        # Append the response to the list
        survey_responses.append(response)

        # Set the thank you message
        thank_you_message = 'Thanks for Participating in the Survey!'

    return render_template('survey.html', thank_you_message=thank_you_message)

if __name__ == '__main__':
    app.run(debug=True)