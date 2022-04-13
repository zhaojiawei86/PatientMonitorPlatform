'''
appointment module:
manage medical device;
assign device and get measure result
'''
import os
import sqlite3
from flask import request, Blueprint, render_template
# , url_for, flash, redirect
from werkzeug.exceptions import abort
from modules import PROJ_ADDRESS, AWS_ADDRESS

if not os.path.exists(PROJ_ADDRESS):
    PROJ_ADDRESS = AWS_ADDRESS
DB_ADDRESS = PROJ_ADDRESS + "/database/db.sqlite3"

apts = Blueprint("apts", __name__)


def get_db_connection():
    '''connect db'''
    conn = sqlite3.connect(DB_ADDRESS)
    conn.row_factory = sqlite3.Row
    return conn


def get_post(device_id):
    '''get single device'''
    conn = get_db_connection()
    single_post = conn.execute('SELECT * FROM devices WHERE Device_ID = ?',
                               (device_id,)).fetchone()
    conn.close()
    if single_post is None:
        abort(404)
    return single_post


@apts.route('/appointment')
def all_appointments():
    '''get all appointments'''
    if request.method == 'GET':
        conn = get_db_connection()
        all_apts = conn.execute('SELECT * FROM appointments').fetchall()
        conn.close()
        return render_template('appointments.html', all_apts=all_apts)


# @devices.route('/appointments', methods=['GET'])
# def appointments():
#     '''get appointments'''
#     with sqlite3.connect(DB_ADDRESS) as conn:
#         if request.method == 'GET':
#             cursor = conn.execute("SELECT * FROM appointments")
#             appointments_list = [
#                 dict(Appointment_ID=row[0], Doctor_ID=row[1], Patient_ID=row[2],
#                      Device_ID=row[3], Device_Output=row[4], Date=row[5], Alert=row[6])
#                 for row in cursor.fetchall()
#             ]
#             if appointments_list is not None:
#                 return jsonify(appointments_list)
#     return None


# @devices.route('/appointment/<int:apt_id>', methods=['GET', 'PUT'])
# def single_apt(apt_id):
#     '''get/ change/ delete device'''
#     with sqlite3.connect(DB_ADDRESS) as conn:
#         cursor = conn.cursor()
#         apt = None
#         if request.method == 'GET':
#             cursor.execute(
#                 "SELECT * FROM appointments WHERE Appointment_ID=?", (apt_id,))
#             rows = cursor.fetchall()
#             for row in rows:
#                 apt = row
#             if apt is not None:
#                 return jsonify(apt), 200
#             return f"Cannot find appointment {apt_id}", 404

#         if request.method == 'PUT':
#             sql = """UPDATE appointments
#                     SET Device_ID=?
#                     WHERE Appointment_ID=?"""
#             device_id = request.form['Device_ID']
#             updated_apt = {
#                 'Appointment_ID': apt_id,
#                 'Device_ID': device_id
#             }
#             conn.execute(sql, (device_id, apt_id,))
#             conn.commit()
#             return jsonify(updated_apt)
#     return None

# if __name__ == "__main__":
#     devices.run(debug=True)
