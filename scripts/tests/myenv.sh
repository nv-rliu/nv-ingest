# Minimal configuration for nv-ingest integration tests

# Dataset path - REQUIRED (no default, must be set for each test)
RESULTS=/raid/ralphl/nv-ingest-proj/bo20_run_py_results
DATASET_DIR=/raid/ralphl/nv-ingest-proj/data/bo20
LLM_SUMMARIZATION_MODEL=nvidia/nvidia-nemotron-nano-9b-v2

# Test name for collection naming (affects collection prefix)
TEST_NAME=can_delete_me

# Compose profiles to run in managed mode
PROFILES=retrieval,table-structure

# Readiness timeout in seconds (starts counting after docker compose finishes building/starting)
READINESS_TIMEOUT=600

# Where to write run artifacts (summary, stdout). Can be set to /raid/... if preferred
ARTIFACTS_DIR=/raid/ralphl/tmp/

# Spill directory used by test cases
SPILL_DIR=/raid/ralphl/tmp/nv-ingest-spill

# Milvus collection name. If empty, a timestamped name will be generated using TEST_NAME
# COLLECTION_NAME=

# Runtime configuration
HOSTNAME=localhost
SPARSE=true
GPU_SEARCH=false

# Embedding model (auto-detected if not set)
# EMBEDDING_NIM_MODEL_NAME=

# Extraction configuration
EXTRACT_TEXT=true

EXTRACT_TABLES=false
EXTRACT_CHARTS=false
EXTRACT_IMAGES=false
EXTRACT_INFOGRAPHICS=false

# EXTRACT_TABLES=true
# EXTRACT_CHARTS=true
# EXTRACT_IMAGES=true
# EXTRACT_INFOGRAPHICS=true

# not-multimodal

TEXT_DEPTH=page
TABLE_OUTPUT_FORMAT=markdown

# Logging configuration (set by run.py, can be overridden)
LOG_PATH=
