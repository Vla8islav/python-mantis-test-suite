
from zeep import Client

client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
result = client.service.mc_login("administrator", "rootvnjkdfkjvnjfkvfd")
print(result)

