Introduction
===========

Building an REST API with Django using Vagrant and Puppet or standalone on Ubuntu 14.04.

# Without vagrant

1. Install mysql server
2. Install python and pip
3. Install virtualenv and virtualenvwrapper
4. Create a virtualenv
5. Activate the virtualenv with the following command
+ `source (virtualenv)/bin/activate`
6. Run the command:
+ `pip install -r puppet/provision/modules/language/files/local.txt`
7. Verify all the packages with yolk:
+ `yolk -l`
8. Modify manage.py like 'Run the application' section

# Without vagrant and without mysql - using sqlite

1. Install python and pip
2. Install virtualenv and virtualenvwrapper
3. Create a virtualenv
4. Activate the virtualenv with the following command
+ `source (virtualenv)/bin/activate`
5. Run the command:
+ `pip install -r puppet/provision/modules/language/files/local_sqlite3.txt`
6. Using pip freeze instead of yolk:
+ `pip freeze`
7. Use just virtualenvwrapper postactivate:
+ `export DJANGO_SETTINGS_MODULE=agenda.settings.local_sqlite3`

# Using Vagrant

## Prerequisites

+ [Vagrant](http://www.vagrantup.com/downloads.html)
+ [Vagrant BindFS](https://github.com/gael-ian/vagrant-bindfs)
+ [Vagrant Puppet Install](https://github.com/petems/vagrant-puppet-install)

Modules for puppet:

+ puppetlabs-apache v1.5.0
+ puppetlabs-apt v2.1.1
+ puppetlabs-mysql v3.4.0
+ puppetlabs-reboot v1.1.0

To install puppet modules, execute the following command:

+ `puppet module install puppetlabs-apache`
+ `puppet module install puppetlabs-apt`
+ `puppet module install puppetlabs-mysql`
+ `puppet module install puppetlabs-reboot`

To install vagrant plugins, execute the following command:

+ `vagrant plugin install vagrant-bindfs`
+ `vagrant plugin install vagrant-puppet-install`
+ `vagrant plugin install vagrant-vbguest`

## Getting Started

This is a fairly simple project to get up and running.
The procedure for starting up is as follows:

1. Clone the project. (There’s only master branch.)
2. Modify parameters in config.yaml such as:
- USER
- PASSWORD
- PROJECT
- DOMAIN_NAME
- HOSTNAME
- public_ip according your network connection.
3. Run the command `vagrant up` from the directory

For standalone configuration:
4. Open your browser to http://localhost:8000
For vagrant configuration:
4. Open your browser to http://localhost:9834

## Run the application

1. Modify the following line at manage.py:
+ `os.environ.setdefault("DJANGO_SETTINGS_MODULE", "agenda.settings")`
For local development:
+ `os.environ.setdefault("DJANGO_SETTINGS_MODULE", "agenda.settings.local")`
For production:
+ `os.environ.setdefault("DJANGO_SETTINGS_MODULE", "agenda.settings.production")`

For changing this manual change, we need to use virtualenvwrapper.

2. For running the application the first time:
`python manage.py migrate`

3. For running django server
`python manage.py runserver 0.0.0.0:8000`

## Heroku Deployment Supported

Added the require files to deploy on Heroku:
+ `requirements.txt`
+ `Procfile`

On Heroku:
* `heroku config:set DJANGO_SETTINGS_MODULE=agenda.settings.production`

Config mysql database:
* `heroku addons:create cleardb:ignite`
* `heroku config | grep CLEARDB_DATABASE_URL`

Copy the message result:
* `heroku config:set DATABASE_URL='mysql://xxxxxxxx:yyyyyy@zzzzzzzz/heroku_db?reconnect=true'`

Create super user:
* `heroku run python manage.py createsuperuser`

Restart web server
* `heroku ps:scale web=0 && heroku ps:scale web=1`
