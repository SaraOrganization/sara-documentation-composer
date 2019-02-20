import argparse
import sys
from jinja2 import Environment, FileSystemLoader
from jinja2.exceptions import TemplateNotFound

from sara.commons import serialization
from sara.domain.project import Project
from sara.domain.document import Document


class Cmd:

    def __init__(self):
        self.domain_loaded_from_samples=False
        self._setup_parser()
        self._env = None
        self._template = None

    def _setup_parser(self):
        parser = argparse.ArgumentParser(description="Cmd")

        template_group = parser.add_argument_group("templates")
        template_group.add_argument("--location",help="Template folders location",default=".")

        project_group = parser.add_argument_group("project")
        project_group.add_argument("--definition",help="Project definition file in yaml format",default=".")

        parser.add_argument("action", choices=['render','sample'])
        parser.add_argument("--template", required=True)

        self._parser = parser


    def run(self, args):
        arguments = self.configure(args)

        action_method = getattr(self, arguments.action)
        return action_method()

    def configure(self, args):
        """
        Configure command from arguments
        :param args:
        :return:
        """
        arguments = self._parser.parse_args(args=args)

        self.configure_template_runtime(arguments)
        self.configure_domain_objects(arguments)

        return arguments


    def configure_template_runtime(self, arguments):
        self._env = Environment(loader=FileSystemLoader(arguments.location))
        try:
            self._template = self._env.get_template(arguments.template)
        except TemplateNotFound as tnf:
            print(tnf,arguments.location,arguments.template)
            raise tnf


    def configure_domain_objects(self, arguments):
        self.domain_loaded_from_samples = ( arguments.action == 'sample' )
        if self.domain_loaded_from_samples :
            self._create_samples()
        else:
            self.project = serialization.load_from_yaml(Project, arguments.properties)
            self.document = serialization.load_from_yaml(Document, arguments.properties)

        self.document.configure_from_project(self.project)

    def render(self):
        args = { 'title': 'Foo',
                 'doc': self.document }
        result = self._template.render(args)
        print(result)

    def sample(self):
        self.render()

    def _create_samples(self):
        self.project = Project.sample()
        print(self.project)

        self.document = Document.sample()
        print(self.document)
        print(' - as yaml - ')
        print(serialization.to_yaml(self.document))




if __name__ == '__main__':
    cmd = Cmd()
    cmd.run(sys.argv[1:])

