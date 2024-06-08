from logic.products_logic import ProductsLogic
from flask import request # Request object arrived from the frontend.
from models.product_model import ProductModel
from models.client_errors import ResourceNotFoundError, ValidationError

class ProductsFacade:

    # ctor - create the logic:
    def __init__(self):
        self.logic = ProductsLogic()

    # Get all products:
    def get_all_products(self):
        return self.logic.get_all_products()
    
    # Get one product:
    def get_one_product(self, id):
        product = self.logic.get_one_product(id)
        if not product: raise ResourceNotFoundError(id)
        return product
    
    # Add new product: 
    def add_product(self):
        name = request.form.get("name") # <input type="text" name="name" />
        price = request.form.get("price") # <input type="number" name="price" />
        stock = request.form.get("stock") # <input type="number" name="stock" />
        image = request.files["image"] # <input type="file" name="image" />
        product = ProductModel(None, name, price, stock, image)
        error = product.validate_insert()
        if error: raise ValidationError(error, product)
        self.logic.add_product(product)

    # Update existing product: 
    def update_product(self):
        id = request.form.get("id") # <input type="hidden" name="id" />
        name = request.form.get("name") # <input type="text" name="name" />
        price = request.form.get("price") # <input type="number" name="price" />
        stock = request.form.get("stock") # <input type="number" name="stock" />
        image = request.files["image"] # <input type="file" name="image" />
        product = ProductModel(id, name, price, stock, image)
        error = product.validate_update()
        if error: raise ValidationError(error, product)
        self.logic.update_product(product)

    # Delete existing product:
    def delete_product(self, id):
        self.logic.delete_product(id)

    # Close connection:
    def close(self):
        self.logic.close()
