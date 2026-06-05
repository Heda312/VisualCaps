import os
import cv2
import numpy as np
import mediapipe as mp
from multiprocessing import Pool, cpu_count
from tqdm import tqdm

# =====================================================
# CONFIG
# =====================================================

INPUT_DIR = "dataset_clean"
OUTPUT_DIR = "dataset_landmarks"

SEQUENCE_LENGTH = 40

os.makedirs(OUTPUT_DIR, exist_ok=True)

# =====================================================
# MEDIAPIPE
# =====================================================

mp_hands = mp.solutions.hands

# =====================================================
# ANGLE TRIPLETS
# =====================================================

ANGLE_TRIPLETS = [
    (1, 2, 3),
    (2, 3, 4),

    (5, 6, 7),
    (6, 7, 8),

    (9, 10, 11),
    (10, 11, 12),

    (13, 14, 15),
    (14, 15, 16),

    (17, 18, 19),
    (18, 19, 20),

    (0, 5, 6),
    (0, 9, 10),
    (0, 13, 14),
    (0, 17, 18),

    (5, 9, 13)
]

# =====================================================
# ANGLE
# =====================================================

def calculate_angle(a, b, c):

    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    ba = a - b
    bc = c - b

    cosine = np.dot(
        ba, bc
    ) / (
        np.linalg.norm(ba)
        * np.linalg.norm(bc)
        + 1e-6
    )

    cosine = np.clip(
        cosine,
        -1.0,
        1.0
    )

    angle = np.degrees(
        np.arccos(cosine)
    )

    return angle / 180.0


# =====================================================
# FRAME FEATURE
# =====================================================

def extract_features(frame, hands):

    frame_rgb = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    result = hands.process(frame_rgb)

    left_hand = np.zeros((21, 3))
    right_hand = np.zeros((21, 3))

    if result.multi_hand_landmarks:

        for hand_landmarks, handedness in zip(
            result.multi_hand_landmarks,
            result.multi_handedness
        ):

            coords = np.array([
                [lm.x, lm.y, lm.z]
                for lm in hand_landmarks.landmark
            ])

            hand_type = (
                handedness
                .classification[0]
                .label
            )

            if hand_type == "Left":
                left_hand = coords
            else:
                right_hand = coords

    coord_features = np.concatenate([
        left_hand.flatten(),
        right_hand.flatten()
    ])

    hand_for_angle = right_hand

    if np.sum(right_hand) == 0:
        hand_for_angle = left_hand

    angles = []

    for a, b, c in ANGLE_TRIPLETS:

        angles.append(
            calculate_angle(
                hand_for_angle[a],
                hand_for_angle[b],
                hand_for_angle[c]
            )
        )

    angles = np.array(
        angles,
        dtype=np.float32
    )

    features = np.concatenate([
        coord_features,
        angles
    ])

    return features.astype(np.float32)


# =====================================================
# RESAMPLE TO 40 FRAMES
# =====================================================

def resample_sequence(sequence):

    if len(sequence) == 0:

        return np.zeros(
            (SEQUENCE_LENGTH, 141),
            dtype=np.float32
        )

    sequence = np.array(
        sequence,
        dtype=np.float32
    )

    idx = np.linspace(
        0,
        len(sequence) - 1,
        SEQUENCE_LENGTH
    ).astype(int)

    return sequence[idx]


# =====================================================
# VIDEO PROCESSING
# =====================================================

def process_video(video_path):

    hands = mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=2,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    )

    cap = cv2.VideoCapture(video_path)

    sequence = []

    while cap.isOpened():

        ret, frame = cap.read()

        if not ret:
            break

        sequence.append(
            extract_features(
                frame,
                hands
            )
        )

    cap.release()
    hands.close()

    return resample_sequence(sequence)


# =====================================================
# MULTIPROCESS WORKER
# =====================================================

def process_single_video(args):

    video_path, save_path = args

    try:

        sequence = process_video(
            video_path
        )

        np.save(
            save_path,
            sequence
        )

        return True

    except Exception as e:

        print(f"\nERROR: {video_path}")
        print(e)

        return False
    
    # =====================================================
# MAIN
# =====================================================

if __name__ == "__main__":

    tasks = []

    print("=" * 60)
    print("LANDMARK EXTRACTION")
    print("=" * 60)

    for root, dirs, files in os.walk(INPUT_DIR):

        videos = [
            f for f in files
            if f.lower().endswith(".mp4")
        ]

        if len(videos) == 0:
            continue

        label = os.path.basename(root)

        save_dir = os.path.join(
            OUTPUT_DIR,
            label
        )

        os.makedirs(
            save_dir,
            exist_ok=True
        )

        print(
            f"{label}: {len(videos)} videos"
        )

        for video in videos:

            video_path = os.path.join(
                root,
                video
            )

            save_path = os.path.join(
                save_dir,
                video.replace(
                    ".mp4",
                    ".npy"
                )
            )

            tasks.append(
                (
                    video_path,
                    save_path
                )
            )

    print("\n")
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)

    print(
        f"Total Videos : {len(tasks)}"
    )

    NUM_WORKERS = cpu_count()

    print(
        f"CPU Cores Used : {NUM_WORKERS}"
    )

    print("\nStarting extraction...\n")

    with Pool(
        processes=NUM_WORKERS
    ) as pool:

        results = list(
            tqdm(
                pool.imap(
                    process_single_video,
                    tasks
                ),
                total=len(tasks)
            )
        )

    success = sum(results)
    failed = len(tasks) - success

    print("\n")
    print("=" * 60)
    print("EXTRACTION FINISHED")
    print("=" * 60)

    print(
        f"Success Files : {success}"
    )

    print(
        f"Failed Files  : {failed}"
    )

    print("\nOutput:")
    print(OUTPUT_DIR)

    print("\nFeature Shape:")
    print(f"({SEQUENCE_LENGTH}, 141)")
    print("126 Landmark + 15 Angle")