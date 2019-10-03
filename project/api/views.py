from project.api.models import GeneralCategory
from project.api.models import ProviderCategory
from flask import request, jsonify, Blueprint

general_category_blueprint = Blueprint('general', __name__)
provider_category_blueprint = Blueprint('provider', __name__)


@category_blueprint.route('/category/all', methods=['GET'])
def get_categories():
    return jsonify({
        'status': 'success',
        'general': {
            'categories': [PROVIDER_CATEGORY.to_json() for PROVIDER_CATEGORY in ProviderCategory.query.all()]
        },
        'provider': {
            'categories': [GENERAL_CATEGORY.to_json() for GENERAL_CATEGORY in GeneralCategory.query.all()]
        }
    })
