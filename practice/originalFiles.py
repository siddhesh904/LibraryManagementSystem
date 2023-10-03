import requests
number = int(input("Enter The Number:"))
api_url = f"https://frappe.io/api/method/frappe-library?page={number}&title=and"
response = requests.get(api_url)
data = response.json()

# for i in data['message']:
#     print(i['bookID'])

l1 = ['bookID', 'title', 'authors', 'average_rating', 'isbn', 'isbn13','language_code', 'ratings_count', 'text_reviews_count', 'publication_date', 'publisher' ]
for i in data['message']:
    for j in l1:
        print(i[j])
    print("\n")


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
