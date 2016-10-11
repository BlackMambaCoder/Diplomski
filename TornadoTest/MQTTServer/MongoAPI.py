import time

from pymongo import MongoClient


class MongoAPI:
    def __init__(self):
        pass

    client = MongoClient()
    db = client.raspDB

    DEBUG_TAG = "MongoAPI# "

    def store_temp(self, temperature):
        print self.DEBUG_TAG + "Store temperature: " + str(temperature)

        collection = self.get_ds18b20_collection()

        temp_obj = {
            "temperature": temperature,
            "date": time.time() * 1000,
            "unread": 1
        }

        print self.DEBUG_TAG + "Temperature object created"

        result = collection.insert_one(temp_obj)

        if result.inserted_id:
            print self.DEBUG_TAG + "Temperature object successfully inserted"
            return True

        print self.DEBUG_TAG + "Temperature object insert failed"
        return False

    def get_unread_temperature(self):
        collection = self.get_ds18b20_collection()

        cursor = collection.find({"unread": 1})

        if cursor.count() > 0:
            temp_list = []

            for temp_doc in cursor:
                del temp_doc["_id"]
                temp_list.append(temp_doc)
                break

            self.set_temp_unread_to_false(collection)

            return temp_list

        return []

    def set_temp_unread_to_false(self, collection):
        collection.update_many(
            {"unread": 1},
            {
                "$set": {"unread": 0}
            })

    def get_ds18b20_collection(self):
        return self.db.tempDS18B20
