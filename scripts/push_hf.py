"""Mirror data/ to the Hugging Face dataset xiaozhan-aihub/models (run by the daily sync).

Needs a Hugging Face token with write access to that dataset in the repository secret
HF_TOKEN; without it this step does nothing. Unchanged files are skipped, so a day
without changes makes no commit on Hugging Face.
"""

import os
import sys

from huggingface_hub import HfApi

REPO_ID = "xiaozhan-aihub/models"

token = os.environ.get("HF_TOKEN", "").strip()
if not token:
    print("HF_TOKEN is not set: skipping the Hugging Face mirror.")
    sys.exit(0)

info = HfApi(token=token).upload_folder(
    repo_id=REPO_ID,
    repo_type="dataset",
    folder_path="data",
    path_in_repo="data",
    commit_message="data: model catalogue (mirrored from github.com/xiaozhan-aihub/models)",
)
print(f"ok: {info}")
