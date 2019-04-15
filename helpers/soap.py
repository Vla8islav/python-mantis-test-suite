import suds.bindings
from suds import WebFault


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = suds.client.Client(self.app.get_absolute_url("api/soap/mantisconnect.php?wsdl"))
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

