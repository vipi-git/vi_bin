from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

# Path to the JSON file where member data will be stored
json_file_path = 'data/members.json'


def save_member_data(data):
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def load_member_data():
    if not os.path.exists(json_file_path):
        return []  # Return an empty list if the file doesn't exist
    with open(json_file_path, 'r') as json_file:
        try:
            return json.load(json_file)
        except json.decoder.JSONDecodeError:
            return []  # Return an empty list if there's a decoding error


@app.route('/', methods=['GET', 'POST'])
def index():
    confirmation_message = None
    confirmation_class = None
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        schedule = request.form['schedule']  # Get the chosen schedule
        existing_members = load_member_data()
        if any(member['email'] == email for member in existing_members):
            confirmation_message = f"Registration failed. The email '{email}' is already registered."
            confirmation_class = "registration-failed"  # Set the CSS class for failed registration
        else:
            # Create a new member dictionary with the chosen schedule
            member = {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'schedule': schedule
            }

            # Add the new member to the data
            existing_members.append(member)

            # Save the updated data
            save_member_data(existing_members)

            # Set the confirmation message and CSS class for successful registration
            confirmation_message = f"Registration for {first_name} {last_name} is successful!"
            confirmation_class = "registration-success"

    return render_template('index.html', members=load_member_data(), confirmation_message=confirmation_message, confirmation_class=confirmation_class)


if __name__ == '__main__':
    app.run(debug=True)
