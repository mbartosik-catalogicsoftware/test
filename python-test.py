import os
import requests

# Test downloading the license file
url = "https://pl-nexus.ad.catalogic.us/repository/dpx-build-tools/installbuilder/license_2024-07-22.xml"

print("Testing download...")
print(f"URL: {url}")
print(os.getenv('REQUESTS_CA_BUNDLE'))

try:
    response = requests.get(url)
    print("SUCCESS: Download worked!")
    print(f"File size: {len(response.content)} bytes")
except Exception as e:
    print(f"FAILED: {e}")
