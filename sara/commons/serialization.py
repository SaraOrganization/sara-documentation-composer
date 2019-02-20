"""
module for serialization.
"""

import yaml

def load_from_dict(class_name, data):
    """
    Load a instance from a dictionary
    :param class_name:
    :param data:
    :return:
    """
    obj = class_name()
    obj.__dict__.update(data)
    return obj

def write_to_dict(obj, data):
    return obj.__dict__


def load_from_yaml(class_name, file_location) :
    """
    Load from a yaml file.
    Yaml content could be a dump or a pure yaml
    :param class_name:
    :param file_location:
    :return:
    """
    with open(file_location, 'r') as file:
        data = yaml.load(file)

        if isinstance(data, class_name) :
            return data

        return load_from_dict(class_name, data)

def write_to_yaml(obj, file_location):
    with open(file_location, 'w') as file:
        yaml.dump(obj,file)

def to_yaml(obj):
    return yaml.dump(obj,default_flow_style=False)
