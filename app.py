from flask import Flask, render_template, jsonify
import json
import pandas as pd
import os
import certifi

app = Flask(__name__)

# landing page
@app.route('/')
def index():
    # render an index.html template and pass it the data you retrieved from the database
    # this is the main page
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
