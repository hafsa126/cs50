from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# In-memory "database" to store rides
rides = []

# HTML templates embedded within Python (for simplicity)
home_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Carpool App</title>
</head>
<body>
    <h1>Welcome to Carpool App</h1>
    <a href="/find">Find a Ride</a> | <a href="/offer">Offer a Ride</a>
</body>
</html>
'''

find_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Find a Ride</title>
</head>
<body>
    <h1>Find a Ride</h1>
    <form method="POST" action="/find">
        <label>Origin:</label>
        <input type="text" name="origin" required>
        <label>Destination:</label>
        <input type="text" name="destination" required>
        <label>Date:</label>
        <input type="date" name="date" required>
        <button type="submit">Search</button>
    </form>

    <h2>Available Rides</h2>
    <ul>
        {% for ride in rides %}
        <li>{{ ride['origin'] }} to {{ ride['destination'] }} on {{ ride['date'] }} with {{ ride['seats'] }} seats available</li>
        {% else %}
        <li>No rides available.</li>
        {% endfor %}
    </ul>
    <br>
    <a href="/">Back to Home</a>
</body>
</html>
'''

offer_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Offer a Ride</title>
</head>
<body>
    <h1>Offer a Ride</h1>
    <form method="POST" action="/offer">
        <label>Origin:</label>
        <input type="text" name="origin" required>
        <label>Destination:</label>
        <input type="text" name="destination" required>
        <label>Date:</label>
        <input type="date" name="date" required>
        <label>Seats:</label>
        <input type="number" name="seats" required>
        <button type="submit">Post Ride</button>
    </form>
    <br>
    <a href="/">Back to Home</a>
</body>
</html>
'''

# Home route


@app.route('/')
def home():
    return render_template_string(home_template)

# Find a ride route


@app.route('/find', methods=['GET', 'POST'])
def find():
    if request.method == 'POST':
        origin = request.form.get('origin')
        destination = request.form.get('destination')
        date = request.form.get('date')

        # Search for matching rides
        matching_rides = [ride for ride in rides if ride['origin'] ==
                          origin and ride['destination'] == destination and ride['date'] == date]
        return render_template_string(find_template, rides=matching_rides)

    return render_template_string(find_template, rides=[])

# Offer a ride route


@app.route('/offer', methods=['GET', 'POST'])
def offer():
    if request.method == 'POST':
        # Get ride information from the form
        ride = {
            'origin': request.form.get('origin'),
            'destination': request.form.get('destination'),
            'date': request.form.get('date'),
            'seats': request.form.get('seats')
        }
        # Add ride to "database"
        rides.append(ride)
        return redirect(url_for('home'))

    return render_template_string(offer_template)


if __name__ == '_main_':
    app.run(debug=True)
