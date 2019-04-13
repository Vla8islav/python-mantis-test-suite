from model.project import Project


def test_remove_project(app, db):
    name = "Some name"
    if not db.project_with_name_exists(name):
        db.create_project_by_name(name)

    app.pr.delete_project_by_id(db.get_project_by_name(name).id)
    assert not db.project_with_name_exists(name)
