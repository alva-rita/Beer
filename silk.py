from flask import Flask, request, jsonify
import datetime
import pytz
import os

silk = Flask(__name__)

@silk.route('/endpoint', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get current day of the week
    current_day = datetime.datetime.now(pytz.utc).strftime('%A')

    # Get current UTC time with validation of +/-2 hours
    utc_time = datetime.datetime.now(pytz.utc)
    utc_time_validated = utc_time.strftime('%Y-%m-%d %H:%M:%S')

    # Get GitHub URLs
    github_url_file = 'https://github.com/alva-rita/Beer/blob/main/silk.py'
    github_url_source = 'https://github.com/alva-rita/Beer'

    # Create the response JSON
    response_data = {
        'slack_name': slack_name,
        'current_day': current_day,
        'current_utc_time': utc_time_validated,
        'track': track,
        'github_url_file': github_url_file,
        'github_url_source': github_url_source,
        'status_code': 'Success'
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
