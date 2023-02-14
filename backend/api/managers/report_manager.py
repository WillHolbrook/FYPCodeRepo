# -*- coding: utf-8 -*-
"""Module for ReportManager"""
from django.core.files import File
from django.db.models.manager import Manager


class ReportManager(Manager):  # pylint: disable=too-few-public-methods
    """Manager for creation of Report objects"""

    def create(
        self, report_file: File, *args, **kwargs
    ):  # pylint: disable=unused-argument
        """Method to create a Report model from the file pdf

        This will involve calling the grobid server configured in settings to extract the TEI XML"""
        # TODO implement sending file to the grobid server for processing # pylint: disable=fixme

        return super().create(*args, **kwargs)
