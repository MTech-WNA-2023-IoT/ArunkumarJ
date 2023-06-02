from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if city is None:
        return Response('Please specify a city.', status=400)

    url = 'https://api.weatherapi.com/v1/current.json?key=ff20c525398c4d97ae640555232905&q=' + city
    api_page = urlopen(url)
    api = api_page.read()
    json_api = json.loads(api)

    return Response(json.dumps(json_api), mimetype='application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
