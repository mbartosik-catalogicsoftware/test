import requests

# Test downloading the license file
url = "https://pl-nexus.ad.catalogic.us/repository/dpx-build-tools/installbuilder/license_2024-07-22.xml"
ca_cert = "C:\Catalogic_Root_CA.cer"

print("Testing download...")
print(f"URL: {url}")
print(f"CA Certificate: {ca_cert}")

try:
    # Test with default SSL verification (should fail)
    response = requests.get(url)
    print("SUCCESS: Download worked!")
    print(f"File size: {len(response.content)} bytes")
except Exception as e:
    print(f"FAILED: {e}")
