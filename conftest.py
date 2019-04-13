import importlib
import json
import os
import jsonpickle
import pytest

from fixture.application import Application
from model.user import User

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file_name = os.path.join(get_project_folder(), file)
        with open(config_file_name) as config_file:
            target = json.load(config_file)
    return target


def get_project_folder():
    return os.path.dirname(os.path.realpath(__file__))


def get_data_folder():
    return os.path.join(get_project_folder(), "data")


@pytest.fixture
def app(request):
    global fixture

    web_config = load_config(request.config.getoption("--target"))["web"]
    user = User(web_config["login"], web_config["password"])
    if fixture is None or not fixture.is_valid():
        browser = request.config.getoption("--browser")
        url = web_config["baseUrl"]
        fixture = Application(browser, url)
        fixture.session.login(user)

    fixture.session.ensure_login(user)
    return fixture


@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))["db"]
    db_fixture = DbFixture(host=db_config["host"], database=db_config["database"], user=db_config["user"],
                           password=db_config["password"])

    def fin():
        db_fixture.destroy()

    request.addfinalizer(fin)
    return db_fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


@pytest.fixture
def check_ui(request):
    retval = request.config.getoption("--check-ui")
    return retval


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check-ui", action="store_true")


def load_from_module(module):
    return importlib.import_module("data.%s" % module).test_data


def load_from_json(file):
    with open(os.path.join(get_data_folder(), "%s.json" % file)) as f:
        return jsonpickle.decode(f.read())


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            test_data = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])
        if fixture.startswith("json_"):
            test_data = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])
