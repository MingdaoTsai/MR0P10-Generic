 # importing the requests library 
import requests 

# Step 1: Fetch an access token from a Managed Identity enabled azure resource.      
# Note that the resource here is https://vault.azure.net for public cloud and api-version is 2018-02-01
MSI_ENDPOINT = "http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https%3A%2F%2Fvault.azure.net"
r = requests.get(MSI_ENDPOINT, headers = {"Metadata" : "true"}) 

# extracting data in json format 
# This request gets an access_token from Azure AD by using the local MSI endpoint.
data = r.json() 

# Step 2: Pass the access_token received from previous HTTP GET call to your key vault.
KeyVaultURL = "https://appkeyvalut.vault.azure.net/secrets/secret123?api-version=2016-10-01"
kvSecret = requests.get(url = KeyVaultURL, headers = {"Authorization": "Bearer " + data["access_token"]})


print(kvSecret.json()["value"])
