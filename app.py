from flask import Flask, render_template
import data


app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/departures/<departure>/")
def render_departure(departure):
    return render_template('departure.html')


@app.route("/tours/<id>/")
def render_tours(id):
    return render_template('tour.html')


@app.route("/data/")
def main_data():
    print(data.tours[1]["country"])
    return render_template('data.html', tours=data.tours)


@app.route("/data/departures/<departure>/")
def data_departure(departure):
    return render_template('data_departures.html', tours=data.tours)


@app.route("/data/tours/<id>/")
def data_tours(id):
    tour_id = int(id)
    country = data.tours[tour_id]["country"]
    hotel = data.tours[tour_id]["title"]
    price = data.tours[tour_id]["price"]
    duration = data.tours[tour_id]["nights"]
    description = data.tours[tour_id]["description"]
    print(country)
    return render_template('data_tours.html', country=country, hotel=hotel, price=price, duration=duration,
                           description=description)


if __name__ == '__main__':
    app.run()
