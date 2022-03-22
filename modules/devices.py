'''
device module:
manage medical device;
assign device and get measure result
'''

import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/devices', methods=['GET', 'POST'])
def devices():
    '''get / post device'''
    with sqlite3.connect("../database/db.sqlite3") as conn:
        if request.method == 'GET':
            cursor = conn.execute("SELECT * FROM devices")
            devices_list = [
                dict(Device_ID=row[0], Device_Name=row[1])
                for row in cursor.fetchall()
            ]
            if devices_list is not None:
                return jsonify(devices_list)

        if request.method == 'POST':
            new_device = request.form['Device_Name']
            sql = """INSERT INTO devices (Device_Name) VALUES (?)"""
            cursor = conn.execute(sql, (new_device,))
            conn.commit()
            return f"Device with the id {cursor.lastrowid} created successfully.", 201
    return None


@app.route('/device/<int:device_id>', methods=['GET', 'PUT', 'DELETE'])
def single_device(device_id):
    '''get/ change/ delete device'''
    with sqlite3.connect("../database/db.sqlite3") as conn:
        cursor = conn.cursor()
        device = None
        if request.method == 'GET':
            cursor.execute(
                "SELECT * FROM devices WHERE Device_ID=?", (device_id,))
            rows = cursor.fetchall()
            for row in rows:
                device = row
            if device is not None:
                return jsonify(device), 200
            return f"Cannot find device {device_id}", 404

        if request.method == 'PUT':
            sql = """UPDATE devices
                    SET Device_Name=?
                    WHERE Device_ID=?"""
            device_name = request.form['Device_Name']
            updated_device = {
                'Device_ID': device_id,
                'Device_Name': device_name
            }
            conn.execute(sql, (device_name, device_id,))
            conn.commit()
            return jsonify(updated_device), 200

        if request.method == 'DELETE':
            if device_id in range(1, 7):
                return "This device cannot be removed.", 200

            sql = """ DELETE FROM devices WHERE Device_ID=?"""
            conn.execute(sql, (device_id,))
            conn.commit()
            return f"The device with id {device_id} has been deleted.", 200
    return None


@app.route('/appointments', methods=['GET'])
def appointments():
    '''get appointments'''
    with sqlite3.connect("../database/db.sqlite3") as conn:
        if request.method == 'GET':
            cursor = conn.execute("SELECT * FROM appointments")
            appointments_list = [
                dict(Appointment_ID=row[0], Doctor_ID=row[1], Patient_ID=row[2],
                     Device_ID=row[3], Device_Output=row[4], Date=row[5], Alert=row[6])
                for row in cursor.fetchall()
            ]
            if appointments_list is not None:
                return jsonify(appointments_list)
    return None


@app.route('/appointment/<int:apt_id>', methods=['GET', 'PUT'])
def single_apt(apt_id):
    '''get/ change/ delete device'''
    with sqlite3.connect("../database/db.sqlite3") as conn:
        cursor = conn.cursor()
        apt = None
        if request.method == 'GET':
            cursor.execute(
                "SELECT * FROM appointments WHERE Appointment_ID=?", (apt_id,))
            rows = cursor.fetchall()
            for row in rows:
                apt = row
            if apt is not None:
                return jsonify(apt), 200
            return f"Cannot find appointment {apt_id}", 404

        if request.method == 'PUT':
            sql = """UPDATE appointments
                    SET Device_ID=?
                    WHERE Appointment_ID=?"""
            device_id = request.form['Device_ID']
            updated_apt = {
                'Appointment_ID': apt_id,
                'Device_ID': device_id
            }
            conn.execute(sql, (device_id, apt_id,))
            conn.commit()
            return jsonify(updated_apt)
    return None


if __name__ == "__main__":
    app.run(debug=True)
