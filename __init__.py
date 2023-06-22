from mycroft import MycroftSkill, intent_file_handler


class Fart(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('fart.intent')
    def handle_fart(self, message):
        self.speak_dialog('fart')


def create_skill():
    return Fart()

