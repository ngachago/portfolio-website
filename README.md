# Data Science Portfolio Website
This repository hosts the code for my portfolio site which was built by modifying the code base found [here](https://github.com/julianikulski/portfolio-website).


## Table of Contents
1. [Installation](#installation)
2. [Instructions](#instructions)
    1. [Create Database for Content](#create_database)
    2. [Updating Database Content](#update_database)
4. [File Descriptions](#descriptions)
5. [Licensing, Authors, Acknowledgements](#licensing)


## Installation <a name="installation"></a>
The code requires Python 3 versions.

I would advise creating a [virtual environment](https://medium.com/datacat/a-simple-guide-to-creating-a-virtual-environment-in-python-for-windows-and-mac-1079f40be518) for your project.

Install the packages listed in `requirements.txt` by running `pip install -r requirements.txt` in the terminal.

## Instructions <a name="instructions"></a>

### Create Database for Content <a name="create_database"></a>
The database containing the content for the website is a PostgreSQL database on Heroku.

If you want to update the database, you need to connect to the remote database in your local environment. Follow the below steps to connect to a Heroku PostgreSQL database locally:
1. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).
2. Create a PostgreSQL database on [Heroku](https://devcenter.heroku.com/articles/heroku-postgresql#provisioning-heroku-postgres) that is linked to this app.
3. Install PostgreSQL on your computer locally and update your PATH environment variable to add the bin directory of your Postgres installation. (More details [here](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup))
4. Get the database credentials by running `heroku pg:credentials:url -a <your app name>`. Copy the Connection URL.
5. Paste the Connection URL into the `production_input` variable in `sample.run.sh`. Update the file name to `run.sh`.
6. Create the database locally on PostgreSQL using pgAdmin, which should have been included in installation.
6. Update the `development_input` variable in `run.sh` with your information.

Now your local environment has the DATABASE_URL for your remote Heroku PostgreSQL database saved and the code in app.py can access this database from your local computer. The DATABASE_URL in `development_input` allows you to update data and test the site locally before deploying to Heroku.

### Update Database Content <a name="update_database"></a>
To update the database content, modify the excel files in the sample_database folder to contain the content you would like to feed to the database. Remove the `sample_` notation from the folder and file names to match the notation expected in the code.

Running `./run.sh dbfeed` in the terminal will update the database locally

**Please note**: There is currently no feature in this file that deletes and creates a new database if a new column is added. Adding of rows is handled, but not of columns. Therefore, if you want to add a new column to the Excel file and then database, you need to first reset the PostgreSQL in the app on Heroku and then you need to add the relevant code to the script, before running it.


### Development vs. Production <a name="mode"></a>
It is recommended to make and test changes locally before deploying to Heroku. Once data is updated, run `./run.sh` in the terminal to load your site on localhost.

## File Description <a name="descriptions"></a>
The `templates` folder contains all html pages that will be accessible through the site. The `static` folder is made up of the images displayed on the site, the robots.txt file (to prevent Google indexing), as well as the CSS stylesheet. `app.py` is the file which will render the website through the micro web framework Flask. `database_feeder.py` is the script that reads in the data from the Excel files into the database. The `helper.py` file contains the functions querying the database when a html page is rendered.

## Licensing, Authors, Acknowledgements <a name="licensing"></a>
This original code can be used under the [MIT license](https://github.com/julianikulski/portfolio-website/blob/master/LICENSE.md). All modifications I have made are also subject to the MIT license. Feel free to use the code, updating any of my personal information (name, experience, etc.) to your own.
