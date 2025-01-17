"""Fixtures module."""

import os

from dependency_injector import providers
from pytest import fixture


@fixture
def config_type():
    return "default"


@fixture
def config(config_type):
    if config_type == "strict":
        return providers.Configuration(strict=True)
    elif config_type == "default":
        return providers.Configuration()
    else:
        raise ValueError("Undefined config type \"{0}\"".format(config_type))


@fixture
def ini_config_file_1(tmp_path):
    config_file = str(tmp_path / "config_1.ini")
    with open(config_file, "w") as file:
        file.write(
            "[section1]\n"
            "value1=1\n"
            "\n"
            "[section2]\n"
            "value2=2\n"
        )
    return config_file


@fixture
def ini_config_file_2(tmp_path):
    config_file = str(tmp_path / "config_2.ini")
    with open(config_file, "w") as file:
        file.write(
            "[section1]\n"
            "value1=11\n"
            "value11=11\n"
            "[section3]\n"
            "value3=3\n"
        )
    return config_file


@fixture
def ini_config_file_3(tmp_path):
    ini_config_file_3 = str(tmp_path / "config_3.ini")
    with open(ini_config_file_3, "w") as file:
        file.write(
            "[section1]\n"
            "value1=${CONFIG_TEST_ENV}\n"
            "value2=${CONFIG_TEST_PATH}/path\n"
        )
    return ini_config_file_3


@fixture
def yaml_config_file_1(tmp_path):
    config_file = str(tmp_path / "config_1.yml")
    with open(config_file, "w") as file:
        file.write(
            "section1:\n"
            "  value1: 1\n"
            "\n"
            "section2:\n"
            "  value2: 2\n"
        )
    return config_file


@fixture
def yaml_config_file_2(tmp_path):
    config_file = str(tmp_path / "config_2.yml")
    with open(config_file, "w") as file:
        file.write(
            "section1:\n"
            "  value1: 11\n"
            "  value11: 11\n"
            "section3:\n"
            "  value3: 3\n"
        )
    return config_file


@fixture
def yaml_config_file_3(tmp_path):
    yaml_config_file_3 = str(tmp_path / "config_3.yml")
    with open(yaml_config_file_3, "w") as file:
        file.write(
            "section1:\n"
            "  value1: ${CONFIG_TEST_ENV}\n"
            "  value2: ${CONFIG_TEST_PATH}/path\n"
        )
    return yaml_config_file_3


@fixture(autouse=True)
def environment_variables():
    os.environ["CONFIG_TEST_ENV"] = "test-value"
    os.environ["CONFIG_TEST_PATH"] = "test-path"
    os.environ["DEFINED"] = "defined"
    os.environ["EMPTY"] = ""
    os.environ["CONFIG_INT"] = "42"
    yield
    os.environ.pop("CONFIG_TEST_ENV", None)
    os.environ.pop("CONFIG_TEST_PATH", None)
    os.environ.pop("DEFINED", None)
    os.environ.pop("EMPTY", None)
    os.environ.pop("CONFIG_INT", None)
