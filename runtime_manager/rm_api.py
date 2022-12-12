'''
This is the entry point to contact the Runtime Manager for load balancing purposes
This is a communication interface RM to RM only
'''

from runtime_manager.receiver import Receiver
from runtime_manager.utility.file_reader import File_Reader 
from runtime_manager.utility.paths import Paths
from flask import Flask
from flask_restful import Api
import json

app = Flask(__name__)
api = Api(app)

#  TODO inserire i dati nel file di config
api.add_resource(Receiver, json.loads((File_Reader.read_file(Paths.COMM.value)))['rest']['endpoint']) #    endpoint to trigger the RM

if __name__ == '__main__':
    app.run(debug=True)  #  run Flask app
