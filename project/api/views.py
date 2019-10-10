from project.api.models import GeneralCategory, ProviderCategory, Works
from flask import request, jsonify, Blueprint
from database import db
from sqlalchemy import exc

category_blueprint = Blueprint('category', __name__)


@category_blueprint.route('/general', methods=['GET'])
def get_general_categories():
    return jsonify({
        'status': 'success',
        'data': {
            'categories': [GENERAL_CATEGORY.to_json() for GENERAL_CATEGORY in GeneralCategory.query.all()]
        }
    })


@category_blueprint.route('/provider', methods=['GET'])
def get_provider_categories():
    return jsonify({
        'status': 'success',
        'data': {
            'categories': [PROVIDER_CATEGORY.to_json() for PROVIDER_CATEGORY in ProviderCategory.query.all()]
        }
    })


@category_blueprint.route('/<general_category_id>/provider', methods=['GET'])
def get_specific_provider_categories(general_category_id):
    provider_categories = [PROVIDER_CATEGORY.to_json() for PROVIDER_CATEGORY in ProviderCategory.query.filter_by(general_category_id=(general_category_id))]

    if not provider_categories:
        response = {
            'status': 'failed',
            'error': "ID Not Found"
        }
        return jsonify(response), 404

    response = {
        'status': 'success',
        'data': {
            'categories': provider_categories
        }
    }
    return jsonify(response), 200
