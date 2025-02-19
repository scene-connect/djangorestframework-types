from collections.abc import (
    Callable,
    Iterable,
    Iterator,
    Mapping,
    MutableMapping,
    Sequence,
)
from typing import (
    Any,
    Literal,
    NoReturn,
)

from django.db import models
from django.db.models import Manager, QuerySet
from rest_framework.exceptions import APIException as APIException
from rest_framework.exceptions import AuthenticationFailed as AuthenticationFailed
from rest_framework.exceptions import ErrorDetail as ErrorDetail
from rest_framework.exceptions import MethodNotAllowed as MethodNotAllowed
from rest_framework.exceptions import NotAcceptable as NotAcceptable
from rest_framework.exceptions import NotAuthenticated as NotAuthenticated
from rest_framework.exceptions import NotFound as NotFound
from rest_framework.exceptions import ParseError as ParseError
from rest_framework.exceptions import PermissionDenied as PermissionDenied
from rest_framework.exceptions import Throttled as Throttled
from rest_framework.exceptions import UnsupportedMediaType as UnsupportedMediaType
from rest_framework.exceptions import ValidationError as ValidationError
from rest_framework.fields import BooleanField as BooleanField
from rest_framework.fields import CharField as CharField
from rest_framework.fields import ChoiceField as ChoiceField
from rest_framework.fields import CreateOnlyDefault as CreateOnlyDefault
from rest_framework.fields import CurrentUserDefault as CurrentUserDefault
from rest_framework.fields import DateField as DateField
from rest_framework.fields import DateTimeField as DateTimeField
from rest_framework.fields import DecimalField as DecimalField
from rest_framework.fields import DictField as DictField
from rest_framework.fields import DurationField as DurationField
from rest_framework.fields import EmailField as EmailField
from rest_framework.fields import Field as Field
from rest_framework.fields import FileField as FileField
from rest_framework.fields import FilePathField as FilePathField
from rest_framework.fields import FloatField as FloatField
from rest_framework.fields import HiddenField as HiddenField
from rest_framework.fields import HStoreField as HStoreField
from rest_framework.fields import ImageField as ImageField
from rest_framework.fields import IntegerField as IntegerField
from rest_framework.fields import IPAddressField as IPAddressField
from rest_framework.fields import JSONField as JSONField
from rest_framework.fields import ListField as ListField
from rest_framework.fields import ModelField as ModelField
from rest_framework.fields import MultipleChoiceField as MultipleChoiceField
from rest_framework.fields import NullBooleanField as NullBooleanField
from rest_framework.fields import ReadOnlyField as ReadOnlyField
from rest_framework.fields import RegexField as RegexField
from rest_framework.fields import SerializerMethodField as SerializerMethodField
from rest_framework.fields import SkipField as SkipField
from rest_framework.fields import SlugField as SlugField
from rest_framework.fields import TimeField as TimeField
from rest_framework.fields import URLField as URLField
from rest_framework.fields import UUIDField as UUIDField
from rest_framework.fields import empty as empty
from rest_framework.relations import Hyperlink as Hyperlink
from rest_framework.relations import (
    HyperlinkedIdentityField as HyperlinkedIdentityField,
)
from rest_framework.relations import HyperlinkedRelatedField as HyperlinkedRelatedField
from rest_framework.relations import ManyRelatedField as ManyRelatedField
from rest_framework.relations import PrimaryKeyRelatedField as PrimaryKeyRelatedField
from rest_framework.relations import RelatedField as RelatedField
from rest_framework.relations import SlugRelatedField as SlugRelatedField
from rest_framework.relations import StringRelatedField as StringRelatedField
from rest_framework.utils.model_meta import FieldInfo, RelationInfo
from rest_framework.utils.serializer_helpers import BoundField, ReturnList
from typing_extensions import Self

LIST_SERIALIZER_KWARGS: Sequence[str] = ...
ALL_FIELDS: str = ...

