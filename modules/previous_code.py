''' devices.py'''
import sqlite3


def read_sqlite(db_name):
    '''read from database'''
    with sqlite3.connect("../database/db.sqlite3") as conn:
        command = "SELECT * FROM " + db_name
        cursor = conn.execute(command)
        return cursor.fetchall()


def add_device(device_id, device_name):
    '''
    add new device:
    device_id: int
    device_name: str
    '''
    try:
        new_device = {"Device_ID": device_id, "Device_Name": device_name}
        with sqlite3.connect("../database/db.sqlite3") as conn:
            command = "INSERT INTO devices VALUES(?, ?)"
            conn.execute(command, tuple(new_device.values()))
            conn.commit()
    except sqlite3.IntegrityError:
        print("This device_id/device_name has already existed. Please check.")
    else:
        print("New device has been already added.")


def remove_device(device_id):
    '''remove device from database'''
    if device_id in range(1, 7):
        print("This device cannot be removed.")
        return

    with sqlite3.connect("../database/db.sqlite3") as conn:
        command_dev = f"SELECT COUNT(*) from devices WHERE Device_ID={device_id}"
        cursor_dev = conn.execute(command_dev)
        dev_exist = cursor_dev.fetchall()[0][0]

        if dev_exist:
            command = "DELETE FROM devices WHERE Device_ID = ?"
            conn.execute(command, (device_id,))
            conn.commit()
        else:
            print(f"Device {device_id} does not exist, cannot remove.")


def assign_device(appointment_id, device_id):
    '''assign device'''
    with sqlite3.connect("../database/db.sqlite3") as conn:
        command_app = f"SELECT COUNT(*) from appointments WHERE Appointment_ID={appointment_id}"
        cursor_app = conn.execute(command_app)
        app_exist = cursor_app.fetchall()[0][0]

        command_dev = f"SELECT COUNT(*) from devices WHERE Device_ID={device_id}"
        cursor_dev = conn.execute(command_dev)
        dev_exist = cursor_dev.fetchall()[0][0]

        command_dev_in_app = f"SELECT COUNT(*) from appointments WHERE Device_ID={device_id}"
        cursor_dev_in_app = conn.execute(command_dev_in_app)
        dev_inappexist = cursor_dev_in_app.fetchall()[0][0]

        if not app_exist:
            print(f"Appointment {appointment_id} has not been created.")
            return
        if not dev_exist:
            print(f"Device {device_id} does not existed.")
            return
        if dev_inappexist:
            print(
                f"Appointment {appointment_id} has been assigned device, cannot be changed.")
            return

        command = "UPDATE appointments SET Device_ID = ? WHERE Appointment_ID = ?"
        conn.execute(command, (device_id, appointment_id,))
        conn.commit()


if __name__ == "__main__":

    print(read_sqlite("users"))
    print(read_sqlite("appointments"))
    print(read_sqlite("devices"))

    add_device(1, "new_device")
    add_device(7, "new_device")
    add_device(8, "new_device")
    print(read_sqlite("devices"))

    remove_device(1)
    remove_device(7)
    remove_device(8)
    print(read_sqlite("devices"))

    assign_device(1, 1)
    print(read_sqlite("appointments"))
    assign_device(3, 6)
    assign_device(3, 7)
    assign_device(4, 2)
    print(read_sqlite("appointments"))
