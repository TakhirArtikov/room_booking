# room_booking

Clone the project via https://github.com/TakhirArtikov/room_booking.git

Check .env.example for variables to set up connection with PostgreSQL

### To run the project go to root folder of the project and run the following commands
``` bash
python3 manage.py makemigrations
python3 manage.py migrate
python manage.py runserver
```
 
It is all up

### For the documentation of the project go to the following link: http://localhost:8000/swagger/


### To run test run the following command:
``` bash
pytest
```

### To run pylint run the following command:
``` bash
make lint
```