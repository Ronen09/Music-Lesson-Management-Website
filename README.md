# Team *<enter team name here>* Small Group project

## Team members
The members of the team are:
- *Aayush Dwivedi (aayush.dwivedi@kcl.ac.uk)*
- *Ronen Roy (ronen.roy@kcl.ac.uk)*
- *Oliver Singer (oliver.singer@kcl.ac.uk)*
- *Tony Smith (tony.o.smith@kcl.ac.uk)*
- *Kabir Suri (kabir.suri@kcl.ac.uk)*

## Project structure
The project is called `msms` (Music School Management System).  It currently consists of a single app `lessons` where all functionality resides.

## Deployed version of the application
The deployed version of the application can be found at *<[enter URL here](URL)>*.

## Installation instructions
To install the software and use it in your local development environment, you must first set up and activate a local development environment.  From the root of the project:

```
$ virtualenv venv
$ source venv/bin/activate
```

Install all required packages:

```
$ pip3 install -r requirements.txt
```

Migrate the database:

```
$ python3 manage.py migrate
```

Seed the development database with:

```
$ python3 manage.py seed
```

Run all tests with:
```
$ python3 manage.py test
```

*The above instructions should work in your version of the application.  If there are deviations, declare those here in bold.  Otherwise, remove this line.*

## Sources
The packages used by this application are specified in `requirements.txt`

- Some source code taken from the Clucker project.
- Some illustrations taken from [Storyset](https://storyset.com).
    - [Illustration used for log in and sign up pages](https://storyset.com/illustration/connected-world/amico)
    - [Illustration used for welcome page](https://www.onlinelogomaker.com/blog/6-things-can-learn-iconic-music-logo-design/)