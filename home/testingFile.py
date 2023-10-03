from home.models import *
# import requests
# api_url = f"https://frappe.io/api/method/frappe-library?page=2&title=and"
# response = requests.get(api_url)
# data = response.json()
# # for i in data['message']:
# #     print(i)


# print(type(data))

# for i in data:
#     print("only Data itreate:", i)

# for i in data['message']:
#     print("Data['message']", i)

# for i, item in data.items():
#     print("only print i", i)
#     print("only print item ", item)


# for i, item in data.items():
#     for j in item:
#         print(f"{i} : {j['title']}")


# for i, item in data.items():
#     for j in item:
#         print(j['bookID'])


# print("Second Itreate")
# # i is message
# # item is dictionary
# # if I am print the each item then use the loop
# ''' for i , item in data.items():
#         print(i)
#         for j in item:
#             print(j)'''


# for i, item in data.items():
#     print(i)
#     for j in item:
#         print(j)# each diectionary value print.
#         '''for example:{'bookID': '890', 'title': 'Of Mice and Men', 'authors': 'John Steinbeck', 'average_rating': '3.87', 'isbn': '0142000671', 'isbn13': '9780142000670', 'language_code': 'eng', '  num_pages': '103', 'ratings_count': '1755253', 'text_reviews_count': '25554', 'publication_date': '1/8/2002', 'publisher': 'Penguin Books'}'''



# for i, item in data.items():
#     for j in item:
#         print('bookID:', j['bookID'])
#         print('title:', j['title'])
#         print('authors:', j['authors'])
#         print('average_rating:', j['average_rating'])
#         print('isbn:', j['isbn'])
#         print('language_code:', j['language_code'])
#         print('ratings_count:', j['ratings_count'])
#         print('ratings_count:', j['ratings_count'])
#         print('text_reviews_count:', j['text_reviews_count'])
#         print('publisher:', j['publisher'])
#         print("\n \n")

#         # print('num_pages',j['num_pages'])

# import requests
# data = ""
# for i in range(1, 10+1):
#     api_url = f"https://frappe.io/api/method/frappe-library?page={i}&title=and"
#     response = requests.get(api_url)
#     data = response.json()

#     l1 = ['bookID', 'title', 'authors', 'average_rating', 'isbn', 'isbn13','language_code', 'ratings_count', 'text_reviews_count', 'publication_date', 'publisher' ]
#     for i in data['message']:
#         for j in l1:
#             f = open('text2.txt', 'a') 
#             context = f.write(f'{i[j]} \n\n')
#             print('\n\n')
#         print("\n\n")

import requests
import random

def seed_db(): 
    for i in range(1, 35+1):
        api_url = f"https://frappe.io/api/method/frappe-library?page={i}&title=and"
        response = requests.get(api_url)
        data = response.json()

        for item in data['message']:
            # Convert average_rating to a float or set a default value if conversion fails
            try:
                average_rating = float(item['average_rating'])
            except (ValueError, TypeError):
                average_rating = 0.0  # Set a default value, you can change it as per your requirements
            
            # Create FetchBook objects with the converted average_rating
            queryset = FetchBook.objects.create(
                book_id = item['bookID'],
                title = item['title'],
                authors = item['authors'],
                average_rating = average_rating,  # Use the converted value here
                isbn = item['isbn'],
                isbn13 = item['isbn13'],
                language_code = item['language_code'],
                ratings_count = item['ratings_count'],
                text_reviews_count = item['text_reviews_count'],
                publication_date = item['publication_date'],
                publisher = item['publisher'],
                amount = random.randint(100, 1000)
            )


