import datetime
class Actor:

    def __init__(self,name=None, date=None,quality=None):
        self.name = name
        self.date = datetime.date.today()
        self.quality= quality

    def __repr__(self):
        return self.__dict__.__repr__()