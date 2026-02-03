import streamlit as st
import os
from datetime import datetime

UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

st.title("Smart Learning Support System")

doc_type = st.selectbox("Select document type", ["Syllabus", "PYQ", "Book"])

uploaded = st.file_uploader("Upload PDF / Image", type=["pdf","png","jpg","jpeg"])

if uploaded:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(UPLOAD_DIR, f"{ts}_{doc_type}_{uploaded.name}")
    with open(path, "wb") as f:
        f.write(uploaded.getbuffer())
    st.success("File uploaded successfully!")

st.subheader("Uploaded Files")
for f in os.listdir(UPLOAD_DIR):
    st.write("📄", f)
