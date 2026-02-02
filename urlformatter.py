def generate_product_slug(product_name):
    #Convert to loser and replaces spaces with hyphens
    slug = product_name.lower().replace(" ","-")
    return slug

URL = input()
result = generate_product_slug(URL)
print(result)