
#### install python3.4 to your system from https://www.python.org/downloads/
#### commands for linux or mac terminal , creating virtual-env and installing dependencies
$ python3.4 -m venv totient_env
$ pip install -r requirement.txt

#### activating the virtual environment
#### for mac-terminal
$ . totient_env/bin/activate
#### for linux/unix terminal
$ source totient_env/bin/activate

#### export project patch to pythonpath : or .../totient/
export PYTHONPATH=path-to-project-root:$PYTHONPATH

#### running the dev server
#### manage.py is located in totient/manage.py
python manage.py runserver


#### try viewing urls in swagger localhost:8000/docs/ , access the admin site at localhost:8000/admin/
/api-token-auth/ : for getting the jwt token

### pass the jwt token to every request

### urls are:

Get/POST : /route/routes/ (Lists and create routes for a logged-in-user with name, default set date as todays date)
POST: /route/locations/ (Add one or more locations : (lat, long), along with route-id of the logged-in user)

Admin-only:

GET : route/admin/routes/ (Lists all routes , with filtering on user, date_from, date_till)

