from main import search, list_user_products, list_products_per_tag, add_product_to_catalog, update_stock, remove_product, purchase_product

# Run this functions to test the database

search("stoel")
print("--------------------------")
list_user_products(1)
print("--------------------------")
list_products_per_tag(2)
print("--------------------------")
add_product_to_catalog(2, "test", "test", 10, 4, 3)
print("--------------------------")
update_stock(2, 10)
print("--------------------------")
remove_product(4)
print("--------------------------")
purchase_product(2, 2, 1)
