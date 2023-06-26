import time
import datetime
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import re

def format_date(date_string):
    # Convert the date string to a datetime object
    date = datetime.datetime.strptime(date_string, "%Y-%m-%d")

    # Extract the day with suffix (e.g., 23rd, 1st)
    day = date.strftime("%d")
    if day.endswith(('11', '12', '13')):
        day += "th"
    elif day.endswith('1'):
        day += "st"
    elif day.endswith('2'):
        day += "nd"
    elif day.endswith('3'):
        day += "rd"
    else:
        day += "th"

    formatted_date = date.strftime(f"{day} %B")
    return formatted_date


def get_calendar_events(end_date=None):
        # Load the credentials from the JSON file you downloaded
        credentials = Credentials.from_authorized_user_file('/home/pranav125/Desktop/mycroft-core/skills/birthday-skill/credentials/google_credentials.json')

        # Build the service using the credentials
        service = build('calendar', 'v3', credentials=credentials)

        # Get the current date and time
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

        # Calculate the date for one week from now
        one_week_from_now = (datetime.datetime.utcnow() + datetime.timedelta(days=365)).isoformat() + 'Z'

        end_date = one_week_from_now
        # Call the Calendar API to retrieve the events
        events_result = service.events().list(calendarId='primary', timeMin=now, timeMax=end_date, singleEvents=True,
                                            orderBy='startTime').execute()
        events = events_result.get('items', [])
        print(events_result)
        # Create a list to store the events with dates
        events_list = []

        if not events:
            print('No upcoming events found.')
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            event_summary = event['summary']
            if event_summary.startswith('Birthday -'):
                formatted_date = format_date(start)
                name = re.sub(r'^Birthday - ', '', event_summary)
                events_list.append((formatted_date, name))
        
        # prepare a string
        return_string = "There are {} birthdays for the specified duration.\n".format(len(events_list))
        for date, name in events_list:
            return_string += f'{name} {date}.\n'

        return return_string