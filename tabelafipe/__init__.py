# coding=utf-8
import pkg_resources


pkg_resources.declare_namespace(__name__)

VERSION = (0, 0, 1)
__version__ = ".".join(map(str, VERSION))
__status__ = "Development"
__description__ = u"Módulo de comunicação com o site oficial da tabela fipe."
__author__ = u"Ervilis Viana de Souza"
__credits__ = []
__email__ = u"ervilisviana@gmail.com"
__license__ = u"MIT"
__copyright__ = u"Copyright 2015, Ervilis Viana de Souza"
