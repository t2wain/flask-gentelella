class Config(object):
    SECRET_KEY = 'key'


class ProductionConfig(Config):
    pass
    # DEBUG = False


class DebugConfig(Config):
    pass
    # DEBUG = True


class GAEConfig(Config):
    pass
    # DEBUG = False
