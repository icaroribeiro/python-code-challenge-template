class Config:
    pass


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/testdb"


config_by_name = dict(dev=DevelopmentConfig)
