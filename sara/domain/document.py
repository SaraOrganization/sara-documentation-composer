import related


class Document:
    @related.mutable
    class Document:
        title = related.StringField(required=True)
        version = related.StringField(required=False)
        date = related.DateField(required=False)
        reference = related.StringField(required=False)
        custodian = related.ChildField(Agent, required=False)
        preparators = related.SequenceField(Agent, required=False)
        title_template = related.StringField(default="Document about {name}", required=False)


    @classmethod
    def load_from_dictionary(cls,obj=None):
        subject = obj if obj else Document()







    def configure_from_project(self, project):
        self.title = self.title_template.format(name=project.name)
        pass

    @classmethod
    def sample(cls):
        d = Document()
        d.title = "document title"
        d.version = "1.0"
        d.reference = "REC-FOO-A"
        d.custodian = "mister.custodian"
        d.preparators.append(Actor(name='John Doe',quality='Leader'))
        return d

    def __repr__(self):
        return self.__dict__.__repr__()
