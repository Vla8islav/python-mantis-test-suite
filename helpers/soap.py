from zeep import Client
from zeep.exceptions import Fault

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.get_absolute_url("api/soap/mantisconnect.php?wsdl"))
        try:
            client.service.mc_login(username, password)
            return True
        except Fault:
            return False

