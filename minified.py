from typing import Any, Generic, Literal, TypeVar, Union, overload

A = TypeVar('A')

class MiniTypeAdapter(Generic[A]):
    @overload
    def __init__(
        self,
        type: type[A],
    ) -> None: ...

    # This second overload is for unsupported special forms (such as Annotated, Union, etc.)
    # Currently there is no way to type this correctly
    # See https://github.com/python/typing/pull/1618
    @overload
    def __init__(
        self,
        type: Any,
    ) -> None: ...

    def __init__(
        self,
        type: Any,
    ) -> None:
        self._type = type


    def dump_python(self, instance: A) -> A:
        return instance

class FooInA:
    kind: Literal["a"]
    a: bytes


class FooInB:
    kind: Literal["b"]
    b: int


FooIn = Union[FooInA, FooInB]

def branchA(x: FooInA):
    """ No error, encode class """
    MiniTypeAdapter(FooInA).dump_python(
        x,
    )

def branchB(x: FooInB):
    """ No error, encode class """
    MiniTypeAdapter(FooInB).dump_python(
        x,
    )

def union(x: FooIn):
    """ Error, encode class union """
    MiniTypeAdapter(FooIn).dump_python(
        # Argument 1 to "dump_python" of "TypeAdapter" has incompatible
        # type "FooInA | FooInB"; expected "<typing special form>"  [arg-type]
        x,
    )
