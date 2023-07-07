import json
import requests

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNWJiMjY3ZDEtNjJlMi00NmM1LWJmMTktZTJmZjdiMmRiZDFmIiwidHlwZSI6ImFwaV90b2tlbiJ9.tzdZGIQoPVBViN7Mu1655m8ZS8mgNP8UMG1DH3wRxFU"}

url="https://api.edenai.run/v2/ocr/custom_document_parsing_async"
data = {
  "providers": "amazon",
  "queries": "[{'query': 'What is the supplier name', 'pages': '1-*'}]",
}
files = {'file': open("/Users/joyxu/Downloads/eversource_example.png",'rb')}

response = requests.post(url, data=data, files=files, headers=headers)

result = json.loads(response.text)
print(result)
