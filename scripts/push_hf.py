"""Mirror data/ and the dataset card to Hugging Face (run by the daily sync workflow).

Uploads data/models.{json,csv} and build/hf/README.md (written by scripts/render.py) to the
dataset xiaozhan-aihub/ai-model-api-pricing. Needs a token with write access to that dataset
in the repository secret HF_TOKEN; without it this step does nothing. Unchanged files are
skipped, so a day without changes makes no commit on Hugging Face.
"""

import os
import shutil
import sys
import tempfile

from huggingface_hub import HfApi

REPO_ID = "xiaozhan-aihub/ai-model-api-pricing"
CARD = "build/hf/README.md"

token = os.environ.get("HF_TOKEN", "").strip()
if not token:
    print("HF_TOKEN is not set: skipping the Hugging Face mirror.")
    sys.exit(0)

with tempfile.TemporaryDirectory() as tmp:
    shutil.copytree("data", os.path.join(tmp, "data"))
    if os.path.exists(CARD):
        shutil.copy(CARD, os.path.join(tmp, "README.md"))
    else:
        print(f"{CARD} not found: uploading the data only.")
    info = HfApi(token=token).upload_folder(
        repo_id=REPO_ID,
        repo_type="dataset",
        folder_path=tmp,
        commit_message="Update model catalogue (mirrored from github.com/xiaozhan-aihub/ai-model-api-pricing)",
    )
print(f"ok: {info}")
