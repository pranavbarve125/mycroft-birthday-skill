from mycroft import MycroftSkill, intent_file_handler
from mycroft.skills.api import SkillApi
import re

from .google_calendar_api import GoogleCalendar

class Birthday(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.txt = ""
        self.gc = GoogleCalendar()
        self.tele = SkillApi.get('telegram.luke5sky')
        
    @intent_file_handler('duration.intent')
    def handle_birthdays_duration(self, message): # week, month, tommorrow, today
        duration_entity = message.data.get('duration')
        self.txt = self.gc.get_calendar_events_for_a_duration(duration_entity)
        self.speak(self.txt)
        msg = 'works'
        self.speak(self.tele.sendTelegramMessage(msg))

    def handle_birthdays_date(self, message):
        date_entity = date_entity = message.data.get('date')

def create_skill():
    return Birthday()