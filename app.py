from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock database (in-memory for simplicity)
rides = []

# Home route


@app.route('/')
def home():
    return render_template('index.html')

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
        return render_template('find.html', rides=matching_rides)
    return render_template('find.html', rides=[])

# Offer a ride route


@app.route('/offer', methods=['GET', 'POST'])
def offer():
    if request.method == 'POST':
        ride = {
            'origin': request.form.get('origin'),
            'destination': request.form.get('destination'),
            'date': request.form.get('date'),
            'seats': request.form.get('seats')
        }
        rides.append(ride)
        return redirect(url_for('home'))
    return render_template('offer.html')


if __name__ == '_main_':
    app.run(debug=True)
