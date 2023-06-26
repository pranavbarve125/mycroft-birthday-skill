from mycroft import MycroftSkill, intent_file_handler
import re

from .google_calendar_api import get_calendar_events

class Birthday(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.txt = ""
        
    @intent_file_handler('duration.intent')
    def handle_birthday(self, message):
        duration_entity = message.data.get('duration')
        date_entity = date_entity = message.data.get('date')
        
        self.txt = get_calendar_events()
        
        self.speak(self.txt)


def create_skill():
    return Birthday()