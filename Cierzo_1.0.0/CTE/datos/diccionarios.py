# -*- coding: utf-8 -*-
"""
CIERZO CTE DB SE-AE
Constantes de la aplicación

Created on Thu Mar 12 14:49:53 2020

__author__ = Pedro Biel
__version__ = 1.0.0
__email__ = structural.eng.biel@gmail.com
"""


class Diccionarios:
    """Valores constantes de la aplicación."""

    dcc_presion_dinamica = {
        'zonas': ('A', 'B', 'C'),
        'velocidad_básica': (26, 27, 28),
        'presion_dinámica': (0.42, 0.45, 0.52)
        }
    
    dcc_periodo_retorno = {
        'periodo_retorno': ('1', '2', '5', '10', '20', '50', '200'),
        'coeficiente_corrector': (0.41, 0.78, 0.85, 0.90, 0.95, 1.00, 1.08)
        }

    dcc_coeficientes_entorno = {
        'grados': ('I', 'II', 'III', 'IV', 'V'),
        'definición': (
            'Borde del mar o de un lago, con una superficie de agua en la \
dirección del viento de al menos 5 km de longitud.',
            'Terreno rural llano sin obstáculos ni arbolado de importancia.',
            'Zona rural accidentada o llana con algunos obstáculos aislados, \
como árboles o construcciones pequeñas.',
            'Zona urbana en general, industrial o forestal.',
            'Centro de negocio de grandes ciudades, con profusión de \
edificios en altura.'
                ),
        'k': (0.156, 0.17, 0.19, 0.22, 0.24),
        'L': (0.003, 0.01, 0.05, 0.3, 1.0),
        'Z': (1., 1., 2., 5., 10.)
        }
