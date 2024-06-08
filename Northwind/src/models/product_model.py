class ProductModel:

    def __init__(self, id, name, price, stock, image):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        self.image = image # image file

    # Validating a new product insert:
    def validate_insert(self):
        if not self.name: return "Missing name."
        if not self.price: return "Missing price."
        if not self.stock: return "Missing stock."
        if not self.image: return "Missing image."
        if len(self.name) < 2 or len(self.name) > 100: return "name length must be 2 - 100 chars."
        if float(self.price) < 0 or float(self.price) > 1000: return "price must be 0 - 1000."
        if int(self.stock) < 0 or int(self.stock) > 1000: return "stock must be 0 - 1000."
        return None # No error.

    # Validating an existing product update:
    def validate_update(self):
        if not self.id: return "Missing id."
        if not self.name: return "Missing name."
        if not self.price: return "Missing price."
        if not self.stock: return "Missing stock."
        if len(self.name) < 2 or len(self.name) > 100: return "name length must be 2 - 100 chars."
        if float(self.price) < 0 or float(self.price) > 1000: return "price must be 0 - 1000."
        if int(self.stock) < 0 or int(self.stock) > 1000: return "stock must be 0 - 1000."
        return None # No error.

