import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    st.title("this is my first ecom app")
    st.sidebar.title("Upload file for analysis")

    uploaded_file = st.sidebar.file_uploader("Choose a file", type=["csv", "xlsx"])
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith("csv"):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            
            st.sidebar.success("File uploaded successfully!")
            
            st.subheader("I am showing you a table format of your file")
            st.dataframe(df.head())

            st.subheader("I am showing you a chart format of your file")
            st.write("shape of the data:", df.shape)
            st.write("columns of the data:", df.columns)
            st.write("missing values in the data:", df.isnull().sum())
            
            st.subheader("Data Visualization")
            st.write("Discriptive statistics of the data:", df.describe())
        except Exception as e:
            st.sidebar.error(f"Error reading file: {e}")
            return
        


if __name__ == "__main__":
    main()

    
