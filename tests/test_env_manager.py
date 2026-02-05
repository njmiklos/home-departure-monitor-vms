import pytest
from pathlib import Path

import env_manager


@pytest.fixture(autouse=True)
def disable_dotenv_loading(monkeypatch):
    """
    Global patch preventing load_dotenv() from loading the real *.env file in all tests.
    - during tests, load_dotenv() does nothing, only os.environ matters
    - monkeypatch.setenv() says what os.environ contains
    """
    monkeypatch.setattr(env_manager, 'load_dotenv', lambda: None)

# OK

def test_get_path_ok(monkeypatch):
    tmp_path = str('tmp_path')
    monkeypatch.setenv('DATA_DIR', tmp_path)
    result = env_manager.get_path('DATA_DIR')
    assert result == Path(tmp_path)
    assert isinstance(result, Path)

def test_get_longitude_ok(monkeypatch):
    monkeypatch.setenv('LONGITUDE', '12.917891093807997')
    result = env_manager.get_longitude()
    assert result == 12.91789109
    assert isinstance(result, float)

def test_get_latitude_ok(monkeypatch):
    monkeypatch.setenv('LATITUDE', '50.84516430809533')
    result = env_manager.get_latitutde()
    assert result == 50.84516431
    assert isinstance(result, float)

def test_get_radius_ok(monkeypatch):
    monkeypatch.setenv('RADIUS', '500')
    result = env_manager.get_radius()
    assert result == 500
    assert isinstance(result, int)

def test_get_timeframe_ok(monkeypatch):
    monkeypatch.setenv('TIMEFRAME', '30')
    result = env_manager.get_timeframe()
    assert result == 30
    assert isinstance(result, int)

# ValueErrors

def test_get_path_error(monkeypatch):
    monkeypatch.delenv('TMP_PATH', raising=False)
    with pytest.raises(ValueError, match='TMP_PATH is not set in the .env file.'):
        env_manager.get_path('TMP_PATH')

def test_get_latitude_error(monkeypatch):
    monkeypatch.delenv('LATITUDE', raising=False)
    with pytest.raises(ValueError, match='LATITUDE is not set in the .env file.'):
        env_manager.get_latitutde()

def test_get_longitude_error(monkeypatch):
    monkeypatch.delenv('LONGITUDE', raising=False)
    with pytest.raises(ValueError, match='LONGITUDE is not set in the .env file.'):
        env_manager.get_longitude()

def test_get_radius_error(monkeypatch):
    monkeypatch.delenv('RADIUS', raising=False)
    with pytest.raises(ValueError, match='RADIUS is not set in the .env file.'):
        env_manager.get_radius()

def test_get_timeframe_error(monkeypatch):
    monkeypatch.delenv('TIMEFRAME', raising=False)
    with pytest.raises(ValueError, match='TIMEFRAME is not set in the .env file.'):
        env_manager.get_timeframe()