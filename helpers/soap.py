from zeep import Client
from zeep.exceptions import Fault

from model.project import Project


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

    def get_project_list(self, username, password):
        retval = []
        client = Client(self.app.get_absolute_url("api/soap/mantisconnect.php?wsdl"))
        try:
            for soap_project in client.service.mc_projects_get_user_accessible(username, password):
                retval.append(Project(id=soap_project.id, name=soap_project.name))

            return retval
        except Fault:
            return False
