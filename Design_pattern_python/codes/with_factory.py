import form as form

from abc import ABC, abstractmethod


class LanguageLocalizer(ABC):
    def localize(self):
        pass


class FrenchLocalizer(LanguageLocalizer):

    def __init__(self):
        self.translations = {"car": "voiture", "bike": "bicyclette",
                             "cycle": "cyclette"}

    def localize(self, msg):
        return self.translations.get(msg, msg)


class SpanishLocalizer(LanguageLocalizer):
    """it simply returns the spanish version"""

    def __init__(self):
        self.translations = {"car": "coche", "bike": "bicicleta",
                             "cycle": "ciclo"}

    def localize(self, msg):
        """change the message using translations"""
        return self.translations.get(msg, msg)


class EnglishLocalizer(LanguageLocalizer):
    """Simply return the same message"""

    def localize(self, msg):
        return msg


class Factory(ABC):
    def create(self):
        pass


class ConcreteFactory(Factory):
    def create(self, language="English"):
        """Factory Method"""
        localizers = {
            "French": FrenchLocalizer,
            "English": EnglishLocalizer,
            "Spanish": SpanishLocalizer,
        }

        return localizers[language]()


if __name__ == "__main__":
    obj = ConcreteFactory()
    f = obj.create("French")
    e = obj.create("English")
    s = obj.create("Spanish")

    message = ["car", "bike", "cycle"]

    for msg in message:
        print(f.localize(msg))
        print(e.localize(msg))
        print(s.localize(msg))
