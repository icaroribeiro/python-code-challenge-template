import os


class Config:
    pass


class DevelopmentConfig(Config):
    pass


config_by_name = dict(dev=DevelopmentConfig)
