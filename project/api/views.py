from project.api.models import GeneralCategory
from project.api.models import ProviderCategory
from flask import request, jsonify, Blueprint

general_category_blueprint = Blueprint('general', __name__)
provider_category_blueprint = Blueprint('provider', __name__)


@general_category_blueprint.route('/general/category', methods=['GET'])
def get_general_categories():
    return jsonify({
        'status': 'success',
        'general': {
            'category': [GENERAL_CATEGORY.to_json() for GENERAL_CATEGORY in GeneralCategory.query.all()]
        }
    })


@provider_category_blueprint.route('/provider/category', methods=['GET'])
def get_provider_categories():
    return jsonify({
        'status': 'success',
        'provider': {
            'category': [PROVIDER_CATEGORY.to_json() for PROVIDER_CATEGORY in ProviderCategory.query.all()]
        }
    })
