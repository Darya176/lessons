class Animal():
    def __init__(self, type, voice):
        self.type = type
        self.voice = voice

    def print_voice(self):
        print(self.voice)

egnyat = Animal('Барящик', 'Кушоц хочеца')
egnyat.print_voice()
print(egnyat.type)
katikovka = Animal('Птичка', 'Ку')
print(katikovka.type)
katikovka.print_voice()