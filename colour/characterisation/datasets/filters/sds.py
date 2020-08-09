# -*- coding: utf-8 -*-
"""
Filter Spectral Distributions
=============================

Defines *filter* spectral distributions.

Each *filter* data is in the form of :class:`OrderedDict` class instance of
:class:`colour.SpectralDistribution` classes as follows::

    {'name': SpectralDistribution, ..., 'name': SpectralDistribution}

The following *filters* are available:

-   ISO 7589 Diffuser

References
----------
-   :cite:`ISO2002` : ISO. (2002). INTERNATIONAL STANDARD 7589-2002 -
    Photography - Illuminants for sensitometry - Specifications for daylight,
    incandescent tungsten and printer.
"""

from __future__ import division, unicode_literals

from colour.colorimetry import SpectralDistribution
from colour.utilities import CaseInsensitiveMapping

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['DATA_SDS_FILTER_ISO', 'SDS_FILTER_ISO', 'SDS_FILTER']

DATA_SDS_FILTER_ISO = {
    'ISO 7589 Diffuser': {
        350: 0.00,
        360: 0.00,
        370: 0.00,
        380: 0.10,
        390: 0.43,
        400: 0.69,
        410: 0.78,
        420: 0.83,
        430: 0.86,
        440: 0.88,
        450: 0.90,
        460: 0.91,
        470: 0.93,
        480: 0.94,
        490: 0.95,
        500: 0.96,
        510: 0.97,
        520: 0.98,
        530: 0.99,
        540: 0.99,
        550: 1.00,
        560: 1.00,
    }
}

SDS_FILTER_ISO = CaseInsensitiveMapping({
    'ISO 7589 Diffuser':
        SpectralDistribution(
            DATA_SDS_FILTER_ISO['ISO 7589 Diffuser'],
            name='ISO 7589 Diffuser'),
})
SDS_FILTER_ISO.__doc__ = """
*ISO* filter spectral distributions.

References
----------
:cite:`ISO2002`

SDS_FILTER_ISO : CaseInsensitiveMapping
"""

SDS_FILTER = CaseInsensitiveMapping(SDS_FILTER_ISO)
SDS_FILTER.__doc__ = """
Aggregated filter spectral distributions.

References
----------
:cite:`ISO2002`

SDS_FILTER : CaseInsensitiveMapping
"""
