# SPDX-FileCopyrightText: Copyright (c) 2024-25, NVIDIA CORPORATION & AFFILIATES.
# All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import Any
from typing import Dict
from typing import Union
from uuid import UUID

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class ControlMessageTask(BaseModel):
    model_config = ConfigDict(extra="forbid")

    type: str
    id: str | UUID
    properties: dict[str, Any] = Field(default_factory=dict)
