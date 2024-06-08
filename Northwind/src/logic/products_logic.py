from utils.dal import DAL
from utils.image_handler import ImageHandler

class ProductsLogic:

    # ctor - creating the DAL:
    def __init__(self):
        self.dal = DAL()

    # Get all products: 
    def get_all_products(self):
        sql = "SELECT * FROM products"
        return self.dal.get_table(sql)
    
    # Get one product: 
    def get_one_product(self, id):
        sql = "SELECT * FROM products WHERE id = %s"
        return self.dal.get_scalar(sql, (id, )) # (id, ) --> Tuple
       
    # Add new product: 
    def add_product(self, product):
        image_name = ImageHandler.save_image(product.image)
        sql = "INSERT INTO products(name, price, stock, image_name) VALUES(%s, %s, %s, %s)"
        self.dal.insert(sql, (product.name, product.price, product.stock, image_name))

    # Update existing product: 
    def update_product(self, product):
        old_image_name = self.__get_old_image_name(product.id)
        image_name = ImageHandler.update_image(old_image_name, product.image)
        sql = "UPDATE products SET name=%s, price=%s, stock=%s, image_name=%s WHERE id=%s"
        self.dal.update(sql, (product.name, product.price, product.stock, image_name, product.id))

    # Delete existing product:
    def delete_product(self, id):
        image_name = self.__get_old_image_name(id)
        ImageHandler.delete_image(image_name)
        sql = "DELETE FROM products WHERE id=%s"
        self.dal.delete(sql, (id, ))

    def __get_old_image_name(self, id):
        sql = "SELECT image_name FROM products WHERE id=%s"
        result = self.dal.get_scalar(sql, (id, ))
        return result["image_name"]

    # Close connection:
    def close(self):
        self.dal.close()

    