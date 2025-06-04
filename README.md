# README.md file for littlelemon course capstone
# Before anything here you need to be athenticated

## Home page for Littlelemon
- http://localhost:8000/restaurant/

##  Get menu items // single menu item
GET: http://127.0.0.1:8000//api/menu-items
     
     http://127.0.0.1:8000//api/menu-items/{itemId}

## API to display booking table 
- http://localhost:8000/restaurant/booking/tables/


## List all users 
- Get:  http://localhost:8000/auth/users/

## register new user using {"email": "", "username": "", "password": ""}
- POST: http://localhost:8000/auth/users/


## Run unittest
python manage.py test
