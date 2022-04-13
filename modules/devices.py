'''
device module:
manage medical device;
assign device and get measure result
'''
import os
import sqlite3
from flask import request, Blueprint, render_template, url_for, flash, redirect
from werkzeug.exceptions import abort
from modules import PROJ_ADDRESS, AWS_ADDRESS


if not os.path.exists(PROJ_ADDRESS):
    PROJ_ADDRESS = AWS_ADDRESS
DB_ADDRESS = PROJ_ADDRESS + "/database/db.sqlite3"

devices = Blueprint("devices", __name__)


def get_db_connection():
    '''connect db'''
    conn = sqlite3.connect(DB_ADDRESS)
    conn.row_factory = sqlite3.Row
    return conn


@devices.route('/device')
def all_devices():
    '''get all devices'''
    if request.method == 'GET':
        conn = get_db_connection()
        devices_data = conn.execute('SELECT * FROM devices').fetchall()
        conn.close()
        return render_template('devices.html', devices_data=devices_data)


@devices.route('/device/new', methods=['GET', 'POST'])
def new_device():
    '''post new deivce'''
    if request.method == 'POST':
        title = request.form['title']

        if not title:
            flash('Device name is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO devices (Device_Name) VALUES (?)',
                         (title,))
            conn.commit()
            conn.close()
            return redirect(url_for('devices.all_devices'))
    return render_template('device_post.html')


# @devices.route('/devices', methods=['GET', 'POST'])
# def all_devices():
#     '''get / post device'''
#     with sqlite3.connect(DB_ADDRESS) as conn:
#         if request.method == 'GET':
#             cursor = conn.execute("SELECT * FROM devices")
#             devices_list = [
#                 dict(Device_ID=row[0], Device_Name=row[1])
#                 for row in cursor.fetchall()
#             ]
#             if devices_list is not None:
#                 return jsonify(devices_list)

#         if request.method == 'POST':
#             new_device = request.form['Device_Name']
#             sql = """INSERT INTO devices (Device_Name) VALUES (?)"""
#             cursor = conn.execute(sql, (new_device,))
#             conn.commit()
#             return f"Device with the id {cursor.lastrowid} created successfully.", 201

#     return None


def get_post(device_id):
    '''get single device'''
    conn = get_db_connection()
    single_post = conn.execute('SELECT * FROM devices WHERE Device_ID = ?',
                               (device_id,)).fetchone()
    conn.close()
    if single_post is None:
        abort(404)
    return single_post


@devices.route('/device/<int:device_id>')
def single_device(device_id):
    '''get single device'''
    if request.method == 'GET':
        device = get_post(device_id)
        return render_template('device_single.html', device=device)


@devices.route('/device/<int:device_id>/edit', methods=('GET', 'POST'))
def edit_device(device_id):
    '''edit device'''
    edit_name = get_post(device_id)

    if request.method == 'POST':
        title = request.form['title']

        if not title:
            flash('Device name is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE devices SET Device_Name = ?'
                         ' WHERE Device_ID = ?',
                         (title, device_id,))
            conn.commit()
            conn.close()
            return redirect(url_for('devices.all_devices'))

    return render_template('device_edit.html', edit_name=edit_name)


@devices.route('/device/<int:device_id>/delete', methods=('POST',))
def delete_device(device_id):
    '''delete device'''
    del_device = get_post(device_id)
    conn = get_db_connection()
    conn.execute('DELETE FROM devices WHERE Device_ID = ?', (device_id,))
    conn.commit()
    conn.close()
    flash(f"{del_device['Device_ID']} was successfully deleted!")
    return redirect(url_for('devices.all_devices'))

# @devices.route('/device/<int:device_id>', methods=['GET', 'PUT', 'DELETE'])
# def single_device(device_id):
    # '''get/ change/ delete device'''
    # with sqlite3.connect(DB_ADDRESS) as conn:
    #     cursor = conn.cursor()
    #     device = None
    #     if request.method == 'GET':
    #         cursor.execute(
    #             "SELECT * FROM devices WHERE Device_ID=?", (device_id,))
    #         rows = cursor.fetchall()
    #         for row in rows:
    #             device = row
    #         if device is not None:
    #             return jsonify(device), 200
    #         return f"Cannot find device {device_id}", 404

    #     if request.method == 'PUT':
    #         sql = """UPDATE devices
    #                 SET Device_Name=?
    #                 WHERE Device_ID=?"""
    #         device_name = request.form['Device_Name']
    #         updated_device = {
    #             'Device_ID': device_id,
    #             'Device_Name': device_name
    #         }
    #         conn.execute(sql, (device_name, device_id,))
    #         conn.commit()
    #         return jsonify(updated_device), 200

    #     if request.method == 'DELETE':
    #         if device_id in range(1, 7):
    #             return "This device cannot be removed.", 200

    #         sql = """ DELETE FROM devices WHERE Device_ID=?"""
    #         conn.execute(sql, (device_id,))
    #         conn.commit()
    #         return f"The device with id {device_id} has been deleted.", 200
    # return None


# if __name__ == "__main__":
#     devices.run(debug=True)
