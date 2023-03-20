# Notes App
A simple note editor created via Vue3.js. It has basic functionality including: creating and deleting notes, sorting by default/date/alphabet option, searching by the title. Every note has date which is set when the note created and updated every time when the note has been changed, so then the note is set to the very beggining of the notes list by default sorting. You can use group selection to delete a few notes at once as well. When the app is opened it uses `hipsum.co` API to generate a lorem ipsum template note.

## Stack

- Vue3 
- TypeScript
- SCSS
- Python
- Flask
- MySQL

## Start Locally
### Client
1. Install all the dependencies. Use: `npm install`
2. Use `npm start` to start at localhost:8080

### Server
1. Install all the dependencies. Use: `pip install -r requirements.txt`
2. Use your IDE to start the project or `python ./backend/index.py` to start from a terminal at localhost:5000
