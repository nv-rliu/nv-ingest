# SPDX-FileCopyrightText: Copyright (c) 2024, NVIDIA CORPORATION & AFFILIATES.
# All rights reserved.
# SPDX-License-Identifier: Apache-2.0

# NOTE: This code is duplicated from the ingest service:
# src/nv_ingest_client/schemas/response_schema.py
# Eventually we should move all client wrappers for the message broker into a shared library that both the ingest
# service and the client can use.

from typing import Optional
from typing import Union

from pydantic import BaseModel


class ResponseSchema(BaseModel):
    response_code: int
    response_reason: str | None = "OK"
    response: str | dict | None = None
    trace_id: str | None = None  # Unique trace ID
    transaction_id: str | None = None  # Unique transaction ID
