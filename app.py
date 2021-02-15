from flask import Blueprint, Flask, g, jsonify, render_template, request, Response, redirect, url_for, send_from_directory
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
import helper
import os

# Configure application
app = Flask(__name__)


@app.route('/index', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():

    # get all projects from the database
    # zipped = helper.get_portfolio_content()

    # get the title content for the portfolio page
    # title_text = helper.get_title_content('portfolio')

    return render_template('/index.html',
                            # title_text=title_text,
                            # title="PROJECT PORTFOLIO",
                            id="index")
                            # projects=zipped)


# @app.route('/portfolio', methods=['POST', 'GET'])
# def portfolio():

#     # get all projects from the database
#     zipped = helper.get_portfolio_content()

#     # get the title content for the portfolio page
#     title_text = helper.get_title_content('portfolio')

#     return render_template('/index.html',
#                             title_text=title_text,
#                             title="PROJECT PORTFOLIO",
#                             id="portfolio",
#                             projects=zipped)


# @app.route('/about', methods=['POST', 'GET'])
# def about():

#     title_text = helper.get_title_content('about')

#     skills = helper.get_skill_content()

#     return render_template('/about.html',
#                             title_text=title_text,
#                             skills=skills,
#                             title="ABOUT ME",
#                             id="about")


@app.route("/robots.txt")
def robots():
    '''
    Add robots.txt file to avoid google indexing
    '''

    return send_from_directory(app.static_folder, request.path[1:])


if __name__ == '__main__':
    app.run()
