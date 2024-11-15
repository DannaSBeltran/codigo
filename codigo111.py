import re
import json
import matplotlib.pyplot as plt
from collections import Counter


pattern = (
    r'(\d{1,3}\.){3}\d{1,3} - - \[(.*?)\] "(\S+) (\S+) (\S+)" (\d{3}) (\d+) "(.*?)" "(.*?)" (\d+\.\d+)'
)
with open('datos.txt', 'r') as lines:
    jsonExtract = []
    for line in lines:
        values = re.finditer(pattern, line)
        for match in values:
            jsonData = {
        "ip": match.group(0).split(" ")[0],
        "timestamp": match.group(2),
        "method": match.group(3),
        "resource": match.group(4),
        "http_version": match.group(5),
        "status_code": int(match.group(6)),
        "response_size": int(match.group(7)),
        "referer": match.group(8),
        "user_agent": match.group(9),
        "response_time": float(match.group(10)),
                
                
            }
            jsonExtract.append(jsonData)

    
    print(json.dumps(jsonExtract, indent=4))
    
    status_codes = [jsonData['status_code'] for log in jsonExtract]
status_counter = Counter(status_codes)


plt.bar(status_counter.keys(), status_counter.values())
plt.xlabel("Código de Estado HTTP")
plt.ylabel("Frecuencia")
plt.title("Frecuencia de Códigos de Estado HTTP")
plt.show()
