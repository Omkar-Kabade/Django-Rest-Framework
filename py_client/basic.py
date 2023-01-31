import requests

# we wil  request something to the following endpoint to get the response

# endpoint = "https://httpbin.org/anything"
headers = {'content-type': 'application/json'}
endpoint = "http://localhost:8000/api/"
get_response  = requests.post(endpoint,json={"title":'Fourth Product'}) #API - get method
#we can send json data with above using json and form data using data 

# print(get_response.text) #prints raw response
print(get_response.json()) #prints json response