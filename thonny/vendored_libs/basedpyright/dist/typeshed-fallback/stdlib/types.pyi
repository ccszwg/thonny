import sys
from _typeshed import MaybeNone, SupportsKeysAndGetItem
from _typeshed.importlib import LoaderProtocol
from collections.abc import (
    AsyncGenerator,
    Awaitable,
    Callable,
    Coroutine,
    Generator,
    ItemsView,
    Iterable,
    Iterator,
    KeysView,
    MutableSequence,
    ValuesView,
)
from importlib.machinery import ModuleSpec

# pytype crashes if types.MappingProxyType inherits from collections.abc.Mapping instead of typing.Mapping
from typing import Any, ClassVar, Literal, Mapping, TypeVar, final, overload  # noqa: Y022
from typing_extensions import ParamSpec, Self, TypeVarTuple, deprecated

__all__ = [
    "FunctionType",
    "LambdaType",
    "CodeType",
    "MappingProxyType",
    "SimpleNamespace",
    "GeneratorType",
    "CoroutineType",
    "AsyncGeneratorType",
    "MethodType",
    "BuiltinFunctionType",
    "ModuleType",
    "TracebackType",
    "FrameType",
    "GetSetDescriptorType",
    "MemberDescriptorType",
    "new_class",
    "prepare_class",
    "DynamicClassAttribute",
    "coroutine",
    "BuiltinMethodType",
    "ClassMethodDescriptorType",
    "MethodDescriptorType",
    "MethodWrapperType",
    "WrapperDescriptorType",
    "resolve_bases",
    "CellType",
]

if sys.version_info >= (3, 9):
    __all__ += ["GenericAlias"]

if sys.version_info >= (3, 10):
    __all__ += ["EllipsisType", "NoneType", "NotImplementedType", "UnionType"]

if sys.version_info >= (3, 12):
    __all__ += ["get_original_bases"]

if sys.version_info >= (3, 13):
    __all__ += ["CapsuleType"]

# Note, all classes "defined" here require special handling.

_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")
_KT = TypeVar("_KT")
_VT_co = TypeVar("_VT_co", covariant=True)

