#  ********************************************************************************
#
#      __                ________
#     / /___  __  ______/ / __/ /___ _      __
#    / / __ \/ / / / __  / /_/ / __ \ | /| / /      A Multi-Agent Framework
#   / / /_/ / /_/ / /_/ / __/ / /_/ / |/ |/ /       in Python
#  /_/\____/\__,_/\__,_/_/ /_/\____/|__/|__/
#
#  Copyright (c) 2021-2022 FarSimple Oy.
#
#  The MIT License (MIT)
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software
#  and associated documentation files (the "Software"), to deal in the Software without restriction,
#  including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
#  subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included
#  in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
#  INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
#  WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH
#  THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#  ********************************************************************************

from __future__ import annotations

import functools
import time
from typing import Any, Callable

from loguru import logger


def trace(*, log_entry: bool = True, log_exit: bool = True, level: str = "TRACE") -> Any:
    """Decorator for tracing entry to and exit from a function.

    Args:
        log_entry: Log entry to function if True. Default is True.
        log_exit: Log exit from function if True. Default is True.
        level: Log level. Default is TRACE.

    Returns:
        Wrapper function for decorator.
    """

    def wrapper(func: Callable) -> Any:
        @functools.wraps(func)
        def wrapped(*args: Any, **kwargs: Any) -> Any:
            logger_ = logger.opt(depth=1)
            name = func.__name__
            args_repr = [repr(a) for a in args]
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            if log_entry:
                logger_.log(level, "Entering [{}(args={}, kwargs={})].", name, args_repr, kwargs_repr)
            result = func(*args, **kwargs)
            if log_exit:
                logger_.log(level, "Exiting [{}] with result [{}].", name, repr(result))
            return result

        return wrapped

    return wrapper


def timer(*, level: str = "TRACE") -> Any:
    """Decorator for timing the execution of a function.

    Args:
        level: Log level. Default is TRACE.

    Returns:
        Wrapper function for decorator.
    """

    def wrapper(func: Callable) -> Any:
        @functools.wraps(func)
        def wrapped(*args: Any, **kwargs: Any) -> Any:
            logger_ = logger.opt(depth=1)
            name = func.__name__
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            logger_.log(level, "Executed [{}] in {:f} seconds.", name, end - start)
            return result

        return wrapped

    return wrapper
