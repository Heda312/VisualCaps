import os
import cv2
import shutil
import pandas as pd

# =====================================================
# CONFIG
# =====================================================

SOURCE_DIR = "dataset"
OUTPUT_DIR = "dataset_clean"

MIN_DURATION = 2
MAX_DURATION = 5

VIDEO_EXTENSIONS = (
    ".mp4",
    ".avi",
    ".mov",
    ".mkv"
)

os.makedirs(OUTPUT_DIR, exist_ok=True)

# =====================================================
# STORAGE
# =====================================================

cleaned_data = []
removed_data = []

total_files = 0
valid_files = 0
removed_files = 0

print("=" * 60)
print("DATA CLEANING")
print("=" * 60)

# =====================================================
# WALK DATASET
# =====================================================

for root, dirs, files in os.walk(SOURCE_DIR):

    video_files = [
        f for f in files
        if f.lower().endswith(VIDEO_EXTENSIONS)
    ]

    if len(video_files) == 0:
        continue

    relative_path = os.path.relpath(
        root,
        SOURCE_DIR
    )

    output_label_dir = os.path.join(
        OUTPUT_DIR,
        relative_path
    )

    os.makedirs(
        output_label_dir,
        exist_ok=True
    )

    label = os.path.basename(root)

    print(f"\nProcessing: {label}")

    for filename in video_files:

        total_files += 1

        filepath = os.path.join(
            root,
            filename
        )

        reason = None

        try:

            # ==========================
            # FILE SIZE
            # ==========================

            if os.path.getsize(filepath) == 0:

                reason = "empty_file"

            else:

                cap = cv2.VideoCapture(filepath)

                if not cap.isOpened():

                    reason = "cannot_open"

                else:

                    fps = cap.get(
                        cv2.CAP_PROP_FPS
                    )

                    frame_count = int(
                        cap.get(
                            cv2.CAP_PROP_FRAME_COUNT
                        )
                    )

                    duration = (
                        frame_count / fps
                        if fps > 0
                        else 0
                    )

                    if fps <= 0:

                        reason = "invalid_fps"

                    elif frame_count <= 0:

                        reason = "invalid_frame_count"

                    elif duration < MIN_DURATION:

                        reason = "too_short"

                    elif duration > MAX_DURATION:

                        reason = "too_long"

                    cap.release()

            # ==========================
            # REMOVE
            # ==========================

            if reason:

                removed_files += 1

                removed_data.append(
                    {
                        "label": label,
                        "file": filename,
                        "reason": reason
                    }
                )

                continue

            # ==========================
            # COPY VALID FILE
            # ==========================

            destination = os.path.join(
                output_label_dir,
                filename
            )

            shutil.copy2(
                filepath,
                destination
            )

            valid_files += 1

            cleaned_data.append(
                {
                    "label": label,
                    "file": filename
                }
            )

        except Exception as e:

            removed_files += 1

            removed_data.append(
                {
                    "label": label,
                    "file": filename,
                    "reason": str(e)
                }
            )

# =====================================================
# SAVE REPORT
# =====================================================

REPORT_DIR = "reports"

os.makedirs(
    REPORT_DIR,
    exist_ok=True
)

pd.DataFrame(cleaned_data).to_csv(
    os.path.join(
        REPORT_DIR,
        "valid_files.csv"
    ),
    index=False
)

pd.DataFrame(removed_data).to_csv(
    os.path.join(
        REPORT_DIR,
        "removed_files.csv"
    ),
    index=False
)

# =====================================================
# TXT REPORT
# =====================================================

report_path = os.path.join(
    REPORT_DIR,
    "cleaning_report.txt"
)

with open(
    report_path,
    "w",
    encoding="utf-8"
) as f:

    f.write("DATA CLEANING REPORT\n")
    f.write("=" * 50 + "\n\n")

    f.write(
        f"Total Files     : {total_files}\n"
    )

    f.write(
        f"Valid Files     : {valid_files}\n"
    )

    f.write(
        f"Removed Files   : {removed_files}\n\n"
    )

    if len(removed_data) > 0:

        reason_df = (
            pd.DataFrame(
                removed_data
            )["reason"]
            .value_counts()
        )

        f.write(
            "REMOVAL REASONS\n"
        )

        f.write(
            "-" * 30 + "\n"
        )

        f.write(
            reason_df.to_string()
        )

print("\n")
print("=" * 60)
print("CLEANING FINISHED")
print("=" * 60)

print(f"Total Files   : {total_files}")
print(f"Valid Files   : {valid_files}")
print(f"Removed Files : {removed_files}")

print("\nOutput Folder:")
print(OUTPUT_DIR)