from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/departures/<departure>/")
def render_departure(departure):
    return render_template('departure.html')


@app.route("/tours/<id>/")
def render_tours(tour_id):
    return render_template('tour.html')


if __name__ == '__main__':
    app.run()
