from apscheduler.schedulers.background import BackgroundScheduler
from mycroft import MycroftSkill, intent_file_handler
from mycroft.skills.api import SkillApi
import time

import re

from .google_calendar_api import GoogleCalendar

class Birthday(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.txt = ""
        self.gc = GoogleCalendar()
        self.tele = SkillApi.get('telegram.luke5sky')

        self.scheduler = BackgroundScheduler()
        self.scheduler.add_job(self.read_daily_birthdays, 'cron', hour='9,15,21', minute='0,30')

    def initialize(self):
        self.scheduler.start()

    def read_daily_birthdays(self):
        self.txt = self.gc.get_calendar_events_for_a_duration("today")
        
        if self.txt == "Please specify correct duration.":
            return
        
        self.speak(self.txt)
        self.tele.sendTelegramMessage(self.txt)
        
    @intent_file_handler('duration.intent')
    def handle_birthdays_duration(self, message): # week, month, tommorrow, today
        duration_entity = message.data.get('duration')
        self.txt = self.gc.get_calendar_events_for_a_duration(duration_entity)
        self.speak(self.txt)
        # self.tele.sendTelegramMessage(self.txt)
        # self.speak(self.tele.sendTelegramMessage(msg))

def create_skill():
    return Birthday()
    