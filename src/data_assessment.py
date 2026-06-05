# ============================================
# Hasil dari assessment disimpan di reports/asessment_report
# ============================================

import os
import cv2
import pandas as pd
import matplotlib.pyplot as plt

# =====================================================
# CONFIG
# =====================================================

DATASET_DIR = "dataset"

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
corrupted_files = []

print("=" * 60)
print("ASSESSING DATASET")
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

    print(f"Processing Label: {label}")

    for filename in video_files:

        filepath = os.path.join(root, filename)

        try:

            file_size = os.path.getsize(filepath)

            if file_size == 0:

                corrupted_files.append({
                    "label": label,
                    "file": filename,
                    "reason": "empty_file"
                })

                continue

            cap = cv2.VideoCapture(filepath)

            if not cap.isOpened():

                corrupted_files.append({
                    "label": label,
                    "file": filename,
                    "reason": "cannot_open"
                })

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
                "height": height,
                "file_size_mb": round(
                    file_size / (1024 * 1024),
                    3
                )
            })

            cap.release()

        except Exception as e:

            corrupted_files.append({
                "label": label,
                "file": filename,
                "reason": str(e)
            })

# =====================================================
# DATAFRAME
# =====================================================

df = pd.DataFrame(records)

if df.empty:
    print("\nERROR: No video files found.")
    print("Check dataset structure.")
    exit()

print("\n")
print("=" * 60)
print("SUMMARY")
print("=" * 60)

print(f"Total Valid Videos : {len(df)}")
print(f"Total Bad Videos   : {len(corrupted_files)}")

# =====================================================
# SAVE RAW SUMMARY
# =====================================================

df.to_csv(
    os.path.join(
        REPORT_DIR,
        "dataset_summary.csv"
    ),
    index=False
)

# =====================================================
# SAVE CORRUPTED FILES
# =====================================================

pd.DataFrame(
    corrupted_files
).to_csv(
    os.path.join(
        REPORT_DIR,
        "corrupted_files.csv"
    ),
    index=False
)

# =====================================================
# LABEL DISTRIBUTION
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
        "label_distribution.csv"
    ),
    index=False
)

# =====================================================
# DATASET STATISTICS
# =====================================================

total_labels = df["label"].nunique()

avg_duration = df["duration_sec"].mean()
min_duration = df["duration_sec"].min()
max_duration = df["duration_sec"].max()

avg_fps = df["fps"].mean()

avg_frames = df["frame_count"].mean()

avg_width = df["width"].mean()
avg_height = df["height"].mean()

# =====================================================
# CLASS DISTRIBUTION
# =====================================================

plt.figure(figsize=(18, 6))

label_dist.plot(kind="bar")

plt.title("Class Distribution")
plt.xlabel("Label")
plt.ylabel("Number of Videos")

plt.tight_layout()

plt.savefig(
    os.path.join(
        FIGURE_DIR,
        "class_distribution.png"
    )
)

plt.close()

# =====================================================
# DURATION DISTRIBUTION
# =====================================================

plt.figure(figsize=(8, 5))

plt.hist(
    df["duration_sec"],
    bins=20
)

plt.title(
    "Video Duration Distribution"
)

plt.xlabel(
    "Duration (seconds)"
)

plt.ylabel(
    "Count"
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        FIGURE_DIR,
        "duration_distribution.png"
    )
)

plt.close()

# =====================================================
# FPS DISTRIBUTION
# =====================================================

plt.figure(figsize=(8, 5))

plt.hist(
    df["fps"],
    bins=20
)

plt.title(
    "FPS Distribution"
)

plt.xlabel("FPS")
plt.ylabel("Count")

plt.tight_layout()

plt.savefig(
    os.path.join(
        FIGURE_DIR,
        "fps_distribution.png"
    )
)

plt.close()

# =====================================================
# FRAME DISTRIBUTION
# =====================================================

plt.figure(figsize=(8, 5))

plt.hist(
    df["frame_count"],
    bins=20
)

plt.title(
    "Frame Count Distribution"
)

plt.xlabel("Frames")
plt.ylabel("Count")

plt.tight_layout()

plt.savefig(
    os.path.join(
        FIGURE_DIR,
        "frame_distribution.png"
    )
)

plt.close()

# =====================================================
# OUTLIER CHECK
# =====================================================

short_videos = df[
    df["duration_sec"] < 2
]

long_videos = df[
    df["duration_sec"] > 5
]

short_videos.to_csv(
    os.path.join(
        REPORT_DIR,
        "videos_under_2s.csv"
    ),
    index=False
)

long_videos.to_csv(
    os.path.join(
        REPORT_DIR,
        "videos_over_5s.csv"
    ),
    index=False
)

# =====================================================
# REPORT TXT
# =====================================================

report_path = os.path.join(
    REPORT_DIR,
    "assessment_report.txt"
)

with open(
    report_path,
    "w",
    encoding="utf-8"
) as f:

    f.write(
        "DATASET ASSESSMENT REPORT\n"
    )

    f.write("=" * 60)
    f.write("\n\n")

    f.write(
        f"Total Labels : {total_labels}\n"
    )

    f.write(
        f"Total Videos : {len(df)}\n"
    )

    f.write(
        f"Corrupted Videos : {len(corrupted_files)}\n\n"
    )

    f.write(
        "VIDEO STATISTICS\n"
    )

    f.write(
        "-" * 30 + "\n"
    )

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
        f"Average Resolution : "
        f"{avg_width:.0f}x{avg_height:.0f}\n\n"
    )

    f.write(
        f"Videos < 2 sec : {len(short_videos)}\n"
    )

    f.write(
        f"Videos > 5 sec : {len(long_videos)}\n\n"
    )

    f.write(
        "LABEL DISTRIBUTION\n"
    )

    f.write(
        "-" * 30 + "\n"
    )

    f.write(
        label_dist.to_string()
    )

print("\nAssessment Completed")
print(f"Report saved : {REPORT_DIR}")