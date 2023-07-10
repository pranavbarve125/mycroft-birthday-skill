from mycroft import MycroftSkill, intent_file_handler
from mycroft.skills.api import SkillApi
import re

from .google_calendar_api import GoogleCalendar

class Birthday(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.txt = ""
        self.events = ""
        self.gc = GoogleCalendar()
        self.tele = SkillApi.get('telegram.luke5sky')

        # self.scheduler = BackgroundScheduler()
        # self.scheduler.add_job(self.read_daily_birthdays, 'cron', hour='9,15,21', minute='0,30')

    def initialize(self):
        self.scheduler.start()

    def read_morning_script(self):
        self.txt = self.gc.get_calendar_events_for_a_duration("today")
        
        if self.txt == "Please specify correct duration.":
            return
        
        self.speak(self.txt)
        self.tele.sendTelegramMessage(self.txt)

    def read_afternoon_evening_script(self):
        self.txt = self.gc.get_calendar_events_for_a_duration("today")
        
        if self.txt == "Please specify correct duration.":
            return
        
        self.speak(self.txt)
        self.tele.sendTelegramMessage(self.txt)
        
    @intent_file_handler('duration.intent')
    def handle_birthdays_duration(self, message): # week, month, tommorrow, today
        duration_entity = message.data.get('duration')
        self.events = self.gc.get_calendar_events_for_a_duration(duration_entity)

        # prepare a string
        self.txt = "There are {} birthday(s) for the specified duration.\n".format(len(self.events))
        for date, name in self.events:
            self.txt += f'{name} {date}.\n'

        self.speak(self.txt)
        msg = 'works'
        self.speak(self.tele.sendTelegramMessage(msg))

    def handle_birthdays_date(self, message):
        date_entity = date_entity = message.data.get('date')

def create_skill():
    return Birthday()