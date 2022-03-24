# FastAPI + Flutter + Heroku

This project is just a showcase on how to use Python as backend for flutter application and deploy them using heroku.

##### This project was mentioned on https://github.com/antonio-pedro99/fastapi_example  

## FastAPI

To build the backend, I used FastAPI which is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
FastAPI has many features and the keys one are  fast, fast to code, fewer bugs, intuitive, easy, Short, Robust. It is very easy to design and document APIs with FastAPI, that is one of the reason I like it. Fast API also supports ORMs, and in this app we used Sqlalchemy our SQLite database.

Reading: https://fastapi.tiangolo.com/

## Heroku

Heroku is a cloud platform as a service supporting several programming languages. One of the first cloud platforms(read more https://en.wikipedia.org/wiki/Heroku).

## Backend anatomy

This a very simple notes app and the strutect of the notes are as follows:

Notes:
  - id : integer value
  - text: string value
  - completed: boolean value
 
 ### SQL 
 our SQL looks like

 CREATE TABLE notes (
      id int not null primary key auto_increment,
      text varchar(255) not null,
      completed boolean not null default 0
 );
 
## Endpoints 

### Post
  URL_HOST/notes/  create a new note
  
### Get
  URL_HOST/notes/  get all notes
  
 URL_HOST can be your localhost(in development) or your heroku-project-name-herokuapp.com/ (in production)
 
 ### FastAPI Swagger Ui
 
 FastAPI is very useful when it comes to documentation of your api, through Swagger you will be able to have your API's docs without any effort
 
 ![image](https://user-images.githubusercontent.com/42675180/159958799-ae5ae91a-a062-49d2-b99e-138cd87531cb.png)

 


 
