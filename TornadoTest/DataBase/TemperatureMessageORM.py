from sqlalchemy.ext.declarative import declarative_base

import sqlalchemy as sa

Base = declarative_base()


class TemperatureMessage(Base):
    __tablename__ = 'temperature_message'

    topic = sa.Column('topic', sa.String, primary_key=True)
    temperature = sa.Column('temperature', sa.Float)
    unread = sa.Column('unread', sa.Boolean)

    def __init__(self, temperature):
        self.temperature = temperature
        self.unread = True

    def __repr__(self):
        return "<temperature_message({}, {})>".format(self.temperature, self.unread)

conn = sa.create_engine('sqlite:///home.db')
