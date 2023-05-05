__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

import models
from models import db
from test_data import tag_data, user_data, product_data, transaction_data


def populate_test_database():
    tag_data()
    user_data()
    product_data()
    transaction_data()


def search(term):
    # retrive all data of a product and store them in a dict
    query = models.Product.select().where((models.Product.product_name.contains(term))
                                          | (models.Product.description.contains(term))).dicts()
    print("The search results are (the full dict!):")
    for product in query:
        print(product)


def list_user_products(user_id):
    # retrive all data of a product of 1 user and store them in a dict
    user = models.User.select().where(models.User.id == user_id)
    name = []
    for i in user:
        name.append(i.user_name)
    query = models.Product.select().where(
        models.Product.user_name == name)
    print("The list of products per user are:")
    for product in query:
        print(product.product_name)


def list_products_per_tag(tag_id):
    # retrive all data of a product with specific tag and store them in a dict
    products = models.Tag.select().where(models.Tag.id == tag_id)
    tag = []
    for i in products:
        tag.append(i.name_tag)
    query = models.Product.select().where(
        models.Product.name_tag == tag)
    print("The list of products per tag:")
    for product in query:
        print(product.product_name)


def add_product_to_catalog(user_id, product, description, price, quantity, tag_id):
    # add a new product

    # first find the user
    user = models.User.select().where(models.User.id == user_id)
    name = []
    for i in user:
        name.append(i.user_name)

    # then find the tag
    products = models.Tag.select().where(models.Tag.id == tag_id)
    tag = []
    for i in products:
        tag.append(i.name_tag)

    # create the product
    models.Product.create(product_name=product, description=description, price_unit=price,
                          quantity_in_stock=quantity, user_name=name[0], name_tag=tag[0])
    print("product is created")


def update_stock(product_id, new_quantity):
    # update the quantity of the product
    q = (models.Product.update({models.Product.quantity_in_stock: new_quantity}).where(
        models.Product.id == product_id))
    q.execute()

    print("product stock is updated")


def purchase_product(product_id, buyer_id, quantity):
    # purchase the product
    user = models.User.select().where(models.User.id == buyer_id)
    name = []
    for i in user:
        name.append(i.user_name)
    models.Transaction.create(
        user_buy=name[0], purchased_product=product_id, quantity=quantity)

    print("product is bought")

    # update number in stock by seller
    q = (models.Product.update({models.Product.quantity_in_stock: models.Product.quantity_in_stock-quantity}).where(
        models.Product.id == product_id))
    q.execute()

    print("quantity in stock is updated")


def remove_product(product_id):
    user = models.Product.get(models.Product.id == product_id)
    user.delete_instance()

    print("product is deleted")


if __name__ == "__main__":
    db.connect()
    db.create_tables([models.Tag, models.Product, models.User,
                     models.Transaction], safe=True)
    populate_test_database()
