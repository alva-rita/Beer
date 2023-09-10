from flask import Flask, request, jsonify
import datetime
import pytz
import os

app = Flask(__name__)

# Specify the target time (UTC)
target_time = datetime.datetime(2023, 9, 10, 12, 0, 0, tzinfo=pytz.utc)

@app.route('/endpoint', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get current day of the week
    current_day = datetime.datetime.now(pytz.utc).strftime('%A')

    # Get current UTC time with validation of +/-2 minutes
    
    utc_time = datetime.datetime.now(pytz.utc)

    # Calculate the time difference in seconds
    time_diff_seconds = abs((utc_time - target_time).total_seconds())

    # Check if the time difference is within +/-2 minutes (120 seconds)
    if time_diff_seconds > 120:
        return jsonify({'error': 'Time is outside the acceptable window'}), 400
        
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
