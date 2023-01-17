from typing import Tuple, Union

from flask import Blueprint

from app.storage import load_data

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.get('/products')
def products() -> list:
    return load_data()


@bp.get('/products/<int:product_id>')
def product(product_id: int) -> Union[dict, Tuple[dict, int]]:

    for prod in load_data():
        if prod['id'] == product_id:
            return prod

    return {'message': f'product with id {product_id} does not exist.'}, 404