# Make sure this class definition stays roughly in line with `builtins.function`
@final
class FunctionType:
    """
    Create a function object.

    code
      a code object
    globals
      the globals dictionary
    name
      a string that overrides the name from the code object
    argdefs
      a tuple that specifies the default argument values
    closure
      a tuple that supplies the bindings for free variables
    kwdefaults
      a dictionary that specifies the default keyword argument values
    """
    @property
    def __closure__(self) -> tuple[CellType, ...] | None: ...
    __code__: CodeType
    __defaults__: tuple[Any, ...] | None
    __dict__: dict[str, Any]
    @property
    def __globals__(self) -> dict[str, Any]: ...
    __name__: str
    __qualname__: str
    __annotations__: dict[str, Any]
    __kwdefaults__: dict[str, Any] | None
    if sys.version_info >= (3, 10):
        @property
        def __builtins__(self) -> dict[str, Any]: ...
    if sys.version_info >= (3, 12):
        __type_params__: tuple[TypeVar | ParamSpec | TypeVarTuple, ...]

    __module__: str
    def __new__(
        cls,
        code: CodeType,
        globals: dict[str, Any],
        name: str | None = ...,
        argdefs: tuple[object, ...] | None = ...,
        closure: tuple[CellType, ...] | None = ...,
    ) -> Self: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Call self as a function."""
        ...
    @overload
    def __get__(self, instance: None, owner: type, /) -> FunctionType:
        """Return an attribute of instance, which is of type owner."""
        ...
    @overload
    def __get__(self, instance: object, owner: type | None = None, /) -> MethodType:
        """Return an attribute of instance, which is of type owner."""
        ...

LambdaType = FunctionType

@final
class CodeType:
    """Create a code object.  Not for the faint of heart."""
    def __eq__(self, value: object, /) -> bool:
        """Return self==value."""
        ...
    def __hash__(self) -> int:
        """Return hash(self)."""
        ...
    @property
    def co_argcount(self) -> int: ...
    @property
    def co_posonlyargcount(self) -> int: ...
    @property
    def co_kwonlyargcount(self) -> int: ...
    @property
    def co_nlocals(self) -> int: ...
    @property
    def co_stacksize(self) -> int: ...
    @property
    def co_flags(self) -> int: ...
    @property
    def co_code(self) -> bytes: ...
    @property
    def co_consts(self) -> tuple[Any, ...]: ...
    @property
    def co_names(self) -> tuple[str, ...]: ...
    @property
    def co_varnames(self) -> tuple[str, ...]: ...
    @property
    def co_filename(self) -> str: ...
    @property
    def co_name(self) -> str: ...
    @property
    def co_firstlineno(self) -> int: ...
    if sys.version_info >= (3, 10):
        @property
        @deprecated("Will be removed in Python 3.14. Use the co_lines() method instead.")
        def co_lnotab(self) -> bytes: ...
    else:
        @property
        def co_lnotab(self) -> bytes: ...

    @property
    def co_freevars(self) -> tuple[str, ...]: ...
    @property
    def co_cellvars(self) -> tuple[str, ...]: ...
    if sys.version_info >= (3, 10):
        @property
        def co_linetable(self) -> bytes: ...
        def co_lines(self) -> Iterator[tuple[int, int, int | None]]: ...
    if sys.version_info >= (3, 11):
        @property
        def co_exceptiontable(self) -> bytes: ...
        @property
        def co_qualname(self) -> str: ...
        def co_positions(self) -> Iterable[tuple[int | None, int | None, int | None, int | None]]: ...

    if sys.version_info >= (3, 11):
        def __new__(
            cls,
            argcount: int,
            posonlyargcount: int,
            kwonlyargcount: int,
            nlocals: int,
            stacksize: int,
            flags: int,
            codestring: bytes,
            constants: tuple[object, ...],
            names: tuple[str, ...],
            varnames: tuple[str, ...],
            filename: str,
            name: str,
            qualname: str,
            firstlineno: int,
            linetable: bytes,
            exceptiontable: bytes,
            freevars: tuple[str, ...] = ...,
            cellvars: tuple[str, ...] = ...,
            /,
        ) -> Self: ...
    elif sys.version_info >= (3, 10):
        def __new__(
            cls,
            argcount: int,
            posonlyargcount: int,
            kwonlyargcount: int,
            nlocals: int,
            stacksize: int,
            flags: int,
            codestring: bytes,
            constants: tuple[object, ...],
            names: tuple[str, ...],
            varnames: tuple[str, ...],
            filename: str,
            name: str,
            firstlineno: int,
            linetable: bytes,
            freevars: tuple[str, ...] = ...,
            cellvars: tuple[str, ...] = ...,
            /,
        ) -> Self: ...
    else:
        def __new__(
            cls,
            argcount: int,
            posonlyargcount: int,
            kwonlyargcount: int,
            nlocals: int,
            stacksize: int,
            flags: int,
            codestring: bytes,
            constants: tuple[object, ...],
            names: tuple[str, ...],
            varnames: tuple[str, ...],
            filename: str,
            name: str,
            firstlineno: int,
            lnotab: bytes,
            freevars: tuple[str, ...] = ...,
            cellvars: tuple[str, ...] = ...,
            /,
        ) -> Self: ...
    if sys.version_info >= (3, 11):
        def replace(
            self,
            *,
            co_argcount: int = -1,
            co_posonlyargcount: int = -1,
            co_kwonlyargcount: int = -1,
            co_nlocals: int = -1,
            co_stacksize: int = -1,
            co_flags: int = -1,
            co_firstlineno: int = -1,
            co_code: bytes = ...,
            co_consts: tuple[object, ...] = ...,
            co_names: tuple[str, ...] = ...,
            co_varnames: tuple[str, ...] = ...,
            co_freevars: tuple[str, ...] = ...,
            co_cellvars: tuple[str, ...] = ...,
            co_filename: str = ...,
            co_name: str = ...,
            co_qualname: str = ...,
            co_linetable: bytes = ...,
            co_exceptiontable: bytes = ...,
        ) -> Self:
            """Return a copy of the code object with new values for the specified fields."""
            ...
    elif sys.version_info >= (3, 10):
        def replace(
            self,
            *,
            co_argcount: int = -1,
            co_posonlyargcount: int = -1,
            co_kwonlyargcount: int = -1,
            co_nlocals: int = -1,
            co_stacksize: int = -1,
            co_flags: int = -1,
            co_firstlineno: int = -1,
            co_code: bytes = ...,
            co_consts: tuple[object, ...] = ...,
            co_names: tuple[str, ...] = ...,
            co_varnames: tuple[str, ...] = ...,
            co_freevars: tuple[str, ...] = ...,
            co_cellvars: tuple[str, ...] = ...,
            co_filename: str = ...,
            co_name: str = ...,
            co_linetable: bytes = ...,
        ) -> Self:
            """Return a copy of the code object with new values for the specified fields."""
            ...
    else:
        def replace(
            self,
            *,
            co_argcount: int = -1,
            co_posonlyargcount: int = -1,
            co_kwonlyargcount: int = -1,
            co_nlocals: int = -1,
            co_stacksize: int = -1,
            co_flags: int = -1,
            co_firstlineno: int = -1,
            co_code: bytes = ...,
            co_consts: tuple[object, ...] = ...,
            co_names: tuple[str, ...] = ...,
            co_varnames: tuple[str, ...] = ...,
            co_freevars: tuple[str, ...] = ...,
            co_cellvars: tuple[str, ...] = ...,
            co_filename: str = ...,
            co_name: str = ...,
            co_lnotab: bytes = ...,
        ) -> Self:
            """Return a copy of the code object with new values for the specified fields."""
            ...

    if sys.version_info >= (3, 13):
        __replace__ = replace

@final
class MappingProxyType(Mapping[_KT, _VT_co]):
    """Read-only proxy of a mapping."""
    __hash__: ClassVar[None]  # type: ignore[assignment]
    def __new__(cls, mapping: SupportsKeysAndGetItem[_KT, _VT_co]) -> Self: ...
    def __getitem__(self, key: _KT, /) -> _VT_co:
        """Return self[key]."""
        ...
    def __iter__(self) -> Iterator[_KT]:
        """Implement iter(self)."""
        ...
    def __len__(self) -> int:
        """Return len(self)."""
        ...
    def __eq__(self, value: object, /) -> bool:
        """Return self==value."""
        ...
    def copy(self) -> dict[_KT, _VT_co]:
        """D.copy() -> a shallow copy of D"""
        ...
    def keys(self) -> KeysView[_KT]:
        """D.keys() -> a set-like object providing a view on D's keys"""
        ...
    def values(self) -> ValuesView[_VT_co]:
        """D.values() -> an object providing a view on D's values"""
        ...
    def items(self) -> ItemsView[_KT, _VT_co]:
        """D.items() -> a set-like object providing a view on D's items"""
        ...
    @overload
    def get(self, key: _KT, /) -> _VT_co | None:
        """Return the value for key if key is in the mapping, else default."""
        ...
    @overload
    def get(self, key: _KT, default: _VT_co | _T2, /) -> _VT_co | _T2:
        """Return the value for key if key is in the mapping, else default."""
        ...
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, item: Any, /) -> GenericAlias:
            """See PEP 585"""
            ...
        def __reversed__(self) -> Iterator[_KT]:
            """D.__reversed__() -> reverse iterator"""
            ...
        def __or__(self, value: Mapping[_T1, _T2], /) -> dict[_KT | _T1, _VT_co | _T2]:
            """Return self|value."""
            ...
        def __ror__(self, value: Mapping[_T1, _T2], /) -> dict[_KT | _T1, _VT_co | _T2]:
            """Return value|self."""
            ...

