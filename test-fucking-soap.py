
from zeep import Client
from zeep.exceptions import Fault

client = Client("http://localhost:8989/api/soap/mantisconnect.php?wsdl")
# result = client.service.mc_login("administrator", "rootvnjkdfkjvnjfkvfd")
try:
    result = client.service.mc_login("administrator", "focCi3QS9mmYNbKYoqXm")
    print(result)
except Fault:
    print("No luck, buddy")


