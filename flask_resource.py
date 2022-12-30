# # Basic Flask App

# from flask import Flask
from flasgger import LazyJSONEncoder, LazyString, Swagger, swag_from
from flask import Flask, request
import os
# # Create app
# app = Flask(__name__)

# # Create function with result sent to UI. 
# # Also use a class method to route the function 
# @app.route('/')
# def hello():
#     return 'Hello World'

# if __name__ == '__main__':
#    app.run(debug=True, host="0.0.0.0")
#    # app.run(debug=True, host="0.0.0.0", port=5000)

# # Within folder of flask app, run following command in terminal
# # $ export FLASK_APP=flask_resource.py
# # $ export FLASK_ENV=development

# # Then run 
# # $ flask run 
app = Flask(__name__)
app.json_encoder = LazyJSONEncoder


swagger_template = dict(
    info={
        "title": LazyString(lambda: "Matching ODEM Job Opportunities"),
        "version": LazyString(lambda: "0.1"),
        "description": LazyString(
            lambda: "This document depicts the usuage of cosine similarities to match available jobs on the ODEM Platform"
        ),
    },
    host=LazyString(lambda: request.host))


swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "career-opportunities",
            "route": "/job_match.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        },
            # {
            #     "endpoint": "career-pathway",
            #     "route": "/job_match.json",
            #     "rule_filter": lambda rule: True,
            #     "model_filter": lambda tag: True,
            # },
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/"}
swagger = Swagger(app, template=swagger_template, config=swagger_config)

def run_app(app):


    @app.route('/')
    def index():
        return 'TESTING TESTING 123   456 789 10'




    @swag_from("hello_world.yml", methods=["GET"])
    @app.route("/career-opportunities/<int:x_input>/")
    def hello_world(x_input):
        user_job_search_matches = sample(x_input)
        if request.method == "GET":

            return {"All Jobs": [user_job_search_matches]}

        # elif request.method == "POST":
        #     return {
        #         "message": "Create an entity",
        #         "method": request.method,
        #         "body": request.json,
        #     }
        



    def sample(x_input):
        return f'The input {x_input}'


    return app

app = run_app(app)

if __name__ == '__main__':
   app.run(debug=True, host="0.0.0.0")
    # app.run(debug=True, host="0.0.0.0", port=80)

    # app.run(debug=True, host="0.0.0.0", port=8080)
   # app.run(debug=True, host="0.0.0.0", port=5000)
    # app.run(debug=True, host="0.0.0.0", port=int(os.environ.get('PORT', 8080)))