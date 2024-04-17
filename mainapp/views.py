from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
import requests
from django import template
from .models import Cat
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

register = template.Library()


def card_list_view(request):
    first_ten_objects = Cat.objects.all()
    catObjectList = []
    # Access data from each object
    for row in first_ten_objects:
        # Access other fields as needed
        picture_object = {"id_cat": row.id_cat, "breed": row.breed, 'url': row.url, 'width': row.width,
                          'height': row.height, "rating": row.rating}
        catObjectList.append(picture_object)

    widthHeightAverageList = calculate_average_picture_size(catObjectList)
    if len(widthHeightAverageList) > 1:
        context = {'catObjectList': catObjectList, "width": widthHeightAverageList[0],
                   "height": widthHeightAverageList[1]}
    else:
        context = {'catObjectList': catObjectList, "width": 400, "height": 500}

    return render(request, 'card_list_view.html', context)


def calculate_average_picture_size(dictionary):
    width_list = []
    height_list = []
    widthHeightAverageList = []

    for row in dictionary:
        width_list.append(row["width"])
        height_list.append(row["height"])

    if len(width_list) != 0 & len(height_list) != 0:
        widthAverage = sum(width_list) / len(width_list)
        heightAverage = sum(height_list) / len(height_list)
        widthHeightAverageList.append(widthAverage)
        widthHeightAverageList.append(heightAverage)
    return widthHeightAverageList


def add_to_database():
    api_key = "live_z9FUEmi4GQZkgmcmIWPt3vCbKA2B5QFJG0iknwB98JCvzplGjs6Yx4oPCVOdUn5m"
    headers = {
        'Authorization': 'Token ' + api_key
    }
    base_url = 'https://api.thecatapi.com/v1/images/search'

    numberOfPics = 3
    pictureList = []

    # Call the API 10 times
    for _ in range(20):
        response = requests.get(base_url, headers=headers)

        # Check for successful response (status code 200)
        if response.status_code == 200:
            data = response.json()
            # Assuming data is a list with one element (image object)
            image_url = data[0]['url']
            pictureList.append(image_url)
            new_cat = Cat(id_cat=data[0]['id'],
                          url=data[0]['url'],
                          breed="Siamese",
                          height=data[0]['height'],
                          width=data[0]['width'])
            new_cat.save()
        else:
            print(f"Error: {response.status_code}")


def cat_page_view(request):
    uniqueCatId = request.GET.get('id_cat')
    cat = Cat.objects.get(id_cat=uniqueCatId)
    show_modal = True
    context = {"id_cat": cat.id_cat, "breed": cat.breed, "rating": cat.rating, "url": cat.url, "name": cat.name,
               "width": cat.width, "height": cat.height, "show_modal": show_modal}
    return render(request, 'single_card_view.html', context)


def rate_cat(request):
    if request.method == 'POST':  # Adjust method if necessary
        data = json.load(request)
        catObject = data.get('catObject')
        cat_rating = catObject['catRating']
        cat_id = catObject.get('catId')

        cat_to_update = Cat.objects.get(id_cat=cat_id)
        cat_to_update.rating = cat_rating
        cat_to_update.save()

        return JsonResponse({'message': 'Function called successfully!'})  # Example response
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
