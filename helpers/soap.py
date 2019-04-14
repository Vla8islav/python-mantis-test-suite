import suds
import suds.bindings
from suds.client import Client
from suds import WebFault
import logging


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        suds.bindings.binding.envns = ('SOAP-ENV',
                                       'http://www.w3.org/2003/05/soap-envelope')
        client = suds.client.Client(self.app.get_absolute_url("api/soap/mantisconnect.php?wsdl"))
        logging.basicConfig(level=logging.DEBUG,
                            format = '%(asctime)s %(levelname)s %(message)s',
                            filename = '/tmp/my-log.txt')
        logging.getLogger('suds.client').setLevel(logging.DEBUG)
        try:
            rez = client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

