

class HTML(object):

    def __init__(self):
        pass

    def __str__(self):
        pass

    def _join(self):
        pass

    def add(self):
        pass

    def attr(self):
        pass


class Element(HTML):

    def __init__(self, single=False):
        super(Element, self).__init__()
        self.attrs = {}
        self.single = single
        self.content = None

    def __str__(self):
        pass

    def update_attrs(self, attrs={}):
        self.attrs.update(attrs)

    def is_single(self):
        return self.single


class Table(HTML):

    def __init__(self):
        super(Table, self).__init__()

    def add_column(self):
        pass

    def add_row(self):
        pass

    def make_table(self, obj):
        if isinstance(obj, list):
            self._make_table_from_list(obj)
        elif isinstance(obj, dict):
            self._make_table_from_dict(obj)

    def _make_table_from_list(self, l):
        pass

    def _make_table_from_dict(self, d):
        pass