class SimpleNamespace:
    __hash__: ClassVar[None]  # type: ignore[assignment]
    if sys.version_info >= (3, 13):
        def __init__(self, mapping_or_iterable: Mapping[str, Any] | Iterable[tuple[str, Any]] = (), /, **kwargs: Any) -> None: ...
    else:
        def __init__(self, **kwargs: Any) -> None: ...

    def __eq__(self, value: object, /) -> bool:
        """Return self==value."""
        ...
    def __getattribute__(self, name: str, /) -> Any:
        """Return getattr(self, name)."""
        ...
    def __setattr__(self, name: str, value: Any, /) -> None:
        """Implement setattr(self, name, value)."""
        ...
    def __delattr__(self, name: str, /) -> None:
        """Implement delattr(self, name)."""
        ...
    if sys.version_info >= (3, 13):
        def __replace__(self, **kwargs: Any) -> Self:
            """Return a copy of the namespace object with new values for the specified attributes."""
            ...

class ModuleType:
    """
    Create a module object.

    The name must be a string; the optional doc argument can have any type.
    """
    __name__: str
    __file__: str | None
    @property
    def __dict__(self) -> dict[str, Any]: ...  # type: ignore[override]
    __loader__: LoaderProtocol | None
    __package__: str | None
    __path__: MutableSequence[str]
    __spec__: ModuleSpec | None
    # N.B. Although this is the same type as `builtins.object.__doc__`,
    # it is deliberately redeclared here. Most symbols declared in the namespace
    # of `types.ModuleType` are available as "implicit globals" within a module's
    # namespace, but this is not true for symbols declared in the namespace of `builtins.object`.
    # Redeclaring `__doc__` here helps some type checkers understand that `__doc__` is available
    # as an implicit global in all modules, similar to `__name__`, `__file__`, `__spec__`, etc.
    __doc__: str | None
    def __init__(self, name: str, doc: str | None = ...) -> None: ...
    # __getattr__ doesn't exist at runtime,
    # but having it here in typeshed makes dynamic imports
    # using `builtins.__import__` or `importlib.import_module` less painful
    def __getattr__(self, name: str) -> Any: ...

