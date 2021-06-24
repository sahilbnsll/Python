# Problem 7. Finding word in the post

post = '''India, our country is a huge and beautiful land full of wonders. From the Himalayas to the Indian Ocean, Desert of Thar in the snowy mountains of Sikkim, it is a country full of beautiful landscapes and beautiful people. India is a unique country with diversity. "Unity is diversity" is the main slogan of the country.'''
word = "india"
if(word in post.lower()):
    print("This post is about India")
else:    
    print("This post is not about India")