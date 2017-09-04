import os

__author__ = 'Ankit Joshi'

# OPENFACE CONSTANTS
openface = {
    'CLASSIFIER_MODEL': os.path.abspath(os.path.dirname(__file__)) + '/data/feature/classifier.pkl',
    'FEATURE_DIR': os.path.abspath(os.path.dirname(__file__)) + '/data/feature',
    'RAW_DIR': os.path.abspath(os.path.dirname(__file__)) + '/data/raw',
    'ALIGNED_DIR': os.path.abspath(os.path.dirname(__file__)) + '/data/align',
    'MAIN_LUA_SCRIPT': 'openface/batch-represent/main.lua',
    'CLASSIFIER': 'LinearSvm'
}

# FLASK CONSTANTS
flask = {
    'INSTANCE_DIR': os.path.abspath(os.path.dirname(__file__)) + '/instance'
}

# STRING_CONSTANTS
string = {
    'SUCCESS': 'SUCCESS',
    'USER_EXISTS': 'This user already exists',
    'MISSING_ARGS': 'Username or Password is empty',
    'USER_DOESNT_EXISTS': 'User with the given id doesn\'t exists'
}

# HTTP_STATUS_CODES
status = {
    'OK': 200,
    'BAD_REQUEST': 400
}