@final
class CellType:
    """
    Create a new cell object.

     contents
       the contents of the cell. If not specified, the cell will be empty,
       and 
    further attempts to access its cell_contents attribute will
       raise a ValueError.
    """
    def __new__(cls, contents: object = ..., /) -> Self: ...
    __hash__: ClassVar[None]  # type: ignore[assignment]
    cell_contents: Any

_YieldT_co = TypeVar("_YieldT_co", covariant=True)
_SendT_contra = TypeVar("_SendT_contra", contravariant=True)
_ReturnT_co = TypeVar("_ReturnT_co", covariant=True)

@final
class GeneratorType(Generator[_YieldT_co, _SendT_contra, _ReturnT_co]):
    @property
    def gi_yieldfrom(self) -> GeneratorType[_YieldT_co, _SendT_contra, Any] | None:
        """object being iterated by yield from, or None"""
        ...
    if sys.version_info >= (3, 11):
        @property
        def gi_suspended(self) -> bool: ...
    __name__: str
    __qualname__: str
    def __iter__(self) -> Self:
        """Implement iter(self)."""
        ...
    def __next__(self) -> _YieldT_co:
        """Implement next(self)."""
        ...
    def send(self, arg: _SendT_contra, /) -> _YieldT_co:
        """
        send(arg) -> send 'arg' into generator,
        return next yielded value or raise StopIteration.
        """
        ...
    @overload
    def throw(
        self, typ: type[BaseException], val: BaseException | object = ..., tb: TracebackType | None = ..., /
    ) -> _YieldT_co:
        """
        throw(value)
        throw(type[,value[,tb]])

        Raise exception in generator, return next yielded value or raise
        StopIteration.
        the (type, val, tb) signature is deprecated, 
        and may be removed in a future version of Python.
        """
        ...
    @overload
    def throw(self, typ: BaseException, val: None = None, tb: TracebackType | None = ..., /) -> _YieldT_co:
        """
        throw(value)
        throw(type[,value[,tb]])

        Raise exception in generator, return next yielded value or raise
        StopIteration.
        the (type, val, tb) signature is deprecated, 
        and may be removed in a future version of Python.
        """
        ...
    if sys.version_info >= (3, 13):
        def __class_getitem__(cls, item: Any, /) -> Any:
            """See PEP 585"""
            ...

