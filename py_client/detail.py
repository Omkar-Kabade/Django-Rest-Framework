import requests

# we wil  request something to the following endpoint to get the response

# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/products/1/"
get_response  = requests.get(endpoint) #API - get method
#we can send json data with above using json and form data using data 

# print(get_response.text) #prints raw response
print(get_response.json()) #prints json response