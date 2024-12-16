# this is the main file for the application. Sometimes it's named 'main'.
# better to have a main python files that calls modules that I've created.
# this request access incoming HTTP request data
from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)


@app.route('/')  # this defines the home page
# this defines how the page below called "index" can be accessed. tells Flask where to go to access the web page.
@app.route('/index')
# this defines/creates a page called index. Pages that are going to be defined go in this area.
def index():
    return render_template('index.html')   # can put inline HTML in this string


@app.route('/weather')
def get_weather():
    # i think this is the value passed from the client
    # get is insecure method to get info from backend. POST is more secure and sends encrypted info. Info isn't stored on the web server.
    city = request.args.get('city')
    # the above value that is recieved from the client (form on the web page) is then passed to the python function/module for processing.

    if not bool(city.strip()):
        # not inverts the Bool value. So if True (ie: empty space), it defaults to the value of "Kansas City".
        city = "Kansas City"

    weather_data = get_current_weather(city)

    # City is not bound by API
    if not weather_data['cod'] == 200:
        return render_template('city-not-found.html')

    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}"
    )


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
