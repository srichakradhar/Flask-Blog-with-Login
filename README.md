# Flask-Blog-with-Login  
Flask-Blog-with-Login is a python web app that lets you create a blog with login and sign up. 

## Authentication options
* User register / login / logout / cancel account


## Deployment
Download
```bash
git clone https://github.com/srichakradhar/Flask-Blog-with-Login.git
cd Flask-Blog-with-Login
```
Deploy virtual environment.
```
virtualenv venv
source ./venv/bin/activiate
```
Install requirements
```bash 
# install python requirements
python3 -m pip install -r requirements.txt
```
Deploy database
```python
# python3
from app import db, create_app
db.create_all(app=create_app())
```
On a development server
```bash 
# run
python3 ./app.py
```
On a production server
> Learn how to [deploy flask app on ubuntu vps](https://blog.joseaniceto.com/ubuntu-vps.html)
> Learn how to [deploy flask app on raspberrypi](https://www.raspberrypi-spy.co.uk/2018/12/running-flask-under-nginx-raspberry-pi/)

Terminate virtualenv  (if you want)
```bash
deactivate
```
### Install virtualenv
```bash
# Use pip3
pip3 install virtualenv
```
```bash
# Use apt-get
sudo apt-get install virtualenv
```
### Install pip3
```bash
# Use apt-get
sudo apt-get install python3-pip
```
```bash
# Use brew
brew install python3
```