import pymysql

from model.project import Project


class DbFixture:
    def __init__(self, host="localhost", port=3306, database="bugtracker", user="root",
                 password=""):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.connection = pymysql.connect(host=self.host, port=self.port, database=self.database, user=self.user,
                                          password=self.password, autocommit=True)

    def get_project_by_name(self, name):
        project_list = self.get_project_list()
        if any(True for _ in filter(lambda x: x.name == name, project_list)):
            return filter(lambda x: x.name == name, project_list).__next__()
        else:
            return None

    def project_with_name_exists(self, name):
        return self.get_project_by_name(name) is not None

    def get_max_project_id(self):
        retval = 1
        cursor = self.connection.cursor()
        try:
            cursor.execute("select max(id) as max_id from mantis_project_table")
            for row in cursor:
                (max_id) = row
                retval = max_id[0]
        finally:
            cursor.close()
        return retval

    def get_project_list(self):
        retval = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select  id, name, status, enabled, view_state, "
                           "access_min, file_path, description, category_id "
                           "from mantis_project_table")
            for row in cursor:
                (id, name, status, enabled, view_state,
                 access_min, file_path, description, category_id) = row
                retval.append(Project(id=id, name=name))
        finally:
            cursor.close()
        return retval

    def delete_project_by_name(self, name):
        retval = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("delete from mantis_project_table where name='%s'" % name)
        finally:
            cursor.close()
        return retval

    def destroy(self):
        self.connection.close()
