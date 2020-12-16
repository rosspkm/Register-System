class Type:
    def __init__(self):
        self._Type = None

    # function to get value of _name
    def get_type(self):
        return self._Type
    # function to set value of _name

    def set_type(self, name):
        self._Type = name

    age = property(get_type, set_type)


class Name:
    def __init__(self):
        self._name = None

    # function to get value of _name
    def get_name(self):
        return self._name
    # function to set value of _name

    def set_name(self, name):
        self._name = name

    age = property(get_name, set_name)


class Key:
    def __init__(self):
        self._Key = None

    # function to get value of _name
    def get_key(self):
        return self._Key
    # function to set value of _name

    def set_key(self, name):
        self._Key = name

    age = property(get_key, set_key)