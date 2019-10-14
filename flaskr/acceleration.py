from flask import Blueprint, request

bp = Blueprint('acceleration', __name__)

@bp.route('/acceleration', methods=('POST'))
def acceleration():
    accel_data = open('acceleration_data.txt', 'w+')
    json = request.get_json()
