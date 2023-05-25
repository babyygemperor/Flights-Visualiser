from datetime import datetime
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flights.db'
db = SQLAlchemy(app)


class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flight_number = db.Column(db.String(200), nullable=False)
    airlines = db.Column(db.String(200), nullable=False)
    aircraft_type = db.Column(db.String(200), nullable=False)
    registration_code = db.Column(db.String(200), nullable=False)
    departure_airport = db.Column(db.String(200), nullable=False)
    destination_airport = db.Column(db.String(200), nullable=False)
    scheduled_departure = db.Column(db.DateTime, nullable=False)
    scheduled_arrival = db.Column(db.DateTime, nullable=False)
    actual_departure_time = db.Column(db.DateTime, nullable=False)
    actual_arrival_time = db.Column(db.DateTime, nullable=False)
    cost = db.Column(db.Float, nullable=False)
    distance_travelled = db.Column(db.Float, nullable=False)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        flight = Flight(
            flight_number=request.form['number'],
            airlines=request.form['number'][:2],
            aircraft_type='MODEL',
            registration_code='D-1234',
            departure_airport=request.form['departure'],
            destination_airport=request.form['destination'],
            scheduled_departure=datetime.strptime(request.form['scheduledDeparture'], '%Y-%m-%dT%H:%M'),
            scheduled_arrival=datetime.strptime(request.form['scheduledArrival'], '%Y-%m-%dT%H:%M'),
            actual_departure_time=datetime.strptime(request.form['actualDeparture'], '%Y-%m-%dT%H:%M'),
            actual_arrival_time=datetime.strptime(request.form['actualArrival'], '%Y-%m-%dT%H:%M'),
            cost=float(request.form['cost']),
            distance_travelled=float(request.form['distance'])
        )
        try:
            db.session.add(flight)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(e)
            return "There was an issue adding your flight"
    else:
        flights = Flight.query.order_by(Flight.id).all()
        for flight in flights:
            flight.duration = (flight.actual_arrival_time - flight.actual_departure_time).total_seconds() / 3600
            flight.total_delay = (flight.actual_arrival_time - flight.scheduled_arrival).total_seconds() / 3600
        return render_template('index.html', flights=flights)


@app.route('/delete/<int:id>')
def delete(id):
    flight_to_delete = Flight.query.get_or_404(id)

    try:
        db.session.delete(flight_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "There was a problem deleting the flight."


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    flight = Flight.query.get_or_404(id)

    if request.method == 'POST':
        flight.flight_number = request.form['number']
        flight.airlines = request.form['number'][:2]
        flight.aircraft_type = 'MODEL'
        flight.registration_code = 'D-123'
        flight.departure_airport = request.form['departure']
        flight.destination_airport = request.form['destination']
        flight.scheduled_departure = datetime.strptime(request.form['scheduledDeparture'], '%Y-%m-%dT%H:%M')
        flight.scheduled_arrival = datetime.strptime(request.form['scheduledArrival'], '%Y-%m-%dT%H:%M')
        flight.actual_departure_time = datetime.strptime(request.form['actualDeparture'], '%Y-%m-%dT%H:%M')
        flight.actual_arrival_time = datetime.strptime(request.form['actualArrival'], '%Y-%m-%dT%H:%M')
        flight.cost = float(request.form['cost'])
        flight.distance_travelled = float(request.form['distance'])

        try:
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return "There was an issue updating your flight"


@app.route('/reset_db')
def reset_db():
    try:
        num_rows_deleted = db.session.query(Flight).delete()
        db.session.commit()
        return "Deleted {} record(s).".format(num_rows_deleted)
    except:
        return "There was a problem resetting the database."


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)
