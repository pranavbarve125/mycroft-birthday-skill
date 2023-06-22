from mycroft import MycroftSkill, intent_file_handler
from mycroft.skills.api import SkillApi
import time

class Birthday(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.txt = ""
        
    @intent_file_handler('birthday.intent')
    def handle_birthday(self, message):
        duration = message.data.get('duration')
        
        with open('/home/pranav125/Desktop/mycroft-core/skills/birthday-skill/morning.txt', 'r') as f:
            self.txt = str(f.read())
        
        self.speak(self.txt)

def create_skill():
    return Birthday()