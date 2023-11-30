class FieldTracker:

    def __init__(self):
        initial_values = dict(self.__dict__)
        self.initial_values = initial_values

    def base(self, key):
        return self.initial_values.get(key)

    def has_changed(self, key):
        return not getattr(self, key) == self.initial_values.get(key)

    def changed(self):
        changed_attrs = {}
        for key, value in self.initial_values.items():
            if self.__dict__[key] != value:
                changed_attrs[key] = value
        return changed_attrs

    def save(self):
        result_dict = {}
        for key in self.initial_values:
            result_dict[key] = self.__dict__[key]
        self.initial_values = result_dict
