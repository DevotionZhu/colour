# -*- coding: utf-8 -*-
"""
Showcases characterisation plotting examples.
"""

from pprint import pprint

import colour
from colour.plotting import (colour_style, plot_single_colour_checker,
                             plot_multi_sds)
from colour.utilities import message_box

message_box('Characterisation Plots')

colour_style()

message_box('Plotting colour rendition charts.')
pprint(sorted(colour.CHROMATICITIES_COLOURCHECKER.keys()))
plot_single_colour_checker('ColorChecker 1976')
plot_single_colour_checker(
    'BabelColor Average', text_kwargs={'visible': False})
plot_single_colour_checker('ColorChecker 1976', text_kwargs={'visible': False})
plot_single_colour_checker('ColorChecker 2005', text_kwargs={'visible': False})

print('\n')

message_box(('Plotting "BabelColor Average" colour rendition charts spectral '
             'distributions.'))
plot_multi_sds(
    colour.SDS_COLOURCHECKER['BabelColor Average'].values(),
    use_sds_colours=True,
    title=('BabelColor Average - '
           'Spectral Distributions'))
