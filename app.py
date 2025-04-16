from flask import Flask, render_template, request, session, redirect, url_for
import requests
import random
import math

app = Flask(__name__)
app.secret_key = 'AlphaBetaGamma'


COUNTRIES = requests.get('https://restcountries.com/v3.1/all').json()
COUNTRY_DICT = {
    country['name']['common']: country for country in COUNTRIES if 'latlng' in country
}
ALL_COUNTRIES = list(COUNTRY_DICT.keys())

def cartesian_distance(lat1, lon1, lat2, lon2):
    return math.sqrt((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2)

def color_scale(distance):
    if distance < 10:
        return "#ff4c4c"
    elif distance < 20:
        return "#ff944c"
    elif distance < 40:
        return "#ffe14c"
    elif distance < 80:
        return "#b4ff4c"
    else:
        return "#4c9aff"

def get_direction_arrow(lat1, lon1, lat2, lon2):
    vertical = ""
    horizontal = ""

    if lat2 > lat1:
        vertical = "↑"
    elif lat2 < lat1:
        vertical = "↓"

    if lon2 > lon1:
        horizontal = "→"
    elif lon2 < lon1:
        horizontal = "←"

    return vertical + horizontal or "•"

@app.route("/")
def home():
    if 'target' not in session:
        session['target'] = random.choice(ALL_COUNTRIES)
        session['guesses'] = []
    for guess in session['guesses']:
        if 'color' not in guess:
            guess['color'] = color_scale(guess.get('distance', 999))
    return render_template("index.html", guesses=session['guesses'], target=session['target'])

@app.route("/guess", methods=["POST"])
def guess():
    country = request.form['country']
    target = session.get('target')
    guesses = session.get('guesses', [])

    if country in COUNTRY_DICT and target in COUNTRY_DICT:
        lat1, lon1 = COUNTRY_DICT[country]['latlng']
        lat2, lon2 = COUNTRY_DICT[target]['latlng']
        distance = cartesian_distance(lat1, lon1, lat2, lon2)
        direction = get_direction_arrow(lat1, lon1, lat2, lon2)
        flag_url = COUNTRY_DICT[country]['flags']['png']

        guesses.append({
            'name': country,
            'distance': round(distance, 2),
            'color': color_scale(distance),
            'direction': direction,
            'flag': flag_url
        })
        session['guesses'] = guesses

    return redirect(url_for('home'))

@app.route("/reset")
def reset():
    session.pop('target', None)
    session.pop('guesses', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
