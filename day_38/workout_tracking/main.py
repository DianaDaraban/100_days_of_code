import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

nutritionix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

headers = {
    'x-app-id': os.getenv('NUTRITIONIX_APPLICATION_ID'),
    'x-app-key': os.getenv('NUTRITIONIX_API_KEY'),
}

exercising = True
while exercising:
    input_workout = input('Tell me which exercices you did: ')
    exercises_data =[]

    if input_workout.lower() == 'exit':
        break

    elif input_workout:
        params = {
            'query': input_workout,
            'weight_kg': 70,
            'height_cm': 170,
            'age': 40
        }
        nutritionix_auth = requests.post(url=nutritionix_endpoint, json=params, headers=headers)
        exercises_data = nutritionix_auth.json()['exercises']

    print(exercises_data)

    sheet_data = requests.get('https://api.sheety.co/cd82068654ddb2d88a38c602a9f952e2/myWorkouts/workouts').json()[
        'workouts']
    if len(exercises_data) > 0:
        for data in exercises_data:
            date = datetime.now().strftime('%d/%m/%Y')
            time = datetime.now().strftime('%H:%M:%S')
            new_data = {
                'workout': {'date': date,
                 'time': time,
                 'exercise': data['user_input'],
                 'duration': data['duration_min'],
                 'calories': data['nf_calories'],
                 'id': data['tag_id']}
            }

            sheet_data_post = requests.post(url='https://api.sheety.co/cd82068654ddb2d88a38c602a9f952e2/myWorkouts/workouts', json=new_data)
        exercising = False
    else:
        print('Type a workout or type "exit" for cancel!')
        exercising = True
