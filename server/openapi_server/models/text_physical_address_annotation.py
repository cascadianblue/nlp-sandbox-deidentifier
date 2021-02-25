# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util
from openapi_server.models.text_annotation import TextAnnotation  # noqa: E501


class TextPhysicalAddressAnnotation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, start=None, length=None, text=None, confidence=None, address_type=None):  # noqa: E501
        """TextPhysicalAddressAnnotation - a model defined in OpenAPI

        :param start: The start of this TextPhysicalAddressAnnotation.  # noqa: E501
        :type start: int
        :param length: The length of this TextPhysicalAddressAnnotation.  # noqa: E501
        :type length: int
        :param text: The text of this TextPhysicalAddressAnnotation.  # noqa: E501
        :type text: str
        :param confidence: The confidence of this TextPhysicalAddressAnnotation.  # noqa: E501
        :type confidence: float
        :param address_type: The address_type of this TextPhysicalAddressAnnotation.  # noqa: E501
        :type address_type: str
        """
        self.openapi_types = {
            'start': int,
            'length': int,
            'text': str,
            'confidence': float,
            'address_type': str
        }

        self.attribute_map = {
            'start': 'start',
            'length': 'length',
            'text': 'text',
            'confidence': 'confidence',
            'address_type': 'addressType'
        }

        self._start = start
        self._length = length
        self._text = text
        self._confidence = confidence
        self._address_type = address_type

    @classmethod
    def from_dict(cls, dikt) -> 'TextPhysicalAddressAnnotation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TextPhysicalAddressAnnotation of this TextPhysicalAddressAnnotation.  # noqa: E501
        :rtype: TextPhysicalAddressAnnotation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def start(self):
        """Gets the start of this TextPhysicalAddressAnnotation.

        The position of the first character  # noqa: E501

        :return: The start of this TextPhysicalAddressAnnotation.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this TextPhysicalAddressAnnotation.

        The position of the first character  # noqa: E501

        :param start: The start of this TextPhysicalAddressAnnotation.
        :type start: int
        """
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501

        self._start = start

    @property
    def length(self):
        """Gets the length of this TextPhysicalAddressAnnotation.

        The length of the annotation  # noqa: E501

        :return: The length of this TextPhysicalAddressAnnotation.
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this TextPhysicalAddressAnnotation.

        The length of the annotation  # noqa: E501

        :param length: The length of this TextPhysicalAddressAnnotation.
        :type length: int
        """
        if length is None:
            raise ValueError("Invalid value for `length`, must not be `None`")  # noqa: E501

        self._length = length

    @property
    def text(self):
        """Gets the text of this TextPhysicalAddressAnnotation.

        The string annotated  # noqa: E501

        :return: The text of this TextPhysicalAddressAnnotation.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this TextPhysicalAddressAnnotation.

        The string annotated  # noqa: E501

        :param text: The text of this TextPhysicalAddressAnnotation.
        :type text: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def confidence(self):
        """Gets the confidence of this TextPhysicalAddressAnnotation.

        The confidence in the accuracy of the annotation  # noqa: E501

        :return: The confidence of this TextPhysicalAddressAnnotation.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this TextPhysicalAddressAnnotation.

        The confidence in the accuracy of the annotation  # noqa: E501

        :param confidence: The confidence of this TextPhysicalAddressAnnotation.
        :type confidence: float
        """
        if confidence is None:
            raise ValueError("Invalid value for `confidence`, must not be `None`")  # noqa: E501
        if confidence is not None and confidence > 100:  # noqa: E501
            raise ValueError("Invalid value for `confidence`, must be a value less than or equal to `100`")  # noqa: E501
        if confidence is not None and confidence < 0:  # noqa: E501
            raise ValueError("Invalid value for `confidence`, must be a value greater than or equal to `0`")  # noqa: E501

        self._confidence = confidence

    @property
    def address_type(self):
        """Gets the address_type of this TextPhysicalAddressAnnotation.

        Type of address information  # noqa: E501

        :return: The address_type of this TextPhysicalAddressAnnotation.
        :rtype: str
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        """Sets the address_type of this TextPhysicalAddressAnnotation.

        Type of address information  # noqa: E501

        :param address_type: The address_type of this TextPhysicalAddressAnnotation.
        :type address_type: str
        """
        allowed_values = ["city", "country", "department", "hospital", "organization", "other", "room", "state", "street", "zip"]  # noqa: E501
        if address_type not in allowed_values:
            raise ValueError(
                "Invalid value for `address_type` ({0}), must be one of {1}"
                .format(address_type, allowed_values)
            )

        self._address_type = address_type
