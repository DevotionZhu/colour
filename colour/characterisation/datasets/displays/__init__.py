# -*- coding: utf-8 -*-
"""
References
----------
-   :cite:`Fairchild1998b` : Fairchild, M., & Wyble, D. (1998). Colorimetric
    Characterization of The Apple Studio Display (flat panel LCD) (p. 22).
    http://scholarworks.rit.edu/cgi/viewcontent.cgi?article=1922&\
context=article
-   :cite:`Machado2010a` : Machado, Gustavo Mello. (2010). A model for
    simulation of color vision deficiency and a color contrast enhancement
    technique for dichromats. (pp. 1-94).
    http://www.lume.ufrgs.br/handle/10183/26950
"""

from __future__ import absolute_import

from .crt import MSDS_DISPLAY_PRIMARIES_CRT
from .lcd import MSDS_DISPLAY_PRIMARIES_LCD
from colour.utilities import CaseInsensitiveMapping

MSDS_DISPLAY_PRIMARIES = CaseInsensitiveMapping(MSDS_DISPLAY_PRIMARIES_CRT)
MSDS_DISPLAY_PRIMARIES.update(MSDS_DISPLAY_PRIMARIES_LCD)
MSDS_DISPLAY_PRIMARIES.__doc__ = """
Display primaries multi-spectral distributions.

References
----------
:cite:`Fairchild1998b`, :cite:`Machado2010a`

MSDS_DISPLAY_PRIMARIES : CaseInsensitiveMapping
    **{Apple Studio Display, Typical CRT Brainard 1997}**
"""

__all__ = ['MSDS_DISPLAY_PRIMARIES']
