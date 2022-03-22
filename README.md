# PatientMonitorPlatform

Jiawei Zhao  
Project for EC530 22Spring.

Platform to monitor patients, which could enable people to check medical measurements, make appointments and chat.

## 1. Introduction

1. modules file  
   including all the module programs as well as their unit testing  
   detailed information could be checked here: https://github.com/zhaojiawei86/PatientMonitorPlatform/tree/master/modules#readme

```
devices.py
chats.py
test_devices.py
test_chats.py
```

2. database file  
   create default database used to implement a simulation to send data via an example program  
   databases saved in sqlite  
   ![IMG_C6662C539033-1](https://user-images.githubusercontent.com/59852184/159430608-530c1bc9-1216-4b93-87c9-4be581757740.jpeg)

```
default_db.py
db.sqlite3
```

3. tables file  
   tables used to create original database, all tables saved in json version

```
appointments.json
chats.json
devices.json
users.json
```

4. chat_record file  
   default chat record used to test chats module  
   including text and audio files

## 2. Branch Stategy

Create new branch for each phase/module/test. When all programs run successfully and pass the unit test, new branch will push to github and then deleted both in local and origin.
