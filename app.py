import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, render_template

postgres = 'postgres'
password = 'postgres'

#################################################
# Database Setup
#################################################
engine = create_engine(
    f"postgres://{postgres}:{password}@localhost:5432/Project_2")
conn = engine.connect()

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return render_template("index.html")


    # return (
    #     f"Available Routes:<br/>"

    #     f"/indeed<br/>"
    #     f"/Job_Type<br/>"
    # )


@app.route("/indeed")
def indeed():
    # # Create our session (link) from Python to the DB
    # session = Session(engine)

    # Query all data
    results = pd.read_sql("SELECT * FROM indeed", conn)

    P2 = results.to_dict(orient='records')
    # session.close()

    # # Convert list of tuples into normal list
    # all_names = list(np.ravel(results))

    # return jsonify(all_names)
    return jsonify(P2)


@app.route("/Job_Type")
def Job_Type():
    # # Create our session (link) from Python to the DB
    # session = Session(engine)

    # Query all data
    results1 = pd.read_sql("SELECT * FROM job_type", conn)

    Job_Type = results1.to_dict(orient='records')
    # session.close()

    # # Convert list of tuples into normal list
    # all_names = list(np.ravel(results))

    # return jsonify(all_names)
    return jsonify(Job_Type)


@app.route("/heran")
def heran():
    # # Create our session (link) from Python to the DB
    # session = Session(engine)

    # Query all data
    results2 = pd.read_sql("SELECT * FROM indeed", conn)

    heran = results2.to_dict(orient='records')
    # session.close()

    # # Convert list of tuples into normal list
    # all_names = list(np.ravel(results))

    # return jsonify(all_names)
    return jsonify(heran)

if __name__ == '__main__':
    app.run(debug=True)

