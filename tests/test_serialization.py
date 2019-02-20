from sara.commons import serialization


class Foo:
    def issues_as_key(self):
        return '-'.join(self.issues)

def check_obj(obj):
    assert isinstance(obj, Foo)
    assert obj.issues == ['a','b']
    assert obj.issues_as_key() == 'a-b'


def test_load_from_dict():
    # --Given--
    data = {'name': 'Foo', 'issues': ['a', 'b']}

    # --When--
    obj = serialization.load_from_dict(Foo, data)

    # --Then--
    check_obj(obj)


def test_load_from_yaml(tmpdir):
    # --Given--
    path = tmpdir.join('test.yaml')
    path.write("{'name': 'Foo', 'issues': ['a', 'b']}")

    # --When--
    obj = serialization.load_from_yaml(Foo, path)

    # --Then--
    check_obj(obj)

def test_write_to_yaml(tmpdir):
    # --Given--
    path = tmpdir.join('test.yaml')

    foo = Foo()
    foo.issues = ['a', 'b']

    # --When--
    serialization.write_to_yaml(foo, path)

    obj = serialization.load_from_yaml(Foo, path)

    # --Then--
    assert path.read().startswith('!!python/object:test_serialization.Foo')
    check_obj(obj)