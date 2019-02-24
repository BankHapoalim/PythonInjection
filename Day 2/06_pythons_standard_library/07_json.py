from json import loads, dumps

weather_json_string = """{
   "city":{
      "id":1851632,
      "name":"Shuzenji",
      "coord":{
         "lon":138.933334,
         "lat":34.966671
      },
      "list":[
         {
            "dt":1406106000,
            "main":{
               "temp":298.77,
               "temp_min":298.77,
               "temp_max":298.774,
               "pressure":1005.93,
               "sea_level":1018.18,
               "grnd_level":1005.93,
               "humidity":87,
               "temp_kf":0.26,
               "accuracy":null
            }
         }
      ]
   }
}"""

# Turn a JSON string into a python objects/data-types:
weather_dict = loads(weather_json_string)
print(weather_dict)


python_mixed_data = {
    "python_list": [1, 2, 3],
    "int": 1337,
    "float": 192.15,
    "other_types": [None, False, True]
}
json_mixed_data = dumps(python_mixed_data)
print(json_mixed_data)
