import requests
import vl_convert as vlc
import pytest
import json

DEV_URL = " http://localhost:3000"


@pytest.fixture
def vl_spec():
    return {
        "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
        "data": {
            "url": "https://vega.github.io/vega-datasets/data/movies.json"
        },
        "mark": "circle",
        "encoding": {
            "x": {"bin": {"maxbins": 10}, "field": "IMDB Rating"},
            "y": {"bin": {"maxbins": 10}, "field": "Rotten Tomatoes Rating"},
            "size": {"aggregate": "count"},
        },
    }


@pytest.fixture
def vl_spec_invalid_base_url():
    return {
        "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
        "data": {
            "url": "https://raw.githubusercontent.com/vega/vega-datasets/next/data/movies.json"
        },
        "mark": "circle",
        "encoding": {
            "x": {"bin": {"maxbins": 10}, "field": "IMDB Rating"},
            "y": {"bin": {"maxbins": 10}, "field": "Rotten Tomatoes Rating"},
            "size": {"aggregate": "count"},
        },
    }


def test_version():
    version_url = f"{DEV_URL}/api/version"
    response = requests.get(version_url)
    assert response.status_code == 200
    assert vlc.__version__ == response.content.decode()


def test_vl2svg(vl_spec):
    url = f"{DEV_URL}/api/vl2svg"
    response = requests.post(url, json=vl_spec)
    assert response.status_code == 200
    assert response.headers['Content-type'] == "image/svg+xml"
    svg = response.content.decode("utf8")
    assert svg.startswith("<svg")


def test_vg2svg(vl_spec):
    url = f"{DEV_URL}/api/vl2vg"
    response = requests.post(url, json=vl_spec)
    assert response.status_code == 200
    assert response.headers['Content-type'] == "application/json"
    vg_spec = json.loads(response.content.decode("utf8"))
    assert vg_spec["$schema"] == "https://vega.github.io/schema/vega/v5.json"

    url = f"{DEV_URL}/api/vg2svg"
    response = requests.post(url, json=vg_spec)
    assert response.status_code == 200
    assert response.headers['Content-type'] == "image/svg+xml"
    svg = response.content.decode("utf8")
    assert svg.startswith("<svg")


def test_vl2svg_allowed_base_url(vl_spec_invalid_base_url):
    # Loading data from GitHub is forbidden by base url rules
    url = f"{DEV_URL}/api/vl2svg"
    response = requests.post(url, json=vl_spec_invalid_base_url)
    assert response.status_code == 400
    assert response.headers['Content-type'] == "text/plain"
    message = response.content.decode("utf8")
    assert "External data url not allowed" in message


def test_vl2png(vl_spec):
    url = f"{DEV_URL}/api/vl2png?scale=2"
    response = requests.post(url, json=vl_spec)
    assert response.status_code == 200
    assert response.headers['Content-type'] == "image/png"
    png = response.content
    assert png.startswith(b"\x89PNG")


def test_vg2png(vl_spec):
    url = f"{DEV_URL}/api/vl2vg"
    response = requests.post(url, json=vl_spec)
    assert response.status_code == 200
    assert response.headers['Content-type'] == "application/json"
    vg_spec = json.loads(response.content.decode("utf8"))
    assert vg_spec["$schema"] == "https://vega.github.io/schema/vega/v5.json"

    url = f"{DEV_URL}/api/vg2png?scale=2"
    response = requests.post(url, json=vg_spec)
    assert response.status_code == 200
    assert response.headers['Content-type'] == "image/png"
    png = response.content
    assert png.startswith(b"\x89PNG")


def test_vl2png_allowed_base_url(vl_spec_invalid_base_url):
    # Loading data from GitHub is forbidden by base url rules
    url = f"{DEV_URL}/api/vl2png"
    response = requests.post(url, json=vl_spec_invalid_base_url)
    assert response.status_code == 400
    assert response.headers['Content-type'] == "text/plain"
    message = response.content.decode("utf8")
    assert "External data url not allowed" in message
