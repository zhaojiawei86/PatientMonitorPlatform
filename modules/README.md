# Introduction for modules

![IMG_C6662C539033-1](https://user-images.githubusercontent.com/59852184/159430608-530c1bc9-1216-4b93-87c9-4be581757740.jpeg)

## 1. devices module

### functions:

URL: http://127.0.0.1:5000/devices

1. GET devices  
   <img width="371" alt="image" src="https://user-images.githubusercontent.com/59852184/159432155-f840cbc0-229d-4f61-bec1-ebf03a051de4.png">
2. POST devices  
   new device has been added  
   <img width="506" alt="image" src="https://user-images.githubusercontent.com/59852184/159432344-53115360-c3be-4e54-96b2-65be30840b46.png"><img width="392" alt="image" src="https://user-images.githubusercontent.com/59852184/159432398-b0418574-ff5b-45f8-a2a9-8b03d8d42fbb.png">

URL: http://127.0.0.1:5000/device/\<device_id>

1. GET single device  
   <img width="361" alt="image" src="https://user-images.githubusercontent.com/59852184/159432744-6db74506-ae85-49d9-ae85-710f8381d892.png">
2. PUT single device  
   update device name  
   <img width="490" alt="image" src="https://user-images.githubusercontent.com/59852184/159433476-7563d54e-7bd6-4fc1-9ea3-6231f3605220.png">
3. DELETE single device  
   <img width="345" alt="image" src="https://user-images.githubusercontent.com/59852184/159433584-dda54453-4ec1-40b9-8fcc-8faa652afa1b.png">

### unit test:

test all responses for devices module, check whether if all responses have code 200  
<img width="525" alt="image" src="https://user-images.githubusercontent.com/59852184/159433741-a5c43229-e802-44c0-afa3-12cc0d64bc1e.png">

## 2. chats module

### functions:

URL: http://127.0.0.1:5000/chats

1. GET all chats  
   Already get two chat history, chat_content means chat address.  
   One chat file for text version, one for audio.  
   <img width="449" alt="image" src="https://user-images.githubusercontent.com/59852184/159434332-9b4874ba-f109-4ed9-8320-09ac64e4a965.png">

URL: http://127.0.0.1:5000/chat/\<chat_id>

2. GET content for chat
   chat with id=1 is an audio file, convert audio to text.  
   <img width="438" alt="image" src="https://user-images.githubusercontent.com/59852184/159434771-cf547573-72c2-4be9-af8e-82315935d982.png">

   chat with id=2 is a text file  
   <img width="374" alt="image" src="https://user-images.githubusercontent.com/59852184/159434857-e28c7946-68de-4917-9b1a-d89a3d31fa95.png">

### unit test:

test all responses for chats module, check whether if all responses have code 200  
<img width="529" alt="image" src="https://user-images.githubusercontent.com/59852184/159435045-28b10424-0290-4e64-b69f-e48062761c9d.png">
