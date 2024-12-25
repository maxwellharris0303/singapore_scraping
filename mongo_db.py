from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017")

db = client["betting"]
collection = db["match_schedule"]

def data_save(first_team, second_team, match_date, match_time, game_total):

    query_to_find = {
        "first_team": first_team,
        "second_team": second_team
    }
    documents_to_find = collection.find(query_to_find)
    if len(list(documents_to_find)) != 0:

        update_data = {'$set': {'match_date_time': match_date + " " + match_time, "game_total": game_total}}
        collection.update_one(query_to_find, update_data)

        return "Updated"
    
    # query_to_find = {
    #     "first_team": first_team,
    #     "second_team": second_team,
    #     "match_date_time": match_date + " " + match_time,
    #     "game_total": game_total
    # }
    # documents_to_find = collection.find(query_to_find)
    # if len(list(documents_to_find)) != 0:
    #     return "Existed"
    
    data_document = {
        "first_team": first_team,
        "second_team": second_team,
        "match_date_time": match_date + " " + match_time,
        "game_total": game_total
    }
    collection.insert_one(data_document)
    query = {
        "first_team": first_team,
        "second_team": second_team
    }
    documents = collection.find(query)
    if len(list(documents)) != 0:
        return True
    else:
        return False
    
def get_nearest_date():
    match_dates = collection.distinct("match_date_time")

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Filter out dates that are in the past
    future_dates = [date for date in match_dates if datetime.strptime(date, "%Y-%m-%d %H:%M") >= datetime.strptime(current_time, "%Y-%m-%d %H:%M")]
    # print(future_dates)
    # Find the future date closest to the current date
    closest_date = min(future_dates, key=lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M") - datetime.strptime(current_time, "%Y-%m-%d %H:%M"))
    # Display the closest future date
    # print("Closest Future Date:", closest_date)
    
    return closest_date

def get_match_data(time):
    query = {"match_date_time": time}
    documents = collection.find(query)

    first_team_name_array = []
    second_team_name_array = []
    game_total_array = []
    for document in documents:
        document['_id'] = str(document['_id'])
        # print(document)
        first_team_name_array.append(document["first_team"])
        second_team_name_array.append(document["second_team"])
        game_total_array.append(document["game_total"])
    # print(array)
    return first_team_name_array, second_team_name_array, game_total_array

def get_all_match_data():
    first_team_name_array = []
    second_team_name_array = []
    game_total_array = []
    match_date_time_array = []

    documents = collection.find()
    for document in documents:
        # document['_id'] = str(document['_id'])
        # print(document)
        first_team_name_array.append(document["first_team"])
        second_team_name_array.append(document["second_team"])
        game_total_array.append(document["game_total"])
        match_date_time_array.append(document["match_date_time"])

    return first_team_name_array, second_team_name_array, game_total_array, match_date_time_array

    
# print(data_save("aaa", "bbb", "ccc", "ddd", "eee"))
# print(get_match_data(get_nearest_date()))
# print(get_all_match_data())