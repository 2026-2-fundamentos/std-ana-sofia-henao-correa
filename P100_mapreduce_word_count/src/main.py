import glob
import os.path
import shutil
import string
import time

ACTIVITY_FOLDER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FOLDER = ACTIVITY_DIR / "data"
INPUT_FOLDER = ACTIVITY_DIR / "temp" / "input"
OUTPUT_FOLDER = ACTIVITY_DIR / "temp" / "output"
SUBMISSION_FOLDER = ACTIVITY_DIR / "submission"


if os.path.exists(INPUT_FOLDER):
        for file in glob.glob(f"{INPUT_FOLDER}/*"):
            os.remove(file)

else:
      os.makedirs(INPUT_FOLDER)
        import os