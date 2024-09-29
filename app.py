import datetime

from flask import Flask, render_template, redirect

app = Flask(__name__)


def calculate_updated_values():
    # Calculate time difference from base time
    base_time = datetime.datetime(2024, 9, 29, 0, 0, 1)
    initial_solar_homes = 600000
    initial_co2_saved = 1200000000  # kg of CO2 saved
    initial_energy_generated = 3000000000  # Wh generated

    # Increments per second
    solar_homes_increment_per_sec = 0.019
    co2_saved_increment_per_sec = 38
    energy_generated_increment_per_sec = 95000
    time_diff = datetime.datetime.now() - base_time
    total_seconds = time_diff.total_seconds()

    # Calculate updated values based on increments
    updated_solar_homes = initial_solar_homes + (solar_homes_increment_per_sec * total_seconds)
    updated_co2_saved = initial_co2_saved + (co2_saved_increment_per_sec * total_seconds)
    updated_energy_generated = initial_energy_generated + (energy_generated_increment_per_sec * total_seconds)
    print(updated_energy_generated,updated_co2_saved,updated_solar_homes)
    return {
        'solar_homes': int(updated_solar_homes),
        'co2_saved': int(updated_co2_saved),
        'energy_generated': int(updated_energy_generated)
    }


@app.route('/')
def index():

    return redirect("/home")


@app.route("/home")
def home():
    counter_values = calculate_updated_values()
    return render_template("index.html", counter_values=counter_values)


@app.route("/market")
def market():
    return render_template("market.html")


@app.route("/sdg")
def sdg():
    # The base timestamp to calculate the difference from when the values were last updated

    counter_values = calculate_updated_values()
    return render_template("sdg.html")


@app.route("/grid")
def grid():
    # this doesn't exist, so they will be rerouted to home page
    return render_template("grid.html")


if __name__ == '__main__':
    app.run(debug=True)
