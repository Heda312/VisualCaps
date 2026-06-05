import os
import pickle
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# =====================================================
# CONFIG
# =====================================================

INPUT_DIR = "dataset_landmarks"
OUTPUT_DIR = "dataset_final"

TEST_SIZE = 0.10
VAL_SIZE = 0.10

RANDOM_STATE = 42

os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)

# =====================================================
# LOAD DATA
# =====================================================

X = []
y = []

print("=" * 60)
print("LOADING LANDMARK DATASET")
print("=" * 60)

labels_found = []

for label in sorted(os.listdir(INPUT_DIR)):

    label_path = os.path.join(
        INPUT_DIR,
        label
    )

    if not os.path.isdir(label_path):
        continue

    labels_found.append(label)

    files = [
        f for f in os.listdir(label_path)
        if f.endswith(".npy")
    ]

    print(
        f"{label}: {len(files)} samples"
    )

    for file in files:

        file_path = os.path.join(
            label_path,
            file
        )

        data = np.load(
            file_path
        )

        X.append(data)
        y.append(label)

# =====================================================
# TO NUMPY
# =====================================================

X = np.array(
    X,
    dtype=np.float32
)

y = np.array(y)

print("\n")
print("=" * 60)
print("DATASET SUMMARY")
print("=" * 60)

print(f"Total Samples : {len(X)}")
print(f"Total Labels  : {len(np.unique(y))}")

print(f"X Shape       : {X.shape}")

# =====================================================
# LABEL ENCODING
# =====================================================

encoder = LabelEncoder()

y_encoded = encoder.fit_transform(y)

# save encoder

with open(
    os.path.join(
        OUTPUT_DIR,
        "label_encoder.pkl"
    ),
    "wb"
) as f:

    pickle.dump(
        encoder,
        f
    )

# =====================================================
# TRAIN / TEMP
# =====================================================

X_train, X_temp, y_train, y_temp = train_test_split(
    X,
    y_encoded,
    test_size=(TEST_SIZE + VAL_SIZE),
    stratify=y_encoded,
    random_state=RANDOM_STATE
)

# =====================================================
# VAL / TEST
# =====================================================

val_ratio = (
    VAL_SIZE /
    (VAL_SIZE + TEST_SIZE)
)

X_val, X_test, y_val, y_test = train_test_split(
    X_temp,
    y_temp,
    test_size=(1 - val_ratio),
    stratify=y_temp,
    random_state=RANDOM_STATE
)

# =====================================================
# SAVE DATASET
# =====================================================

np.save(
    os.path.join(
        OUTPUT_DIR,
        "X_train.npy"
    ),
    X_train
)

np.save(
    os.path.join(
        OUTPUT_DIR,
        "X_val.npy"
    ),
    X_val
)

np.save(
    os.path.join(
        OUTPUT_DIR,
        "X_test.npy"
    ),
    X_test
)

np.save(
    os.path.join(
        OUTPUT_DIR,
        "y_train.npy"
    ),
    y_train
)

np.save(
    os.path.join(
        OUTPUT_DIR,
        "y_val.npy"
    ),
    y_val
)

np.save(
    os.path.join(
        OUTPUT_DIR,
        "y_test.npy"
    ),
    y_test
)

# =====================================================
# DATASET INFO
# =====================================================

info_path = os.path.join(
    OUTPUT_DIR,
    "dataset_info.txt"
)

with open(
    info_path,
    "w",
    encoding="utf-8"
) as f:

    f.write(
        "DATASET FINAL\n"
    )

    f.write(
        "=" * 50 + "\n\n"
    )

    f.write(
        f"Total Samples : {len(X)}\n"
    )

    f.write(
        f"Total Classes : {len(encoder.classes_)}\n\n"
    )

    f.write(
        f"Train Samples : {len(X_train)}\n"
    )

    f.write(
        f"Validation Samples : {len(X_val)}\n"
    )

    f.write(
        f"Test Samples : {len(X_test)}\n\n"
    )

    f.write(
        f"Input Shape : {X_train.shape[1:]}\n"
    )

    f.write(
        "\nClasses:\n"
    )

    for idx, label in enumerate(
        encoder.classes_
    ):

        f.write(
            f"{idx} -> {label}\n"
        )

# =====================================================
# PRINT RESULT
# =====================================================

print("\n")
print("=" * 60)
print("DATASET PREPARATION FINISHED")
print("=" * 60)

print(
    f"Train : {X_train.shape}"
)

print(
    f"Val   : {X_val.shape}"
)

print(
    f"Test  : {X_test.shape}"
)

print("\nClasses")

for idx, label in enumerate(
    encoder.classes_
):

    print(
        f"{idx:02d} -> {label}"
    )

print("\nOutput:")
print(OUTPUT_DIR)