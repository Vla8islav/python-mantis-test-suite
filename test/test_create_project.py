from model.project import Project


def test_create_project(app, db):
    project = Project(name="Some name")
    if db.project_with_name_exists(project.name):
        db.delete_project_by_name(project.name)
    project.id = db.get_max_project_id() + 1
    project_list_initial = app.sh.get_project_list(app.session.current_user.username,
                                                   app.session.current_user.password)
    app.pr.create(project)
    project_list_after_creation = app.sh.get_project_list(app.session.current_user.username,
                                                          app.session.current_user.password)
    expected_project_list = project_list_initial.copy()
    expected_project_list.append(project)
    assert db.project_with_name_exists(project.name)
    assert sorted(project_list_after_creation, key=Project.id) == \
           sorted(expected_project_list, key=Project.id)