@final
class AsyncGeneratorType(AsyncGenerator[_YieldT_co, _SendT_contra]):
    @property
    def ag_await(self) -> Awaitable[Any] | None:
        """object being awaited on, or None"""
        ...
    __name__: str
    __qualname__: str
    if sys.version_info >= (3, 12):
        @property
        def ag_suspended(self) -> bool: ...

    def __aiter__(self) -> Self:
        """Return an awaitable, that resolves in asynchronous iterator."""
        ...
    def __anext__(self) -> Coroutine[Any, Any, _YieldT_co]:
        """Return a value or raise StopAsyncIteration."""
        ...
    def asend(self, val: _SendT_contra, /) -> Coroutine[Any, Any, _YieldT_co]:
        """asend(v) -> send 'v' in generator."""
        ...
    @overload
    async def athrow(
        self, typ: type[BaseException], val: BaseException | object = ..., tb: TracebackType | None = ..., /
    ) -> _YieldT_co:
        """
        athrow(value)
        athrow(type[,value[,tb]])

        raise exception in generator.
        the (type, val, tb) signature is deprecated, 
        and may be removed in a future version of Python.
        """
        ...
    @overload
    async def athrow(self, typ: BaseException, val: None = None, tb: TracebackType | None = ..., /) -> _YieldT_co:
        """
        athrow(value)
        athrow(type[,value[,tb]])

        raise exception in generator.
        the (type, val, tb) signature is deprecated, 
        and may be removed in a future version of Python.
        """
        ...
    def aclose(self) -> Coroutine[Any, Any, None]:
        """aclose() -> raise GeneratorExit inside generator."""
        ...
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, item: Any, /) -> GenericAlias:
            """See PEP 585"""
            ...

@final
class CoroutineType(Coroutine[_YieldT_co, _SendT_contra, _ReturnT_co]):
    __name__: str
    __qualname__: str
    @property
    def cr_origin(self) -> tuple[tuple[str, int, str], ...] | None: ...
    if sys.version_info >= (3, 11):
        @property
        def cr_suspended(self) -> bool: ...

    def close(self) -> None:
        """close() -> raise GeneratorExit inside coroutine."""
        ...
    def __await__(self) -> Generator[Any, None, _ReturnT_co]:
        """Return an iterator to be used in await expression."""
        ...
    def send(self, arg: _SendT_contra, /) -> _YieldT_co:
        """
        send(arg) -> send 'arg' into coroutine,
        return next iterated value or raise StopIteration.
        """
        ...
    @overload
    def throw(
        self, typ: type[BaseException], val: BaseException | object = ..., tb: TracebackType | None = ..., /
    ) -> _YieldT_co:
        """
        throw(value)
        throw(type[,value[,traceback]])

        Raise exception in coroutine, return next iterated value or raise
        StopIteration.
        the (type, val, tb) signature is deprecated, 
        and may be removed in a future version of Python.
        """
        ...
    @overload
    def throw(self, typ: BaseException, val: None = None, tb: TracebackType | None = ..., /) -> _YieldT_co:
        """
        throw(value)
        throw(type[,value[,traceback]])

        Raise exception in coroutine, return next iterated value or raise
        StopIteration.
        the (type, val, tb) signature is deprecated, 
        and may be removed in a future version of Python.
        """
        ...
    if sys.version_info >= (3, 13):
        def __class_getitem__(cls, item: Any, /) -> Any:
            """See PEP 585"""
            ...

@final
class MethodType:
    """Create a bound instance method object."""
    @property
    def __closure__(self) -> tuple[CellType, ...] | None: ...  # inherited from the added function
    @property
    def __code__(self) -> CodeType: ...  # inherited from the added function
    @property
    def __defaults__(self) -> tuple[Any, ...] | None: ...  # inherited from the added function
    @property
    def __func__(self) -> Callable[..., Any]:
        """the function (or other callable) implementing a method"""
        ...
    @property
    def __self__(self) -> object:
        """the instance to which a method is bound"""
        ...
    @property
    def __name__(self) -> str: ...  # inherited from the added function
    @property
    def __qualname__(self) -> str: ...  # inherited from the added function
    def __new__(cls, func: Callable[..., Any], obj: object, /) -> Self: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Call self as a function."""
        ...
    def __eq__(self, value: object, /) -> bool:
        """Return self==value."""
        ...
    def __hash__(self) -> int:
        """Return hash(self)."""
        ...

@final
class BuiltinFunctionType:
    @property
    def __self__(self) -> object | ModuleType: ...
    @property
    def __name__(self) -> str: ...
    @property
    def __qualname__(self) -> str: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Call self as a function."""
        ...
    def __eq__(self, value: object, /) -> bool:
        """Return self==value."""
        ...
    def __hash__(self) -> int:
        """Return hash(self)."""
        ...

