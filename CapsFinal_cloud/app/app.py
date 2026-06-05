import os
import numpy as np
import streamlit as st

# =====================================================
# PATH
# =====================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DATASET_DIR = os.path.join(
    BASE_DIR,
    "dataset_final"
)

# =====================================================
# LOAD DATA
# =====================================================

@st.cache_data
def load_dataset():

    X_train = np.load(
        os.path.join(
            DATASET_DIR,
            "X_train.npy"
        )
    )

    X_val = np.load(
        os.path.join(
            DATASET_DIR,
            "X_val.npy"
        )
    )

    X_test = np.load(
        os.path.join(
            DATASET_DIR,
            "X_test.npy"
        )
    )

    y_train = np.load(
        os.path.join(
            DATASET_DIR,
            "y_train.npy"
        )
    )

    y_val = np.load(
        os.path.join(
            DATASET_DIR,
            "y_val.npy"
        )
    )

    y_test = np.load(
        os.path.join(
            DATASET_DIR,
            "y_test.npy"
        )
    )

    class_names = np.load(
        os.path.join(
            DATASET_DIR,
            "classes.npy"
        ),
        allow_pickle=True
    )

    return (
        X_train,
        X_val,
        X_test,
        y_train,
        y_val,
        y_test,
        class_names
    )

(
    X_train,
    X_val,
    X_test,
    y_train,
    y_val,
    y_test,
    class_names
) = load_dataset()
