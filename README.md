## Medicine Index Application

[Click here](https://nabilmoiun-meds.netlify.app/) to View the live site.

## Technology
+ Backend: Python, Django, Django Restframework
+ Frontend: Vue Js 3

## Getting Started

You must have reliable python and node js installed on your machine to run the application.

I have used python==3.12.3 and node==20.17.0

A bit downgraded versions should work as well.


## Usage
You can [Watch Video](https://drive.google.com/file/d/121BxWaqj9VceVVMoozLHbeVG7Hu0vCGv/view?usp=sharing) to set up the project as per the instructions below: 

To get the backend ready, follow the steps below:

Clone the repo and move into the project root

```bash
git clone https://github.com/MoinulNabil/Medicine-Index.git
cd Medicine-Index

```

Install the dependencies of the frontend and backend.

I would recommend to work on a virtual environment. I have used virtualenv package to create a virtual environment you may wanna use other package. So install this as well if you already haven't..

Create a virtual environment by the following command.

```bash

virtualenv venv

```
Activate the virtual environment by the following command:

**On Linux***

```bash

source venv/bin/activate

```    
***On Windows***

If you are using git bash

```bash

source venv/Scripts/activate

```
Now install dependencies:

```bash
npm i
pip install -r requirements.txt

```

As the backend and frontend run on their individual different development servers,
they must be run separately.

Follow the process below:

## Backend
Backend must be prepared first as they will serve api to the frontend. Follow the steps below to run the backend. The backend code (Rest Api) exists in the api directory.

We will add some data (From data.json) as well that I used for testing purpose in my local machine and server.

```bash
cd api
python manage.py migrate
python manage.py loaddata data.json
python manage.py runserver

```

That's it for backend. Keep the shell alive and follow through the next step to run the frontend.

## Frontend
Our backend server is running now. Next, open up a different terminal shell in the project root directory Medicine-Index

Create a file name .env and put the contents as follows:

.env file

```bash
VITE_APP_HOST=http://localhost:8000
VITE_APP_PAGESIZE=10
VITE_ACCESS_TOKEN_KEY=token
VITE_ALERT_TIMER=2000
```

And just run the following command from Medicine-Index directory to spin up the frontend Vue server

```bash
npm run dev

```
Hit [http://localhost:5173](http://localhost:5173) on your browser to view the application.

## Deployment

+ Backend as been deployed on Render
+ Frontend has been deployed on Netlify

## Notes
Feel free to ask me if you face any issues.



