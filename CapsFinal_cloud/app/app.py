import streamlit as st
import numpy as np
import pandas as pd
import pickle
import plotly.express as px
import plotly.graph_objects as go

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="SignBank AI - EDA Dashboard",
    layout="wide"
)

# =====================================================
# LOAD DATA
# =====================================================

@st.cache_data
def load_dataset():

    X_train = np.load("dataset_final/X_train.npy")
    X_val = np.load("dataset_final/X_val.npy")
    X_test = np.load("dataset_final/X_test.npy")

    y_train = np.load("dataset_final/y_train.npy")
    y_val = np.load("dataset_final/y_val.npy")
    y_test = np.load("dataset_final/y_test.npy")

    with open(
        "dataset_final/label_encoder.pkl",
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

# =====================================================
# HEADER
# =====================================================

st.title("🤟 SignBank AI")
st.subheader(
    "Exploratory Data Analysis Dashboard"
)

# =====================================================
# DATASET OVERVIEW
# =====================================================

st.header("Dataset Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Classes",
    len(encoder.classes_)
)

col2.metric(
    "Train Samples",
    len(X_train)
)

col3.metric(
    "Validation Samples",
    len(X_val)
)

col4.metric(
    "Test Samples",
    len(X_test)
)

st.write("---")

# =====================================================
# INPUT SHAPE
# =====================================================

st.header("Input Shape")

shape_df = pd.DataFrame({
    "Property": [
        "Sequence Length",
        "Feature Count"
    ],
    "Value": [
        X_train.shape[1],
        X_train.shape[2]
    ]
})

st.dataframe(
    shape_df,
    use_container_width=True
)

# =====================================================
# DATASET SPLIT
# =====================================================

st.header("Dataset Split")

split_df = pd.DataFrame({
    "Dataset": [
        "Train",
        "Validation",
        "Test"
    ],
    "Samples": [
        len(X_train),
        len(X_val),
        len(X_test)
    ]
})

fig_split = px.pie(
    split_df,
    names="Dataset",
    values="Samples",
    title="Dataset Split Distribution"
)

st.plotly_chart(
    fig_split,
    use_container_width=True
)

# =====================================================
# CLASS DISTRIBUTION
# =====================================================

st.header("Class Distribution")

all_labels = np.concatenate([
    y_train,
    y_val,
    y_test
])

label_counts = pd.Series(
    all_labels
).value_counts().sort_index()

class_names = encoder.inverse_transform(
    label_counts.index
)

dist_df = pd.DataFrame({
    "Label": class_names,
    "Count": label_counts.values
})

fig_class = px.bar(
    dist_df,
    x="Label",
    y="Count",
    title="Sample Distribution per Class"
)

st.plotly_chart(
    fig_class,
    use_container_width=True
)

# =====================================================
# FEATURE DISTRIBUTION
# =====================================================

st.header("Feature Distribution")

sample_feature = X_train.reshape(
    -1,
    X_train.shape[-1]
)

feature_index = st.slider(
    "Select Feature Index",
    0,
    140,
    0
)

fig_feature = px.histogram(
    sample_feature[:, feature_index],
    nbins=50,
    title=f"Feature Distribution #{feature_index}"
)

st.plotly_chart(
    fig_feature,
    use_container_width=True
)

# =====================================================
# ANGLE FEATURES
# =====================================================

st.header("Angle Feature Analysis")

angle_idx = st.selectbox(
    "Select Angle Feature",
    list(range(126,141))
)

fig_angle = px.histogram(
    sample_feature[:, angle_idx],
    nbins=50,
    title=f"Angle Feature #{angle_idx}"
)

st.plotly_chart(
    fig_angle,
    use_container_width=True
)

# =====================================================
# SAMPLE SEQUENCE
# =====================================================

st.header("Sample Sequence Visualization")

sample_idx = st.slider(
    "Select Sample",
    0,
    len(X_train)-1,
    0
)

feature_seq = st.slider(
    "Select Feature",
    0,
    140,
    0,
    key="sequence_feature"
)

seq_df = pd.DataFrame({
    "Frame": np.arange(
        X_train.shape[1]
    ),
    "Value": X_train[
        sample_idx,
        :,
        feature_seq
    ]
})

fig_seq = px.line(
    seq_df,
    x="Frame",
    y="Value",
    title=f"Feature {feature_seq} Across Sequence"
)

st.plotly_chart(
    fig_seq,
    use_container_width=True
)

# =====================================================
# BUSINESS QUESTIONS
# =====================================================

st.header("Business Questions")

st.markdown("""
### 1. Seberapa akurat SignBank AI dalam menerjemahkan bahasa isyarat perbankan menjadi teks secara real-time?

Analisis dataset dilakukan untuk memastikan data siap digunakan pada proses pelatihan model.

---

### 2. Bagaimana performa SignBank AI dalam mendukung komunikasi antara nasabah Tuli dan petugas bank berdasarkan hasil pengujian model?

Performa model akan dievaluasi menggunakan Accuracy, Precision, Recall, F1-Score, dan Confusion Matrix.
""")

# =====================================================
# DATA SAMPLE
# =====================================================

st.header("Dataset Sample")

st.write(
    "Shape:",
    X_train[sample_idx].shape
)

st.dataframe(
    pd.DataFrame(
        X_train[sample_idx]
    ).head(10),
    use_container_width=True
)