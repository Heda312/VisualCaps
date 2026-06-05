import os
import cv2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =====================================================
# CONFIG
# =====================================================

DATASET_DIR = "dataset_clean"

REPORT_DIR = "reports"
FIGURE_DIR = os.path.join(REPORT_DIR, "figures")

os.makedirs(REPORT_DIR, exist_ok=True)
os.makedirs(FIGURE_DIR, exist_ok=True)

VIDEO_EXTENSIONS = (
    ".mp4",
    ".avi",
    ".mov",
    ".mkv"
)

# =====================================================
# STORAGE
# =====================================================

records = []

print("=" * 60)
print("DATASET VALIDATION")
print("=" * 60)

# =====================================================
# SCAN DATASET
# =====================================================

for root, dirs, files in os.walk(DATASET_DIR):

    video_files = [
        f for f in files
        if f.lower().endswith(VIDEO_EXTENSIONS)
    ]

    if len(video_files) == 0:
        continue

    label = os.path.basename(root)

    print(f"Checking: {label}")

    for filename in video_files:

        filepath = os.path.join(root, filename)

        cap = cv2.VideoCapture(filepath)

        if not cap.isOpened():
            continue

        fps = cap.get(cv2.CAP_PROP_FPS)

        frame_count = int(
            cap.get(cv2.CAP_PROP_FRAME_COUNT)
        )

        width = int(
            cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        )

        height = int(
            cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        )

        duration = (
            frame_count / fps
            if fps > 0
            else 0
        )

        records.append({
            "label": label,
            "file": filename,
            "fps": fps,
            "frame_count": frame_count,
            "duration_sec": duration,
            "width": width,
            "height": height
        })

        cap.release()

# =====================================================
# DATAFRAME
# =====================================================

df = pd.DataFrame(records)

if df.empty:
    print("No valid videos found.")
    exit()

# =====================================================
# CLASS DISTRIBUTION
# =====================================================

label_dist = (
    df["label"]
    .value_counts()
    .sort_index()
)

label_dist_df = (
    label_dist
    .reset_index()
)

label_dist_df.columns = [
    "label",
    "video_count"
]

label_dist_df.to_csv(
    os.path.join(
        REPORT_DIR,
        "validation_label_distribution.csv"
    ),
    index=False
)

# =====================================================
# BASIC STATS
# =====================================================

total_videos = len(df)

total_labels = df["label"].nunique()

min_class = label_dist.min()
max_class = label_dist.max()

mean_class = label_dist.mean()
median_class = label_dist.median()

imbalance_ratio = (
    max_class / min_class
)

# =====================================================
# VIDEO STATS
# =====================================================

avg_duration = df["duration_sec"].mean()
min_duration = df["duration_sec"].min()
max_duration = df["duration_sec"].max()

avg_fps = df["fps"].mean()

avg_frames = df["frame_count"].mean()

# =====================================================
# UNIQUE RESOLUTION
# =====================================================

resolutions = (
    df[["width", "height"]]
    .drop_duplicates()
)

# =====================================================
# VALIDATION STATUS
# =====================================================

dataset_valid = True

issues = []

if min_class < 20:
    dataset_valid = False
    issues.append(
        "Some classes contain less than 20 samples."
    )

if imbalance_ratio > 3:
    issues.append(
        "Potential class imbalance detected."
    )

if len(resolutions) > 1:
    issues.append(
        "Multiple video resolutions detected."
    )

# =====================================================
# SAVE DISTRIBUTION CHART
# =====================================================

plt.figure(figsize=(18, 6))

label_dist.plot(kind="bar")

plt.title("Dataset Validation - Class Distribution")
plt.xlabel("Label")
plt.ylabel("Video Count")

plt.tight_layout()

plt.savefig(
    os.path.join(
        FIGURE_DIR,
        "validation_class_distribution.png"
    )
)

plt.close()

# =====================================================
# SAVE REPORT TXT
# =====================================================

report_path = os.path.join(
    REPORT_DIR,
    "dataset_validation_report.txt"
)

with open(
    report_path,
    "w",
    encoding="utf-8"
) as f:

    f.write(
        "DATASET VALIDATION REPORT\n"
    )

    f.write("=" * 60 + "\n\n")

    f.write(
        f"Total Labels : {total_labels}\n"
    )

    f.write(
        f"Total Videos : {total_videos}\n\n"
    )

    f.write(
        "CLASS STATISTICS\n"
    )

    f.write("-" * 30 + "\n")

    f.write(
        f"Min Samples/Class : {min_class}\n"
    )

    f.write(
        f"Max Samples/Class : {max_class}\n"
    )

    f.write(
        f"Mean Samples/Class : {mean_class:.2f}\n"
    )

    f.write(
        f"Median Samples/Class : {median_class:.2f}\n"
    )

    f.write(
        f"Imbalance Ratio : {imbalance_ratio:.2f}\n\n"
    )

    f.write(
        "VIDEO STATISTICS\n"
    )

    f.write("-" * 30 + "\n")

    f.write(
        f"Average Duration : {avg_duration:.2f} sec\n"
    )

    f.write(
        f"Minimum Duration : {min_duration:.2f} sec\n"
    )

    f.write(
        f"Maximum Duration : {max_duration:.2f} sec\n\n"
    )

    f.write(
        f"Average FPS : {avg_fps:.2f}\n"
    )

    f.write(
        f"Average Frames : {avg_frames:.2f}\n\n"
    )

    f.write(
        "UNIQUE RESOLUTIONS\n"
    )

    f.write("-" * 30 + "\n")

    f.write(
        resolutions.to_string(index=False)
    )

    f.write("\n\n")

    f.write(
        "VALIDATION ISSUES\n"
    )

    f.write("-" * 30 + "\n")

    if len(issues) == 0:

        f.write(
            "No issues detected.\n"
        )

    else:

        for issue in issues:
            f.write(
                f"- {issue}\n"
            )

    f.write("\n")

    f.write(
        f"DATASET STATUS : "
        f"{'VALID' if dataset_valid else 'NOT VALID'}\n"
    )

# =====================================================
# PRINT
# =====================================================

print("\n")
print("=" * 60)
print("VALIDATION FINISHED")
print("=" * 60)

print(f"Total Labels : {total_labels}")
print(f"Total Videos : {total_videos}")

print(f"Min/Class : {min_class}")
print(f"Max/Class : {max_class}")

print(f"Imbalance Ratio : {imbalance_ratio:.2f}")

print(
    f"Dataset Status : "
    f"{'VALID' if dataset_valid else 'NOT VALID'}"
)

print("\nReport saved:")
print(report_path)