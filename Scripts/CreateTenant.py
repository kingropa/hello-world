import requests

url = "http://192.168.10.1/api/node/mo/uni/tn-testtenant.json"

payload = "{\"fvTenant\":{\"attributes\":{\"dn\":\"uni/tn-testtenant\",\"name\":\"testtenant\",\"rn\":\"tn-testtenant\",\"status\":\"created\"},\"children\":[]}}\r\n"
cookie = {"APIC-cookie": "EIJXR+q79b+RdGSwjP5JnRw254wlsLATX9jGv19GZVGTr2hSSnAmQOdtNJx5RmQfNJpO8KODGFIyxrpsI6Bcyqbm5FsqZQ8EomGlzapfsMniCMLFPpb0T3RbXiOrxGPiDwWRT3nqOB1dKOq1mPi45oKJHhKn6ohYtr785ocFca0="}

response = requests.request("POST", url, data=payload, cookies=cookie)

print(response.text)