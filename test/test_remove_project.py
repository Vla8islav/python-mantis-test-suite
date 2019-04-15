from model.project import Project


def test_remove_project(app, db):
    project = Project(name="Some name")
    if db.project_with_name_exists(project.name):
        app.pr.create(project)
    project.id = db.get_project_by_name(project.name).id

    project_list_initial = app.sh.get_project_list(app.session.current_user.username,
                                                   app.session.current_user.password)
    app.pr.delete_project_by_id(project.id)
    project_list_after_deletion = app.sh.get_project_list(app.session.current_user.username,
                                                          app.session.current_user.password)

    expected_project_list = [s for s in project_list_initial if s.name != project.name]

    assert not db.project_with_name_exists(project.name)
    assert sorted(project_list_after_deletion, key=Project.id) == \
           sorted(expected_project_list, key=Project.id)
