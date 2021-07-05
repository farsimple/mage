#  ********************************************************************************
#
#     ____ ___  ____ _____ ____
#    / __ `__ \/ __ `/ __ `/ _ \    A Multi-Agent
#   / / / / / / /_/ / /_/ /  __/    Framework in Python
#  /_/ /_/ /_/\__,_/\__, /\___/
#                  /____/
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

from loguru import logger

from mage.common.decorators import timer, tracer
from mage.realm.world_configuration import WorldConfiguration


class World:
    """World class.

    The world in which the agent(s) act.

    Attributes:
        config: World configuration data.

    """

    @tracer()
    def __init__(self, config: WorldConfiguration) -> None:
        logger.info("Constructing world...")
        self.config = config

    @tracer()
    @timer()
    def hello(self) -> str:
        """Returns hello world string.

        Returns:
            Hello message using world name.

        """
        return "Hello {}!".format(self.config.name)
