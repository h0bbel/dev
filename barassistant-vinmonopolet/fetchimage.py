# Fetch images from vinmonopolet.no based on productid
# Ref https://api.vinmonopolet.no/blog/product-images

import requests, sys

if len(sys.argv) < 2:
    print ("No argument provided, continuing with default")
    item = "9133502"
else:
    item = int(sys.argv[1])


url = f"https://bilder.vinmonopolet.no/cache/515x515-0/{item}-1.jpg"

print("Downloading image from " + url)

r = requests.get(url, allow_redirects=True)

# Generate local filename
localfilename = f"{item}"+".jpg"

open(localfilename, 'wb').write(r.content)
print(localfilename + " downloaded to current directory")



