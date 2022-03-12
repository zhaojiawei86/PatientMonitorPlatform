# Introduction for modules

![IMG_B5684ABC01BF-1](https://user-images.githubusercontent.com/59852184/156551152-39f6e9e8-aea0-426e-9bec-2f37ce09eb0c.jpeg)

## device module

### functions:

1. add_device:  
   input: Device_ID, Device_Name  
   function: create new device in device table

2. remove_device:  
   input: Device_ID  
   function: delete this device from device table

3. assign_device:  
   input: Appointment_ID, Device_ID
   function:  
   assign device to patient

4. set_measurement:
   input: Appointment_ID
   function:
   read Appointment_ID from appointment table
   get device output from device manager
   write output into appointment table

5. get_measurement:
   input: Appointment_ID
   output: Device_Output
   function:
   read Appointment_ID from appointment table  
   get the device output
