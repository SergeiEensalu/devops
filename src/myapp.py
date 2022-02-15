from flask import Flask

app = Flask("__name__")

@app.route("/")
def index():
    return "Hello, Estonia!"

@app.route("/ping")
def pong():
    return "Pong"

if __name__ == "__main__":
    app.run(debug=True)


    # 1)heroku login
    # 2)heroku autorizations:create
    # 3) take token
    # 4) github -> sdettings -> secretc -> action secrets -> new secret -> HEROKU_API_TOKEN -> add secret
    # 5) heroku -> copy aplicaton name  -> github -> sdettings -> secretc -> action secrets -> new secret -> HEROKU_APP_NAME -> add secret
    # 6) need be two secrets in github
    #
    #
    # 8) dobavit wto to tipo 'fetch all history for tags' v yml file
    #