# SPDX-FileCopyrightText: Copyright (c) 2024, NVIDIA CORPORATION & AFFILIATES.
# All rights reserved.
# SPDX-License-Identifier: Apache-2.0


from typing import Annotated

from nv_ingest_api.internal.schemas.message_brokers.message_broker_client_schema import MessageBrokerClientSchema
from pydantic import BaseModel
from pydantic import Field


class MessageBrokerTaskSinkSchema(BaseModel):
    broker_client: MessageBrokerClientSchema = MessageBrokerClientSchema()

    raise_on_failure: bool = False

    progress_engines: Annotated[int, Field(ge=1)] = 6
