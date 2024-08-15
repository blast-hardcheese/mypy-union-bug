from typing import Literal, Union
from pydantic import BaseModel, Field, TypeAdapter


class FooInA(BaseModel):
    kind: Literal["a"] = Field("a", alias="$foo")
    a: bytes


class FooInB(BaseModel):
    kind: Literal["b"] = Field("b", alias="$foo")
    b: int


FooIn = Union[FooInA, FooInB]

def branchA(x: FooInA):
    """ No error, encode BaseModel subclass """
    TypeAdapter(FooInA).dump_python(
        x,
        by_alias=True,
        exclude_none=True,
    )

def branchB(x: FooInB):
    """ No error, encode BaseModel subclass """
    TypeAdapter(FooInB).dump_python(
        x,
        by_alias=True,
        exclude_none=True,
    )

def union(x: FooIn):
    """ Error, encode BaseModel union """
    TypeAdapter(FooIn).dump_python(
        # Argument 1 to "dump_python" of "TypeAdapter" has incompatible
        # type "FooInA | FooInB"; expected "<typing special form>"  [arg-type]
        x,
        by_alias=True,
        exclude_none=True,
    )
