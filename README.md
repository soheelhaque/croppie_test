# croppie_test
Demo app showing how to use the croppie control within Django (https://foliotek.github.io/Croppie/)

The app allows users to upload photos with a title to a website, and these are then displayed in a gallery. Users can click on a photo in the gallery to see details
When a photo is uploaded, it can be cropped using croppie.
In addition, there is a loading animation while the photo is loading into croppie.
This demo assumes that you have some basic familiarity with Django and Pycharm.

1. Install Pycharm if you haven't already
2. Clone the project from Github and open as a Pycharm project.
3. Configure a virtual environment using Python 3.8
4. Run "makemigrations" and "migrate" within manage.py
5. Run "runserver <port number>" within manage.py, or run using the run configuation within PyCharm
6. You can access the website at http://127.0.0.1:8000
7. You can access the admin page at http://127.0.0.1:8000. To login, you will need to create an admin user by running "createsuperuser" in manage.py
  
&copy;Soheel Haque-Everding 2020
This software is intended for personal use only, and the author accepts no liability or responsibility related to your usage of it.
