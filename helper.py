import data
import requests
import urls


def change_data_create_user(key, value):
    body = data.CREATE_USER_BODY.copy()
    body[key] = value

    return body

def get_list_random_ingredients(count):
    ingredients = []
    for i in range(count):
        request = requests.get(urls.BASE_URL + urls.GET_INGREDIENTS)
        ingredient = request.json()["data"][i]["_id"]
        ingredients.append(ingredient)

    return ingredients
