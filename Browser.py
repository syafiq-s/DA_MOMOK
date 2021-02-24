# Use the Request library
import requests
# Set the target webpage

name = input("State full website URL:")

url = name


r = requests.get(url)
# This will get the full page
print(r.text)
# This will get the status code
print("Status code:")
print("\t *", r.status_code)
if (r.status_code == 200):
 print("OK")
# This will just get just the headers
h = requests.head(url)
print("Welcome to MOMOK's Website:")
print("Teemo or Mordekaiser?")
# To print line by line
for x in h.headers:
 print("\t ", x, ":", h.headers[x])
print("**********")
# This will modify the headers user-agent
headers = {
 'User-Agent' : '''Mobile'''
}
# Test it on an external site
url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)