class BaseSerializer(Field[Any, Any, Any, Any]):
    partial: bool
    many: bool
    instance: Any | None
    initial_data: Any
    _context: dict[str, Any]
    def __new__(cls, *args: Any, **kwargs: Any) -> Self: ...
    def __class_getitem__(cls, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(
        self,
        instance: Any | None = ...,
        data: Any = ...,
        partial: bool = ...,
        many: bool = ...,
        allow_empty: bool = ...,
        context: dict[str, Any] = ...,
        read_only: bool = ...,
        write_only: bool = ...,
        required: bool = ...,
        default: Any = ...,
        initial: Any = ...,
        source: str = ...,
        label: str = ...,
        help_text: str = ...,
        style: dict[str, Any] = ...,
        error_messages: dict[str, str] = ...,
        validators: Sequence[Callable[..., Any]] = ...,
        allow_null: bool = ...,
    ): ...
    @classmethod
    def many_init(cls, *args: Any, **kwargs: Any) -> BaseSerializer: ...
    def is_valid(self, raise_exception: bool = ...) -> bool: ...
    @property
    def data(self) -> Any: ...
    errors: Any
    # TODO(sbdchd): figure out how hard it would be to make this return a dict[str, Any]
    @property
    def validated_data(self) -> Any: ...
    def update(self, instance: Any, validated_data: Any) -> Any: ...
    def create(self, validated_data: Any) -> Any: ...
    def save(self, **kwargs: Any) -> Any: ...
    def to_representation(self, instance: Any) -> Any: ...

class SerializerMetaclass(type):
    def __new__(cls, name: Any, bases: Any, attrs: Any) -> Any: ...
    @classmethod
    def _get_declared_fields(
        cls, bases: Sequence[type], attrs: dict[str, Any]
    ) -> dict[str, Field[Any, Any, Any, Any]]: ...

def as_serializer_error(exc: Exception) -> dict[str, list[ErrorDetail]]: ...

class Serializer(BaseSerializer, metaclass=SerializerMetaclass):
    _declared_fields: dict[str, Field[Any, Any, Any, Any]]
    default_error_messages: dict[str, Any] = ...
    def get_initial(self) -> Any: ...
    fields: Any
    def get_fields(self) -> dict[str, Field[Any, Any, Any, Any]]: ...
    def validate(self, attrs: Any) -> Any: ...
    def __iter__(self) -> Iterator[str]: ...
    def __getitem__(self, key: str) -> BoundField: ...
    def _read_only_defaults(self) -> dict[str, Any]: ...
    @property
    def _writable_fields(self) -> list[Field[Any, Any, Any, Any]]: ...
    @property
    def _readable_fields(self) -> list[Field[Any, Any, Any, Any]]: ...
    @property
    def data(self) -> Any: ...
    errors: Any

class ListSerializer(BaseSerializer):
    child: Field[Any, Any, Any, Any] | BaseSerializer | None = ...
    many: bool = ...
    default_error_messages: dict[str, Any] = ...
    allow_empty: bool | None = ...
    def __init__(
        self,
        instance: Any | None = ...,
        data: Any = ...,
        partial: bool = ...,
        context: dict[str, Any] = ...,
        allow_empty: bool = ...,
        child: Field[Any, Any, Any, Any] | BaseSerializer | None = ...,
        read_only: bool = ...,
        write_only: bool = ...,
        required: bool = ...,
        default: Any = ...,
        initial: Any = ...,
        source: str = ...,
        label: str = ...,
        help_text: str = ...,
        style: dict[str, Any] = ...,
        error_messages: dict[str, str] = ...,
        validators: Sequence[Callable[..., Any]] = ...,
        allow_null: bool = ...,
    ): ...
    def get_initial(self) -> list[Mapping[Any, Any]]: ...
    def validate(self, attrs: Any) -> Any: ...
    @property
    def data(self) -> ReturnList: ...
    @property
    def errors(self) -> ReturnList: ...

def raise_errors_on_nested_writes(method_name: str, serializer: BaseSerializer, validated_data: Any) -> NoReturn: ...

class ModelSerializer(Serializer, BaseSerializer):
    serializer_field_mapping: dict[type[models.Field[Any, Any]], Field[Any, Any, Any, Any]] = ...
    serializer_related_field: RelatedField = ...
    serializer_related_to_field: RelatedField = ...
    serializer_url_field: RelatedField = ...
    serializer_choice_field: Field[Any, Any, Any, Any] = ...
    url_field_name: str | None = ...
    instance: Any

    class Meta:
        model: Any
        fields: Sequence[str] | Literal["__all__"]
        read_only_fields: Sequence[str] | None
        exclude: Sequence[str] | None
        depth: int | None
        extra_kwargs: dict[str, dict[str, Any]]
    def __init__(
        self,
        instance: None | Any | Sequence[Any] | QuerySet[Any] | Manager[Any] = ...,
        data: Any = ...,
        partial: bool = ...,
        many: bool = ...,
        context: dict[str, Any] = ...,
        read_only: bool = ...,
        write_only: bool = ...,
        required: bool = ...,
        default: Any | Sequence[Any] | Callable[[], Any | Sequence[Any]] = ...,
        initial: Any | Sequence[Any] | Callable[[], Any | Sequence[Any]] = ...,
        source: str = ...,
        label: str = ...,
        help_text: str = ...,
        style: dict[str, Any] = ...,
        error_messages: dict[str, str] = ...,
        validators: Sequence[Callable[..., Any]] = ...,
        allow_null: bool = ...,
        allow_empty: bool = ...,
    ): ...
    def update(self, instance: Any, validated_data: Any) -> Any: ...
    def create(self, validated_data: Any) -> Any: ...
    def save(self, **kwargs: Any) -> Any: ...
    def to_representation(self, instance: Any) -> Any: ...
    def get_field_names(
        self, declared_fields: Mapping[str, Field[Any, Any, Any, Any]], info: FieldInfo
    ) -> list[str]: ...
    def get_default_field_names(
        self, declared_fields: Mapping[str, Field[Any, Any, Any, Any]], model_info: FieldInfo
    ) -> list[str]: ...
    def build_field(
        self, field_name: str, info: FieldInfo, model_class: Any, nested_depth: int
    ) -> tuple[Field[Any, Any, Any, Any], dict[str, Any]]: ...
    def build_standard_field(
        self, field_name: str, model_field: type[models.Field[Any, Any]]
    ) -> tuple[Field[Any, Any, Any, Any], dict[str, Any]]: ...
    def build_relational_field(
        self, field_name: str, relation_info: RelationInfo
    ) -> tuple[type[Field[Any, Any, Any, Any]], dict[str, Any]]: ...
    def build_nested_field(
        self, field_name: str, relation_info: RelationInfo, nested_depth: int
    ) -> tuple[Field[Any, Any, Any, Any], dict[str, Any]]: ...
    def build_property_field(
        self, field_name: str, model_class: Any
    ) -> tuple[Field[Any, Any, Any, Any], dict[str, Any]]: ...
    def build_url_field(
        self, field_name: str, model_class: Any
    ) -> tuple[Field[Any, Any, Any, Any], dict[str, Any]]: ...
    def build_unknown_field(self, field_name: str, model_class: Any) -> NoReturn: ...
    def include_extra_kwargs(
        self, kwargs: MutableMapping[str, Any], extra_kwargs: MutableMapping[str, Any]
    ) -> MutableMapping[str, Any]: ...
    def get_extra_kwargs(self) -> dict[str, Any]: ...
    def get_uniqueness_extra_kwargs(
        self,
        field_names: Iterable[str],
        declared_fields: Mapping[str, Field[Any, Any, Any, Any]],
        extra_kwargs: dict[str, Any],
    ) -> tuple[dict[str, Any], dict[str, HiddenField]]: ...
    def _get_model_fields(
        self,
        field_names: Iterable[str],
        declared_fields: Mapping[str, Field[Any, Any, Any, Any]],
        extra_kwargs: MutableMapping[str, Any],
    ) -> dict[str, models.Field[Any, Any]]: ...
    def get_unique_together_validators(self) -> list[Callable[..., Any]]: ...
    def get_unique_for_date_validators(self) -> list[Callable[..., Any]]: ...

class HyperlinkedModelSerializer(ModelSerializer): ...
