# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.deidentification_config import DeidentificationConfig
from openapi_server.models.note import Note
from openapi_server import util

from openapi_server.models.deidentification_config import DeidentificationConfig  # noqa: E501
from openapi_server.models.note import Note  # noqa: E501

class DeidentifyRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, deidentification_configurations=None, note=None):  # noqa: E501
        """DeidentifyRequest - a model defined in OpenAPI

        :param deidentification_configurations: The deidentification_configurations of this DeidentifyRequest.  # noqa: E501
        :type deidentification_configurations: List[DeidentificationConfig]
        :param note: The note of this DeidentifyRequest.  # noqa: E501
        :type note: Note
        """
        self.openapi_types = {
            'deidentification_configurations': List[DeidentificationConfig],
            'note': Note
        }

        self.attribute_map = {
            'deidentification_configurations': 'deidentificationConfigurations',
            'note': 'note'
        }

        self._deidentification_configurations = deidentification_configurations
        self._note = note

    @classmethod
    def from_dict(cls, dikt) -> 'DeidentifyRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DeidentifyRequest of this DeidentifyRequest.  # noqa: E501
        :rtype: DeidentifyRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def deidentification_configurations(self):
        """Gets the deidentification_configurations of this DeidentifyRequest.

        A list of deidentification strategies and the entity types on which to perform them. De-identification priority (i.e. which annotation to use when two annotations overlap) is determined by the order of this array and the order of the annotationTypes array inside of each deidentificationConfig.  # noqa: E501

        :return: The deidentification_configurations of this DeidentifyRequest.
        :rtype: List[DeidentificationConfig]
        """
        return self._deidentification_configurations

    @deidentification_configurations.setter
    def deidentification_configurations(self, deidentification_configurations):
        """Sets the deidentification_configurations of this DeidentifyRequest.

        A list of deidentification strategies and the entity types on which to perform them. De-identification priority (i.e. which annotation to use when two annotations overlap) is determined by the order of this array and the order of the annotationTypes array inside of each deidentificationConfig.  # noqa: E501

        :param deidentification_configurations: The deidentification_configurations of this DeidentifyRequest.
        :type deidentification_configurations: List[DeidentificationConfig]
        """

        self._deidentification_configurations = deidentification_configurations

    @property
    def note(self):
        """Gets the note of this DeidentifyRequest.


        :return: The note of this DeidentifyRequest.
        :rtype: Note
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this DeidentifyRequest.


        :param note: The note of this DeidentifyRequest.
        :type note: Note
        """
        if note is None:
            raise ValueError("Invalid value for `note`, must not be `None`")  # noqa: E501

        self._note = note