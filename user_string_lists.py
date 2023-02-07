"""
Modify this docstring.

"""

import random

Advert_types=['Social Media', 'Digital Marketing', 'Digital billboard', 'Radio advert', 'TV Advert', 'Newspaper', 'flyers', 'refferals']

Products= ['cars', 'electronics', 'fashion', 'vacation', 'restaurants','homes', 'hotels', 'drinks']

Target_audience=['children', 'youths', 'adults', 'students', 'parents', 'workers', 'travelers', 'drivers']

advert_medium=['paper', 'steel', 'internet', 'TV', 'Radio', 'Phones', 'Computers', 'posters']

ad_locations=['roadside','airport', 'home', 'sports centers', 'schools', 'hotels','malls', 'cinema']

#String Lists 1. Using Python Built-in Functions 

len_ad_type=len(Advert_types)
len_product=len(Products)
len_ad_med=len(advert_medium)
len_targ_aud=len(Target_audience)
len_ad_loc=len(ad_locations)
#len
print('The lenght of advert type is:', len_ad_type)
print('The lenght of products is:', len_product)
print('the lenght of target audience is :', len_targ_aud)
print('the lenght of advert medium is:,', len_ad_med)
print('the lenght of ad locations is: ', len_ad_loc)

#set
set_ad_location= set(ad_locations)
print('The set of ad locations are:', set_ad_location)

#ZIP
zip_list= zip(Advert_types,Products)
print('The zipped list are:', zip_list)

#String Lists 2. Random Choice

random_ad_types=random.choice(Advert_types)
print('This is a random advert type suggested:', random_ad_types)
print()
print()


#String Lists 3. Get Unique Words
with open ("text_simple.txt", "r") as file:
    text=file.read()
    list_words = text.split()
    unique_words=set(list_words)

print('Unique words was gotten from the simple file.')

#sorting

sorted_words=sorted(unique_words)
lenght_unique_words=len(unique_words)
print('The lenght of the unique words is:', lenght_unique_words)

# reusable functions next

# call functions and execute code
# use if __name__ == "__main__":
