from model.project import Project


def test_create_project(app, db):
    name = "Some name"
    db.delete_project_by_name(name)
    app.pr.create(Project(name=name))
    assert db.project_with_name_exists(name)

