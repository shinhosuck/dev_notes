
from django.shortcuts import render
from django.http import JsonResponse
import psycopg2
from .models import Car
from django.db.models import Count


def queryset_view(request):

    connection = psycopg2.connect(
        database = 'test',
        user = 'postgres',
        password = 'march232014',
        host = 'localhost',
        port = '5432'
    )

    cursor = connection.cursor()

    cursor.execute('SELECT car_make, COUNT(*) as make_count FROM postgresql_car GROUP BY car_make ORDER BY car_make')

    data = cursor.fetchall()

    data_list = []
    keys = ['make', 'make_count']

    for obj in data:
        data_list.append(dict(zip(keys, list(obj))))
    
    context = {'qs': data_list}

    return JsonResponse(context)


def person_detail_view(request, id):

    connection = psycopg2.connect(
        database = 'test',
        user = 'postgres',
        password = 'march232014',
        host = 'localhost',
        port = '5432'
    )

    cursor = connection.cursor()

    cursor.execute(f'SELECT * FROM postgresql_car WHERE id={id}')

    keys = [data.name for data in cursor.description]

    values = cursor.fetchone()
    context = {}

    if values:
        for index in range(0, len([data.name for data in cursor.description])):
            context[keys[index]] = values[index]
    else:
        context['message'] = 'No data available'
        
    return JsonResponse(context)


def delete_view(request, id):

    connection = psycopg2.connect(
        database = 'test',
        user = 'postgres',
        password = 'march232014',
        host = 'localhost',
        port = '5432'
    )

    cursor = connection.cursor()

    cursor.execute(f'DELETE FROM person WHERE id={id}')

    result = connection.commit()

    context = {
        'message': 'Person deleted'
    }
    return JsonResponse(context)

def cars_view(request):

    connection = psycopg2.connect(
        database = 'test',
        user = 'postgres',
        password = 'march232014',
        host = 'localhost',
        port = '5432'
    )

    cursor = connection.cursor()

    cursor.execute('SELECT * FROM car')

    qs = cursor.fetchall()

    keys = [key.name for key in cursor.description]

    car_list = []

    for car in qs:
        car_list.append(dict(zip(keys, car)))

    context = {
        'car_list': car_list
    }

    return JsonResponse(context, status=200)

def get_model_data(request):
    # cars = Car.objects.values('car_make').annotate(make_count=Count('car_make'))
    cars = Car.objects.aggregate(Count('car_make'))
    print(cars)
    return JsonResponse({'message': 'Data fetched'})
