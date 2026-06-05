import os
import pickle
import numpy as np
import streamlit as st

# =====================================================
# PATH CONFIG
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

st.write("BASE_DIR:", BASE_DIR)
st.write("DATASET_DIR:", DATASET_DIR)

if os.path.exists(DATASET_DIR):
    st.success("dataset_final ditemukan")
    st.write(os.listdir(DATASET_DIR))
else:
    st.error("dataset_final tidak ditemukan")

# =====================================================
# LOAD DATASET
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

    with open(
        os.path.join(
            DATASET_DIR,
            "label_encoder.pkl"
        ),
        "rb"
    ) as f:

        encoder = pickle.load(f)

    return (
        X_train,
        X_val,
        X_test,
        y_train,
        y_val,
        y_test,
        encoder
    )

(
    X_train,
    X_val,
    X_test,
    y_train,
    y_val,
    y_test,
    encoder
) = load_dataset()
