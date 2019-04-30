class Logger:
    singleton = None
    @classmethod
    def get_instance(cls):
        if cls.singleton is None:
            cls.singleton = Logger()
            print('creating a logger...')
        return cls.singleton
