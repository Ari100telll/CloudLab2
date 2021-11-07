from app import db
from app import app
from models import Flight, Airplane
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


@app.route("/addAirplain", methods=['POST'])
def add_airplane():
    name = request.args.get('name')
    total_flight_count = request.args.get('total_flight_count')
    airline = request.args.get('airline')
    info = request.args.get('info')
    try:
        airplane = Airplane(
            name=name,
            total_flight_count=total_flight_count,
            airline=airline,
            info=info,
        )
        db.session.add(airplane)
        db.session.commit()
        response = jsonify()
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return (str(e))


@app.route("/getallAirplain", methods=['GET'])
def get_all_airplanes():
    try:
        airplanes = Airplane.query.all()
        response = jsonify([e.serialize() for e in airplanes])
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return (str(e))


@app.route("/getAirplain/<id_>", methods=['GET'])
def get_airplane_by_id(id_):
    try:
        airplain = Airplane.query.filter_by(id=id_).first()
        response = jsonify(airplain.serialize())
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return (str(e))


@app.route("/editAirplain/<id_>", methods=['GET'])
def edit_airplane_by_id(id_):
    try:
        name = request.args.get('name')
        total_flight_count = request.args.get('total_flight_count')
        airline = request.args.get('airline')
        info = request.args.get('info')

        airplain = Airplane.query.filter_by(id=id_).first()

        airplain.name = name
        airplain.total_flight_count = total_flight_count
        airplain.airline = airline
        airplain.info = info

        db.session.add(airplain)
        db.session.commit()

        response = jsonify(airplain.serialize())
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return (str(e))


@app.route("/deleteAirplain/<id_>", methods=['GET'])
def delete_airplane_by_id(id_):
    try:
        airplain = Airplane.query.filter_by(id=id_).first()
        db.session.delete(airplain)
        db.session.commit()

        response = jsonify()
        response.headers.add('Access-Control-Allow-Origin', '*')
        return '', 204
    except Exception as e:
        return (str(e))


@app.route("/addFlight", methods=['POST'])
def add_flight():
    airport_start = request.args.get('airport_start')
    airport_end = request.args.get('airport_end')
    airplane_speed = request.args.get('airplane_speed')
    status = request.args.get('status')
    airplane_id = request.args.get('airplane_id')
    # status = Flight.FlightStatusEnum.NOT_STARTED
    # print( Flight.FlightStatusEnum(status))
    if status not in {i.value for i in Flight.FlightStatusEnum}:
        raise ValueError()

    try:
        flight = Flight(
            airport_start=airport_start,
            airport_end=airport_end,
            airplane_speed=airplane_speed,
            status=Flight.FlightStatusEnum(status),
            airplane_id=airplane_id,
        )
        db.session.add(flight)
        db.session.commit()
        response = jsonify()
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 201
    except Exception as e:
        return (str(e))


@app.route("/getallFlight", methods=['GET'])
def get_all_flights():
    try:
        flights = Flight.query.all()
        response = jsonify([e.serialize() for e in flights])
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return (str(e))


@app.route("/getFlight/<id_>", methods=['GET'])
def get_flight_by_id(id_):
    try:
        flight = Flight.query.filter_by(id=id_).first()
        response = jsonify(flight.serialize())
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return (str(e))


@app.route("/editFlight/<id_>", methods=['GET'])
def edit_flight_by_id(id_):
    try:

        airport_start = request.args.get('airport_start')
        airport_end = request.args.get('airport_end')
        airplane_speed = request.args.get('airplane_speed')
        status = request.args.get('status')
        airplane_id = request.args.get('airplane_id')

        if status not in {i.value for i in Flight.FlightStatusEnum}:
            raise ValueError()

        flight = Flight.query.filter_by(id=id_).first()

        flight.airport_start = airport_start
        flight.airport_end = airport_end
        flight.airplane_speed = airplane_speed
        flight.status = Flight.FlightStatusEnum(status)
        flight.airplane_id = airplane_id

        db.session.add(flight)
        db.session.commit()

        response = jsonify(flight.serialize())
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return (str(e))


@app.route("/deleteFlight/<id_>", methods=['GET'])
def delete_flight_by_id(id_):
    try:
        flight = Flight.query.filter_by(id=id_).first()
        db.session.delete(flight)
        db.session.commit()

        response = jsonify()
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 204
    except Exception as e:
        return (str(e))
