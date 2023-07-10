import time
import datetime
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import re


class GoogleCalendar:
    def __init__(self):
        # Load the credentials from the JSON file you downloaded
        credentials = Credentials.from_authorized_user_file('/home/pranav125/Desktop/mycroft-core/skills/birthday-skill/credentials/google_credentials.json')

        # Build the service using the credentials
        self.service = build('calendar', 'v3', credentials=credentials)

    def format_date(self, date_string):
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


    def get_calendar_events_for_a_duration(self, duration_entity):
        # Get the current date and time
        current_date = datetime.datetime.utcnow()#.isoformat() + 'Z'  # 'Z' indicates UTC time

        # Calculate the date for one week from now

        if duration_entity == "week":
            end_date = current_date + datetime.timedelta(weeks=1)
        elif duration_entity == "month":
            end_date = current_date + datetime.timedelta(days=30)
        elif duration_entity == "today":
            end_date = current_date
        elif duration_entity == "tomorrow":
            end_date = current_date + datetime.timedelta(days=1)

        formatted_current_date = current_date.isoformat() + 'Z'
        formatted_end_date = end_date.isoformat() + 'Z'

        # Call the Calendar API to retrieve the events
        events_result = self.service.events().list(calendarId='primary', timeMin=formatted_current_date, timeMax=formatted_end_date, singleEvents=True,
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
                formatted_date = self.format_date(start)
                name = re.sub(r'^Birthday - ', '', event_summary)
                events_list.append((formatted_date, name))
        
        return events_list