import pytest
from pathlib import Path
pytest_plugins = "pytester"

@pytest.mark.parametrize(
    "send_when", ["everytime", "on_failed"])
def test_send(send_when, pytester: pytest.Pytester, tmp_path: Path):
    config_path = tmp_path.joinpath("../pytest.ini")
    config_path.write_text(f"""
[pytest]
addopts = -p no:warnings
api = https://oapi.dingtalk.com/robot/send?access_token=6deb48ff96240e5e55d8d081ab4cb551fffa8169c924cbd472bac6c81edbc40d
send_when = {send_when}
""")

    print(config_path.read_text())




@pytest.mark.parametrize(
    "api", ["https://oapi.dingtalk.com/robot/send?"
            "access_token=6deb48ff96240e5e55d8d081ab4cb551fffa8169c924cbd472bac6c81edbc40d",
            ""])
def test_sendAPI(api):
    ...