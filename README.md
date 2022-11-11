# VJTI Mumbai Alumni Connect 
  This web-application aims to facilitate the Alumni Affairs of VJTI Mumbai. Please read contributing guidelines before starting.

## Requirements

 * Python: 3.7/3.8  
 * Django: 2.2.20 
 * And additional requirements are in [**requirements.txt**](./requirements.txt). These will automatically be installed with below steps.


## How to run it?

  * Fork the repository.
  * Clone the repository to your local machine `$ git clone https://github.com/<your-github-username>/alumni-management-system.git`
  * Change directory to alumni `$ cd alumni-management-system`
  * Install virtualenv `$ pip3 install virtualenv`  
  * Create a virtual environment `$ virtualenv env -p python3`
  * Activate the env: `$ source env/bin/activate` (for linux) `> ./env/Scripts/activate` (for Windows PowerShell)
  * Install the requirements: `$ pip install -r requirements.txt`  
    **Note:** If some requirement causes some error, remove the version from that requirement (ex. convert `anyjson==0.3.3` to `anyjson`) and run the above command again.
  * Make migrations `$ python manage.py makemigrations`
  * Migrate the changes to the database `$ python manage.py migrate`
  * Run the server `$ python manage.py runserver`
  * Create admin `$ python manage.py createsuperuser`
  * Create tables `$ python manage.py migrate --run-syncdb`

