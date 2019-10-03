from project.api.models import GeneralCategory
from project.api.models import ProviderCategory
from flask import request, jsonify, Blueprint

category_blueprint = Blueprint('category', __name__)


@category_blueprint.route('/general', methods=['GET'])
def get_general_categories():
    return jsonify({
        'status': 'success',
        'general': {
            'category': [GENERAL_CATEGORY.to_json() for GENERAL_CATEGORY in GeneralCategory.query.all()]
        }
    })


@category_blueprint.route('/provider', methods=['GET'])
def get_provider_categories():
    return jsonify({
        'status': 'success',
        'provider': {
            'category': [PROVIDER_CATEGORY.to_json() for PROVIDER_CATEGORY in ProviderCategory.query.all()]
        }
    })
