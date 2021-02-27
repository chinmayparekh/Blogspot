# Instructions

1. ## For installing virtual environment

On macOS and Linux:
python3 -m pip3  install --user virtualenv

On Windows:
py -m pip3 install --user virtualenv

2. ## For creating virtual environment
On macOS and Linux:
python3 -m venv env

On Windows:
py -m venv env

3. ## For activating the virtual environment

On macOS and Linux:
source env/bin/activate

On Windows:
.\env\Scripts\activate

4. ## Use the following command in your terminal
git clone https://github.com/chinmayparekh/Blogspot.git

5. ## Install requirements
cd Blogspot/ <br/>
pip3 install -r requirements.txt

6. ## Make migrations
python3 manage.py makemigrations
python3 manage.py migrate

7. ## Run the server
python3 manage.py runserver
