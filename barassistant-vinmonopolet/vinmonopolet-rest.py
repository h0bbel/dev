########### Python 3.2 #############
import urllib.request, json, sys

if len(sys.argv) < 2:
    print ("No argument provided, continuing with default")
    item = "9133502"
else:
    item = int(sys.argv[1])


try:
    url = f"https://apis.vinmonopolet.no/products/v0/details-normal?productId={item}"

    hdr ={
    # Request headers
    'Cache-Control': 'no-cache',
    'Ocp-Apim-Subscription-Key': '',
    }

    req = urllib.request.Request(url, headers=hdr)

    req.get_method = lambda: 'GET'
    response = urllib.request.urlopen(req)
    print(response.read())
except Exception as e:
    print(e)
####################################