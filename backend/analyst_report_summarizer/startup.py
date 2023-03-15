# -*- coding: utf-8 -*-
"""Module to be ran to avoid lazy loading of modules"""
from importlib import import_module

import django
from django.utils.module_loading import module_has_submodule


def run():
    """Method to autoload required modules on startup"""
    submodules = ["receivers", "urls"]

    django.setup()
    app = "api"
    mod = import_module(app)
    for submodule in submodules:
        try:
            import_module(f"{app}.{submodule}")
        except Exception as e:  # pylint: disable=broad-exception-caught, invalid-name
            if module_has_submodule(mod, submodule):
                raise e
