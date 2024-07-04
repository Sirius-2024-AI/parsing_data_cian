#!/usr/bin/env python3
# import libs
import cianparser

# open file with cities
file = open("cities.ini", "r")
cities = file.readlines()
file.close()

# parsing loop
for city in cities:
    city = city.replace("\n", "") # del \n in string
    city_parser = cianparser.CianParser(location=city)
    data = city_parser.get_flats(deal_type="sale", rooms=("all"), with_extra_data=True, with_saving_csv=True, additional_settings={"start_page":1, "end_page":54})
    # create a flag file indicating the completion of parsing work with this city
    city_flag = open(city + ".done", "w") 
    city_flag.close()
    
print("Done! Check files!")
