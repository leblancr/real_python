class ObjectFactory:
    def __init__(self):
        self._builders = {}

    # put builder in local dict
    def register_builder(self, key, builder):
        self._builders[key] = builder

    # get builder out of dictionary and return it as instantiated
    def create(self, key, **kwargs):
        builder = self._builders.get(key)
        if not builder:
            raise ValueError(key)
        return builder(**kwargs)
    