BuiltinMethodType = BuiltinFunctionType

@final
class WrapperDescriptorType:
    @property
    def __name__(self) -> str: ...
    @property
    def __qualname__(self) -> str: ...
    @property
    def __objclass__(self) -> type: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Call self as a function."""
        ...
    def __get__(self, instance: Any, owner: type | None = None, /) -> Any:
        """Return an attribute of instance, which is of type owner."""
        ...

@final
class MethodWrapperType:
    @property
    def __self__(self) -> object: ...
    @property
    def __name__(self) -> str: ...
    @property
    def __qualname__(self) -> str: ...
    @property
    def __objclass__(self) -> type: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Call self as a function."""
        ...
    def __eq__(self, value: object, /) -> bool:
        """Return self==value."""
        ...
    def __ne__(self, value: object, /) -> bool:
        """Return self!=value."""
        ...
    def __hash__(self) -> int:
        """Return hash(self)."""
        ...

@final
class MethodDescriptorType:
    @property
    def __name__(self) -> str: ...
    @property
    def __qualname__(self) -> str: ...
    @property
    def __objclass__(self) -> type: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Call self as a function."""
        ...
    def __get__(self, instance: Any, owner: type | None = None, /) -> Any:
        """Return an attribute of instance, which is of type owner."""
        ...

@final
class ClassMethodDescriptorType:
    @property
    def __name__(self) -> str: ...
    @property
    def __qualname__(self) -> str: ...
    @property
    def __objclass__(self) -> type: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Call self as a function."""
        ...
    def __get__(self, instance: Any, owner: type | None = None, /) -> Any:
        """Return an attribute of instance, which is of type owner."""
        ...

@final
class TracebackType:
    """Create a new traceback object."""
    def __new__(cls, tb_next: TracebackType | None, tb_frame: FrameType, tb_lasti: int, tb_lineno: int) -> Self: ...
    tb_next: TracebackType | None
    # the rest are read-only
    @property
    def tb_frame(self) -> FrameType: ...
    @property
    def tb_lasti(self) -> int: ...
    @property
    def tb_lineno(self) -> int: ...

@final
class FrameType:
    @property
    def f_back(self) -> FrameType | None: ...
    @property
    def f_builtins(self) -> dict[str, Any]: ...
    @property
    def f_code(self) -> CodeType: ...
    @property
    def f_globals(self) -> dict[str, Any]: ...
    @property
    def f_lasti(self) -> int: ...
    # see discussion in #6769: f_lineno *can* sometimes be None,
    # but you should probably file a bug report with CPython if you encounter it being None in the wild.
    # An `int | None` annotation here causes too many false-positive errors, so applying `int | Any`.
    @property
    def f_lineno(self) -> int | MaybeNone: ...
    @property
    def f_locals(self) -> dict[str, Any]: ...
    f_trace: Callable[[FrameType, str, Any], Any] | None
    f_trace_lines: bool
    f_trace_opcodes: bool
    def clear(self) -> None:
        """F.clear(): clear most references held by the frame"""
        ...

@final
class GetSetDescriptorType:
    @property
    def __name__(self) -> str: ...
    @property
    def __qualname__(self) -> str: ...
    @property
    def __objclass__(self) -> type: ...
    def __get__(self, instance: Any, owner: type | None = None, /) -> Any:
        """Return an attribute of instance, which is of type owner."""
        ...
    def __set__(self, instance: Any, value: Any, /) -> None:
        """Set an attribute of instance to value."""
        ...
    def __delete__(self, instance: Any, /) -> None:
        """Delete an attribute of instance."""
        ...

