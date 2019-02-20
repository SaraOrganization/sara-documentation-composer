class Project:
    """
    Project class
    """
    def __init__(self):
        self.name = None
        self.version = None
        self.long_name = None

    @classmethod
    def sample(cls):
        p = Project()
        p.name = 'SHORT-NAME'
        p.long_name = 'A pretty Long for project named SHORT-NAME'
        p.version = '1.0.1'
        return p

    def __repr__(self):
        return self.__dict__.__repr__()


