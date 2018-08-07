from flask import Blueprint
from api.restful import Api


api_1_bp = Blueprint('api_1', __name__, url_prefix='/api/v1')

api_1 = Api(api_1_bp)


from .conditions import Conditions

api_1.add_resource(Conditions, 'conditions')
