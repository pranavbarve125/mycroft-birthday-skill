from mycroft import MycroftSkill, intent_file_handler


class Birthday(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('birthday.intent')
    def handle_birthday(self, message):
        self.speak_dialog('birthday')


def create_skill():
    return Birthday()

