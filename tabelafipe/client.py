# coding=utf-8
"""Módulo de comunicação com o site oficial da tabela fipe."""


TIPO_CARRO = 1
TIPO_MOTO = 2
TIPO_CAMINHAO = 3


class Client(object):

    """Cliente de comunicação com os endpoints de acesso aos dados."""

    tipo_veiculo = None

    tabela_referencia = None

    def __init__(self, tipo_veiculo, tabela_referencia=None):
        """
        Inicializamos o cliente com o tipo de veículo que será consultado
        pois essa informação é utilizada em todos os endpoints. Recebemos
        também opcionalmente a tabela de referência pois esse parâmetro não é
        necessário em todos os métodos.
        """
        self.tipo_veiculo = tipo_veiculo
        self.tabela_referencia = tabela_referencia

    def get_tabelas_referencia(self):
        """
        Obtem as tabelas de referência disponíves desde a criação dos índices.
        NOTE: Várias tabelas antigas estão com códigos fora de ordem.
        """
        pass

    def get_marcas(self):
        """
        Obtem as marcas disponíves para o tipo de veículo informado.
        NOTE: uma mesma marca possúi ID diferente para cada tipo de veículo.
        """
        pass

    def get_modelos(self, marca):
        """Obtem quais são os modelos disponíves da marca informada"""
        pass

    def get_anos_modelo(self, marca, modelo):
        """Obtem os anos disponíves para o modelo informado"""
        pass
