import os
import tempfile

import pytest

from app import create_app


def test_index_kpi(client):
    rv = client.get('/kpi')
    assert b'kpi' in rv.data

def test_show_kpi(client):
    rv = client.get('/kpi/1')
    assert b'kpi 1' in rv.data
    
def test_index_kpi_statistics(client):
    rv = client.get('/kpi/statistics')
    assert b'statistics' in rv.data

def test_index_job(client):
    rv = client.get('/schedule/')
    assert b'jobs' in rv.data

def test_create_job(client):
    rv = client.post('/schedule/')
    assert b'' in rv.data