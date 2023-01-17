from typing import List, Dict, Union

Products = List[Dict[str, Union[int, str, list]]]
ProductsSorted = Products


def order_products(products: Products) -> ProductsSorted:
    return sorted(products, key=lambda p: p['prices'][0])  # type: ignore
