#!flask/bin/python

from app import app, make_response, jsonify


@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)
