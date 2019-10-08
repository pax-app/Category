from project.api.models import GeneralCategory, ProviderCategory, Works
from flask import request, jsonify, Blueprint
from database import db

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


@category_blueprint.route('/<general_category_id>/provider', methods=['GET'])
def get_specific_provider_categories(general_category_id):
    response = {
        'status': 'success',
        'data': {
            'categories': [PROVIDER_CATEGORY.to_json() for PROVIDER_CATEGORY in ProviderCategory.query.filter_by(general_category_id=(general_category_id))]
        }
    }
    return jsonify(response), 200


@category_blueprint.route('/<provider_id>/category_provider/<provider_category_id>', methods=['DELETE'])
def remove_category_provider_relationship(provider_id, provider_category_id):
    error_response = {
        'status': 'fail',
        'message': 'Relationship Not Found'
    }

    works = Works.query.filter_by(
        provider_category_id=int(provider_category_id), provider_id=int(provider_id)).first()

    if not works:
        return jsonify(error_response), 404

    db.session.delete(works)
    db.session.commit()

    response = {
        'status': 'success',
        'data': {
            'message': 'Relationship deleted!'
        }
    }

    return jsonify(response), 200
