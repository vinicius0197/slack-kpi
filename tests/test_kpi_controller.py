import pytest
from app.api.handler import *

# Verifica se o numero de indicadores esta correto


def test_number_goals():
    assert len(all_kpi()) == 13


# Verifica se todos os indicadores estao presetes
def test_all_kpis():
    indicadores = ['Número de Projetos de Alto Impacto',
                    'NPS1', 'NPS2', 'Número de Projetos Conectados',
                    'Número de Projetos com Clientes Fidelizados',
                    'Faturamento Anual',
                    'Número de Projetos',
                    'Ticket Médio',
                    'Faturamento/Membro',
                    'Porcentagem de Membros Alocados',
                    'Presença em Eventos MEJ (%)',
                    'Número médio de projetos por membro',
                    'Tempo médio de permanência na empresa']

    assert any(k in indicadores for (k, v), indicadores in zip(
        all_kpi().items(), indicadores))


# Verifica se esta sendo carregados todos os indicadores
def test_statistica():
    assert len(reach_gols()) == 13


# Verifica se retorna indicador correto
def test_single_kpi():
    assert "Porcentagem de Membros Alocados" in match_kpi(
        "Porcentagem de Membros Alocados")


# Verifica se retorna lista de coisas parecidas
def test_array_kpi():
    assert match_kpi("projeto") == {'Número médio de projetos por membro': '1', 'Número de Projetos de Alto Impacto': '0',
                                    'Número de Projetos': '6', 'Número de Projetos Conectados': '0', 'Número de Projetos com Clientes Fidelizados': '0'}
