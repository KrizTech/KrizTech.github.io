import requests

url = 'http://127.0.0.1:5000/signup'
data = {
    'first_name': 'Kasumba',
    'last_name': 'Raymond',
    'email': 'kasumba@gmail.com',
    'password': 'katshd123',
    'phone_number' : '+256756519001',
    'account_type': 'Tutor'
}

response = requests.post(url, data=data)

# Print the response
print(response.text)
