# Data Science Portfolio Website
This repository hosts the code for my [portfolio site](https://www.njeri-gachago.com/), deployed on Heroku.


## Table of Contents
1. [Installation](#installation)
2. [Production Mode](#production)
3. [File Descriptions](#descriptions)
4. [Licensing](#licensing)


## Installation <a name="installation"></a>
The code requires Python 3 versions.

I would advise creating a [virtual environment](https://medium.com/datacat/a-simple-guide-to-creating-a-virtual-environment-in-python-for-windows-and-mac-1079f40be518) for your project.

1. Install the packages listed in `requirements.txt` by running `pip install -r requirements.txt` in the terminal.
2. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install) and create your app.
3. It is recommended to make and test changes locally before deploying to Heroku. Run `python app.py` in the terminal to load your site on localhost.

## Production Mode <a name="production"></a>
Once you are ready to deploy the site:

1. Run `git remote -v` to make sure that the Heroku remote is active.
3. If it is not active, run `git remote add heroku https://git.heroku.com/{APP-NAME}.git` to activate.
4. Run `git push heroku master` to push the files to Heroku.

Heroku will provide a domain name, but consider adding your own for more personalization.

## File Description <a name="descriptions"></a>
The `templates` folder contains all html pages that will be accessible through the site. The `static` folder is made up of the images displayed on the site, as well as the CSS stylesheet. `app.py` is the file which will render the website through the micro web framework Flask.

## Licensing <a name="licensing"></a>
This code can be used under the MIT license. Feel free to use the code, changing any of my personal information (name, experience, links, etc.) to your own.
