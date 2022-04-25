<img width="700" alt="image" src="https://user-images.githubusercontent.com/59852184/162890520-dceb5bba-fe8c-4cf0-b491-dad9a6d44c35.png">

# Patient Monitor Platform

Jiawei Zhao  
Project for EC530 22Spring.

Platform to monitor patients, which could also enable medical profe to check medical measurements, make appointments and chat.

# Table of Contents

- [Technologies](#technologies)
- [Setup](#setup)
- [Demo](#demo)
- [Database Structure](#database-structure)
- [Thread](#thread)
- [Test](#test)
- [Usage](#usage)
- [To do](#to-do)

# Technologies

Project is created with:

- Python 3.8.9
- Flask 2.0.3
- SQLite 3.36.0

# Setup

To run this project, download all the project and:

> cd PatientMonitorPlatform/  
> pip3 install requirements.txt  
> python3 app.py

# Demo

Here's a working live demo: http://35.172.134.33:8080/

# Database Structure

<img width="800" alt="image" src="https://user-images.githubusercontent.com/59852184/165007220-96908541-2cd3-4b84-9880-30d64f5a85da.png">

# Thread

Single chat detail could be asked for in threads, which help users GET at the same time.
We GET single chat for the following order:

```
chat 1
chat 2
chat 1
chat 1
```

And we get the thread information in background:

```
# Task 1 begin.
# Task 2 begin.
# Task done.
10.192.41.70 - - [06/Apr/2022 18:05:50] "GET /thread-chats/1 HTTP/1.1" 200 -
# Task 1 begin.
# Task done.
10.192.41.70 - - [06/Apr/2022 18:05:52] "GET /thread-chats/2 HTTP/1.1" 200 -
# Task 1 begin.
# Task done.
10.192.41.70 - - [06/Apr/2022 18:05:56] "GET /thread-chats/1 HTTP/1.1" 200 -
# Task done.
10.192.41.70 - - [06/Apr/2022 18:05:59] "GET /thread-chats/1 HTTP/1.1" 200 -
```

# Test

test all responses for module, check whether if all responses have code 200

<img width="525" alt="image" src="https://user-images.githubusercontent.com/59852184/159433741-a5c43229-e802-44c0-afa3-12cc0d64bc1e.png">

<img width="529" alt="image" src="https://user-images.githubusercontent.com/59852184/159435045-28b10424-0290-4e64-b69f-e48062761c9d.png">

# Usage

## 1. Devices

<img width="600" alt="image" src="https://user-images.githubusercontent.com/59852184/162890373-bce28c02-9814-4dd9-8fe9-930d71a48b91.png">

### GET all devices & single device

![dev_get](https://user-images.githubusercontent.com/59852184/162889341-6cab1a17-bc18-4837-a653-6a36cf0b9df9.gif)

### POST new device

![dev_add](https://user-images.githubusercontent.com/59852184/162889428-0fa33412-eddd-4e3e-a19b-777921092ed0.gif)

### Edit devices

![dev_edit](https://user-images.githubusercontent.com/59852184/162889490-0372f981-bd39-4255-a68b-080097765d4b.gif)

### DELETE devices

![dev_del](https://user-images.githubusercontent.com/59852184/162889548-dc708445-1b0e-455c-8fe1-5be6fc1c73ef.gif)

## 2. Chat History

<img width="600" alt="image" src="https://user-images.githubusercontent.com/59852184/162890321-d5ab40b5-4339-4087-968e-b8af74e1354b.png">

### GET chat & Speech to Text

![chat](https://user-images.githubusercontent.com/59852184/162889190-cae8610f-0b59-4e07-a6c4-9c85d9f7449d.gif)

## 3. Appointments

<img width="600" alt="image" src="https://user-images.githubusercontent.com/59852184/162890230-8b30d969-241e-4698-96fc-b1457da8a252.png">

### GET

![apts](https://user-images.githubusercontent.com/59852184/162888992-4c22a6c3-3a9b-4939-b640-000f68a08e5b.gif)

# To do

- Web Dev for users management
- P2P
