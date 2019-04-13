class ProjectHelper:

    project_cache = None

    def __init__(self, app):
        self.app = app

    def create(self, project):
        self.open_creation_page()
        self.fill_info_fields(project)
        self.click_submit_data_button()
        self.go_to_projects_page()

    def click_submit_data_button(self):
        # Submit group data
        self.project_cache = None
        self.app.wd.find_element_by_css_selector("#manage-project-create-form input[type=submit]").click()

    def open_creation_page(self):
        # Create a new group
        self.app.open_page_relative("/manage_proj_create_page.php")

    def delete_project_by_id(self, id):
        self.open_edit_page_by_id(id)
        self.click_delete_project_button()

    def open_edit_page_by_id(self, id):
        # Create a new group
        self.app.open_page_relative("/manage_proj_edit_page.php?project_id=%s" % id)

    def click_delete_project_button(self):
        self.project_cache = None
        self.app.wd.find_element_by_css_selector("#project-delete-form input[type=submit]").click()
        self.app.wd.find_element_by_css_selector("input[value='Delete Project']").click()

    def fill_info_fields(self, project):
        # Fill group data
        self.app.ge.type("input[name='name']", project.name)

    def go_to_projects_page(self):
        self.app.open_page_relative("/manage_proj_page.php")