@final
class MemberDescriptorType:
    @property
    def __name__(self) -> str: ...
    @property
    def __qualname__(self) -> str: ...
    @property
    def __objclass__(self) -> type: ...
    def __get__(self, instance: Any, owner: type | None = None, /) -> Any:
        """Return an attribute of instance, which is of type owner."""
        ...
    def __set__(self, instance: Any, value: Any, /) -> None:
        """Set an attribute of instance to value."""
        ...
    def __delete__(self, instance: Any, /) -> None:
        """Delete an attribute of instance."""
        ...

def new_class(
    name: str,
    bases: Iterable[object] = (),
    kwds: dict[str, Any] | None = None,
    exec_body: Callable[[dict[str, Any]], object] | None = None,
) -> type: ...
def resolve_bases(bases: Iterable[object]) -> tuple[Any, ...]: ...
def prepare_class(
    name: str, bases: tuple[type, ...] = (), kwds: dict[str, Any] | None = None
) -> tuple[type, dict[str, Any], dict[str, Any]]: ...

if sys.version_info >= (3, 12):
    def get_original_bases(cls: type, /) -> tuple[Any, ...]: ...

# Actually a different type, but `property` is special and we want that too.
DynamicClassAttribute = property

_Fn = TypeVar("_Fn", bound=Callable[..., object])
_R = TypeVar("_R")
_P = ParamSpec("_P")

# it's not really an Awaitable, but can be used in an await expression. Real type: Generator & Awaitable
@overload
def coroutine(func: Callable[_P, Generator[Any, Any, _R]]) -> Callable[_P, Awaitable[_R]]: ...
@overload
def coroutine(func: _Fn) -> _Fn: ...

if sys.version_info >= (3, 9):
    class GenericAlias:
        @property
        def __origin__(self) -> type: ...
        @property
        def __args__(self) -> tuple[Any, ...]: ...
        @property
        def __parameters__(self) -> tuple[Any, ...]:
            """Type variables in the GenericAlias."""
            ...
        def __new__(cls, origin: type, args: Any) -> Self: ...
        def __getitem__(self, typeargs: Any, /) -> GenericAlias:
            """Return self[key]."""
            ...
        def __eq__(self, value: object, /) -> bool:
            """Return self==value."""
            ...
        def __hash__(self) -> int:
            """Return hash(self)."""
            ...
        if sys.version_info >= (3, 11):
            @property
            def __unpacked__(self) -> bool: ...
            @property
            def __typing_unpacked_tuple_args__(self) -> tuple[Any, ...] | None: ...
        if sys.version_info >= (3, 10):
            def __or__(self, value: Any, /) -> UnionType:
                """Return self|value."""
                ...
            def __ror__(self, value: Any, /) -> UnionType:
                """Return value|self."""
                ...

        # GenericAlias delegates attr access to `__origin__`
        def __getattr__(self, name: str) -> Any: ...

if sys.version_info >= (3, 10):
    @final
    class NoneType:
        """The type of the None singleton."""
        def __bool__(self) -> Literal[False]:
            """True if self else False"""
            ...

    @final
    class EllipsisType:
        """The type of the Ellipsis singleton."""
        ...

    from builtins import _NotImplementedType

    NotImplementedType = _NotImplementedType
    @final
    class UnionType:
        @property
        def __args__(self) -> tuple[Any, ...]: ...
        def __or__(self, value: Any, /) -> UnionType:
            """Return self|value."""
            ...
        def __ror__(self, value: Any, /) -> UnionType:
            """Return value|self."""
            ...
        def __eq__(self, value: object, /) -> bool:
            """Return self==value."""
            ...
        def __hash__(self) -> int:
            """Return hash(self)."""
            ...

if sys.version_info >= (3, 13):
    @final
    class CapsuleType:
        """
        Capsule objects let you wrap a C "void *" pointer in a Python
        object.  They're a way of passing data through the Python interpreter
        without creating your own custom type.

        Capsules are used for communication between extension modules.
        They provide a way for an extension module to export a C interface
        to other extension modules, so that extension modules can use the
        Python import mechanism to link to one another.
        """
        ...