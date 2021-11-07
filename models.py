import enum

from app import db


class Airplane(db.Model):
    __tablename__ = 'airplane'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    total_flight_count = db.Column(db.Integer)
    airline = db.Column(db.String())
    info = db.Column(db.String())
    flights = db.relationship('Flight', backref='airplane', uselist=True, lazy=True)

    def __init__(self, name, total_flight_count, airline, info):
        self.name = name
        self.total_flight_count = total_flight_count
        self.airline = airline
        self.info = info

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'total_flight_count': self.total_flight_count,
            'airline': self.airline,
            'info': self.info
        }


class Flight(db.Model):
    __tablename__ = 'flight'

    class FlightStatusEnum(enum.Enum):
        NOT_STARTED = 'not-started'
        IN_PROGRESS = 'in-progress'
        ENDED = 'ended'

    id = db.Column(db.Integer, primary_key=True)
    airport_start = db.Column(db.String())
    airport_end = db.Column(db.String())
    airplane_speed = db.Column(db.Integer)
    status = db.Column(
        db.Enum(FlightStatusEnum),
        default=FlightStatusEnum.NOT_STARTED,
        nullable=False
    )
    airplane_id = db.Column(db.Integer, db.ForeignKey('airplane.id'), nullable=False)

    def __init__(self, airport_start, airport_end, airplane_speed, status, airplane_id):
        self.airport_start = airport_start
        self.airport_end = airport_end
        self.airplane_speed = airplane_speed
        self.status = status
        self.airplane_id = airplane_id

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'airport_start': self.airport_start,
            'airplane_speed': self.airplane_speed,
            'status': self.status.value,
            'airplane_id': self.airplane_id,
        }
