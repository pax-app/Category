from project.api.models import GeneralCategory, ProviderCategory, Context
from flask import request, jsonify, Blueprint
from sqlalchemy import exc

category_blueprint = Blueprint('category', __name__)


@category_blueprint.route('/general', methods=['GET'])
def get_general_categories():
    context = Context(GeneralCategory())

    categories = []
    for GENERAL_CATEGORY in GeneralCategory.query.all():
        category = context.return_json(category=GENERAL_CATEGORY)
        categories.append(category)

    return jsonify({
        'status': 'success',
        'data': {
            'categories': categories
        }
    })


@category_blueprint.route('/provider', methods=['GET'])
def get_provider_categories():
    context = Context(ProviderCategory())

    categories = []
    for PROVIDER_CATEGORY in ProviderCategory.query.all():
        category = context.return_json(category=PROVIDER_CATEGORY)
        categories.append(category)

    return jsonify({
        'status': 'success',
        'data': {
            'categories': categories
        }
    })


@category_blueprint.route('/provider/<general_category_id>', methods=['GET'])
def get_specific_provider_categories(general_category_id):
    context = Context(ProviderCategory())

    categories = []
    for PROVIDER_CATEGORY in ProviderCategory.query.filter_by(general_category_id=(general_category_id)):
        category = context.return_json(category=PROVIDER_CATEGORY)
        categories.append(category)

    if len(categories) == 0:
        response = {
            'status': 'failed',
            'error': "ID Not Found"
        }
        return jsonify(response), 404

    response = {
        'status': 'success',
        'data': {
            'categories': categories
        }
    }
    return jsonify(response), 200
