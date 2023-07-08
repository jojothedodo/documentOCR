import requests

public_id = input("Enter public id: ")

url = "https://api.edenai.run/v2/ocr/custom_document_parsing_async/" + public_id

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNWJiMjY3ZDEtNjJlMi00NmM1LWJmMTktZTJmZjdiMmRiZDFmIiwidHlwZSI6ImFwaV90b2tlbiJ9.tzdZGIQoPVBViN7Mu1655m8ZS8mgNP8UMG1DH3wRxFU"}

response = requests.get(url, headers=headers)

print(response.text)