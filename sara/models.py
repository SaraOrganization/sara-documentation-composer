import related

@related.mutable
class Project:
    name = related.StringField()
    long_name = related.StringField()
    version = related.StringField(default="0.0.1")

    @staticmethod
    def sample():
        return Project(name='My Project',long_name='My very precious project about stars')


@related.mutable
class Agent:
    name = related.StringField()
    role = related.StringField(required=False)

@related.mutable
class Action:
    name = related.StringField()
    description = related.StringField()
    role = related.StringField(required=False)
    date = related.DateField(required=False)

@related.mutable
class Issue:
    id = related.StringField()
    description = related.StringField()
    date = related.DateField()
    comment = related.StringField(required=False)
    page = related.SetField(str,required=False)


@related.mutable
class Document:
    title = related.StringField(required=True)
    version = related.StringField(required=False)
    date = related.DateField(required=False)
    reference = related.StringField(required=False)
    custodian = related.ChildField(Agent, required=False)
    preparations = related.SequenceField(Action, required=False)
    contributions = related.SequenceField(Action, required=False)
    approbations = related.SequenceField(Action, required=False)
    issues = related.SequenceField(Issue, required=False)
    title_template = related.StringField(default="Document about {name}", required=False)


    def configure_from_project(self, project):
        self.title = self.title_template.format(name=project.name)

    @staticmethod
    def sample():
        d = Document("document title")
        d.version = "1.0"
        d.reference = "REC-FOO-A"
        d.custodian = "mister.custodian"
        
        d.preparations.append(Action(name='John Doe',role='Leader', description='Preparation of review',date='2019-01-01'))
        
        d.contributions= [
            Action(name='John Doe', role='Leader', description='Preparation of review', date='2019-01-01'),
            Action(name='John Doe', role='Leader', description='Preparation of review', date='2019-01-01'),
            Action(name='John Doe', role='Leader', description='Preparation of review', date='2019-01-01')]

        d.approbations.append(Action(name='John Doe',role='Leader', description='Preparation of review',date='2019-01-01'))

        d.issues = [
            Issue(id='0.1',date='2018-11-01',page=["2"],description='Typo',comment='file to view the source code until proper documentation is generated.'),
            Issue(id='0.2', date='2018-11-01', page=["2"], description='Typo very long', comment='balbalbalbalbalb'),
            Issue(id='0.3', date='2018-11-01', page=["2","3"], description='Typo', comment='datetime field formatted using formatter.'),
            Issue(id='0.4', date='2018-11-01', page=["2"], description='Typo', comment='balbalbalbalbalb'),
            Issue(id='0.5', date='2018-11-01', page=["2"], description='Typo', comment='Adding your own field types is fairly straightforward '),
        ]

        return d