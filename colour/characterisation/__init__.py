# -*- coding: utf-8 -*-

from __future__ import absolute_import

import sys

from colour.utilities.deprecation import ModuleAPI, build_API_changes
from colour.utilities.documentation import is_documentation_building

from .cameras import RGB_CameraSensitivities
from .displays import RGB_DisplayPrimaries
from .datasets import *  # noqa
from . import datasets
from .aces_it import (
    sd_to_aces_relative_exposure_values, read_training_data_rawtoaces_v1,
    generate_illuminants_rawtoaces_v1, white_balance_multipliers,
    best_illuminant, normalise_illuminant, training_data_sds_to_RGB,
    training_data_sds_to_XYZ, optimisation_factory_rawtoaces_v1,
    optimisation_factory_JzAzBz, idt_matrix)
from .correction import (
    augmented_matrix_Cheung2004, polynomial_expansion_Finlayson2015,
    polynomial_expansion_Vandermonde, POLYNOMIAL_EXPANSION_METHODS,
    polynomial_expansion, colour_correction_matrix_Cheung2004,
    colour_correction_matrix_Finlayson2015,
    colour_correction_matrix_Vandermonde, COLOUR_CORRECTION_MATRIX_METHODS,
    colour_correction_matrix, colour_correction_Cheung2004,
    colour_correction_Finlayson2015, colour_correction_Vandermonde,
    COLOUR_CORRECTION_METHODS, colour_correction)

__all__ = ['RGB_CameraSensitivities']
__all__ += ['RGB_DisplayPrimaries']
__all__ += datasets.__all__
__all__ += [
    'sd_to_aces_relative_exposure_values', 'read_training_data_rawtoaces_v1',
    'generate_illuminants_rawtoaces_v1', 'white_balance_multipliers',
    'best_illuminant', 'normalise_illuminant', 'training_data_sds_to_RGB',
    'training_data_sds_to_XYZ', 'optimisation_factory_rawtoaces_v1',
    'optimisation_factory_JzAzBz', 'idt_matrix'
]
__all__ += [
    'augmented_matrix_Cheung2004', 'polynomial_expansion_Finlayson2015',
    'polynomial_expansion_Vandermonde', 'POLYNOMIAL_EXPANSION_METHODS',
    'polynomial_expansion', 'colour_correction_matrix_Cheung2004',
    'colour_correction_matrix_Finlayson2015',
    'colour_correction_matrix_Vandermonde', 'COLOUR_CORRECTION_MATRIX_METHODS',
    'colour_correction_matrix', 'colour_correction_Cheung2004',
    'colour_correction_Finlayson2015', 'colour_correction_Vandermonde',
    'COLOUR_CORRECTION_METHODS', 'colour_correction'
]


# ----------------------------------------------------------------------------#
# ---                API Changes and Deprecation Management                ---#
# ----------------------------------------------------------------------------#
class characterisation(ModuleAPI):
    def __getattr__(self, attribute):
        return super(characterisation, self).__getattr__(attribute)


# v0.3.16
API_CHANGES = {
    'ObjectRenamed': [
        [
            'colour.characterisation.RGB_SpectralSensitivities',
            'colour.characterisation.RGB_CameraSensitivities',
        ],
        [
            'colour.characterisation.CAMERA_RGB_SPECTRAL_SENSITIVITIES',
            'colour.characterisation.MSDS_CAMERA_SENSITIVITIES',
        ],
        [
            'colour.characterisation.COLOURCHECKERS',
            'colour.characterisation.CHROMATICITIES_COLOURCHECKER',
        ],
        [
            'colour.characterisation.COLOURCHECKER_SDS',
            'colour.characterisation.SDS_COLOURCHECKER',
        ],
        [
            'colour.characterisation.DISPLAY_RGB_PRIMARIES',
            'colour.characterisation.MSDS_DISPLAY_PRIMARIES',
        ],
    ]
}
"""
Defines *colour.characterisation* sub-package API changes.

API_CHANGES : dict
"""

if not is_documentation_building():
    sys.modules['colour.characterisation'] = characterisation(
        sys.modules['colour.characterisation'], build_API_changes(API_CHANGES))

    del ModuleAPI, is_documentation_building, build_API_changes, sys
