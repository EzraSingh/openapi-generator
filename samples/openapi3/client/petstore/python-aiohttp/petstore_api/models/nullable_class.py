# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date, datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class NullableClass(BaseModel):
    """
    NullableClass
    """ # noqa: E501
    required_integer_prop: Optional[StrictInt]
    integer_prop: Optional[StrictInt] = None
    number_prop: Optional[float] = None
    boolean_prop: Optional[StrictBool] = None
    string_prop: Optional[StrictStr] = None
    date_prop: Optional[date] = None
    datetime_prop: Optional[datetime] = None
    array_nullable_prop: Optional[List[Dict[str, Any]]] = None
    array_and_items_nullable_prop: Optional[List[Dict[str, Any]]] = None
    array_items_nullable: Optional[List[Dict[str, Any]]] = None
    object_nullable_prop: Optional[Dict[str, Dict[str, Any]]] = None
    object_and_items_nullable_prop: Optional[Dict[str, Dict[str, Any]]] = None
    object_items_nullable: Optional[Dict[str, Dict[str, Any]]] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["required_integer_prop", "integer_prop", "number_prop", "boolean_prop", "string_prop", "date_prop", "datetime_prop", "array_nullable_prop", "array_and_items_nullable_prop", "array_items_nullable", "object_nullable_prop", "object_and_items_nullable_prop", "object_items_nullable"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of NullableClass from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if required_integer_prop (nullable) is None
        # and model_fields_set contains the field
        if self.required_integer_prop is None and "required_integer_prop" in self.model_fields_set:
            _dict['required_integer_prop'] = None

        # set to None if integer_prop (nullable) is None
        # and model_fields_set contains the field
        if self.integer_prop is None and "integer_prop" in self.model_fields_set:
            _dict['integer_prop'] = None

        # set to None if number_prop (nullable) is None
        # and model_fields_set contains the field
        if self.number_prop is None and "number_prop" in self.model_fields_set:
            _dict['number_prop'] = None

        # set to None if boolean_prop (nullable) is None
        # and model_fields_set contains the field
        if self.boolean_prop is None and "boolean_prop" in self.model_fields_set:
            _dict['boolean_prop'] = None

        # set to None if string_prop (nullable) is None
        # and model_fields_set contains the field
        if self.string_prop is None and "string_prop" in self.model_fields_set:
            _dict['string_prop'] = None

        # set to None if date_prop (nullable) is None
        # and model_fields_set contains the field
        if self.date_prop is None and "date_prop" in self.model_fields_set:
            _dict['date_prop'] = None

        # set to None if datetime_prop (nullable) is None
        # and model_fields_set contains the field
        if self.datetime_prop is None and "datetime_prop" in self.model_fields_set:
            _dict['datetime_prop'] = None

        # set to None if array_nullable_prop (nullable) is None
        # and model_fields_set contains the field
        if self.array_nullable_prop is None and "array_nullable_prop" in self.model_fields_set:
            _dict['array_nullable_prop'] = None

        # set to None if array_and_items_nullable_prop (nullable) is None
        # and model_fields_set contains the field
        if self.array_and_items_nullable_prop is None and "array_and_items_nullable_prop" in self.model_fields_set:
            _dict['array_and_items_nullable_prop'] = None

        # set to None if object_nullable_prop (nullable) is None
        # and model_fields_set contains the field
        if self.object_nullable_prop is None and "object_nullable_prop" in self.model_fields_set:
            _dict['object_nullable_prop'] = None

        # set to None if object_and_items_nullable_prop (nullable) is None
        # and model_fields_set contains the field
        if self.object_and_items_nullable_prop is None and "object_and_items_nullable_prop" in self.model_fields_set:
            _dict['object_and_items_nullable_prop'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict]) -> Optional[Self]:
        """Create an instance of NullableClass from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "required_integer_prop": obj.get("required_integer_prop"),
            "integer_prop": obj.get("integer_prop"),
            "number_prop": obj.get("number_prop"),
            "boolean_prop": obj.get("boolean_prop"),
            "string_prop": obj.get("string_prop"),
            "date_prop": obj.get("date_prop"),
            "datetime_prop": obj.get("datetime_prop"),
            "array_nullable_prop": obj.get("array_nullable_prop"),
            "array_and_items_nullable_prop": obj.get("array_and_items_nullable_prop"),
            "array_items_nullable": obj.get("array_items_nullable"),
            "object_nullable_prop": obj.get("object_nullable_prop"),
            "object_and_items_nullable_prop": obj.get("object_and_items_nullable_prop"),
            "object_items_nullable": obj.get("object_items_nullable")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


