#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################
"""
The arg spec for the vyos_ospfv3 module
"""


class Ospfv3Args(object):  # pylint: disable=R0903
    """The arg spec for the vyos_ospfv3 module
    """
    def __init__(self, **kwargs):
        pass

    argument_spec = {
        'config': {
            'elements': 'dict',
            'options': {
                'ospf_area': {
                    'elements': 'dict',
                    'options': {
                        'area': {
                            'type': 'str'
                        },
                        'export_list': {
                            'type': 'str'
                        },
                        'import_list': {
                            'type': 'str'
                        },
                        'range': {
                            'elements': 'dict',
                            'options': {
                                'address': {
                                    'type': 'str'
                                },
                                'advertise': {
                                    'type': 'bool'
                                },
                                'not_advertise': {
                                    'type': 'bool'
                                }
                            },
                            'type': 'list'
                        }
                    },
                    'type': 'list'
                },
                'parameters': {
                    'options': {
                        'router_id': {
                            'type': 'str'
                        }
                    },
                    'type': 'dict'
                },
                'redistribute': {
                    'elements': 'dict',
                    'options': {
                        'route_map': {
                            'type': 'str'
                        },
                        'route_type': {
                            'choices':
                            ['bgp', 'connected', 'kernel', 'ripng', 'static'],
                            'type':
                            'str'
                        }
                    },
                    'type': 'list'
                }
            },
            'type': 'list'
        },
        "running_config": {"type": "str"},
        'state': {
            'choices': [
                'merged', 'replaced', 'deleted', 'parsed', 'gathered',
                'rendered'
            ],
            'default':
            'merged',
            'type':
            'str'
        }
    }  # pylint: disable=C0301
