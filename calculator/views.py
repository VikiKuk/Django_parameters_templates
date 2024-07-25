from django.http import HttpResponse
from django.shortcuts import render


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },

}

def calculator(request, recipe_name = '', count=1):
    modyfied_recipe = {}
    if recipe_name in DATA:
        for ingredient, amount in DATA[recipe_name].items():
            modyfied_recipe[ingredient] = amount * count
    context = {
      'recipe':  modyfied_recipe
    }

    return render(request, 'calculator/index.html', context)
