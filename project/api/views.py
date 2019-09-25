from flask import request, jsonify, Blueprint

category_blueprint = Blueprint('category', __name__)


@category_blueprint.route('/category/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
