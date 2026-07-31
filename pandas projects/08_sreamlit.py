# streamlit cannot run jupyter nootebook directly.

# Import
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

# Title and Subheader

st.title("Data Analysis")
st.subheader("Using python & streamlit")

# upload dataset

upload= st.file_uploader("upload your dataset(In csv format)")

if upload is not None:
    data= pd.read_csv(upload)


# show dataset

if upload is not None:
   if st.checkbox("Preview:"):
        if st.button("Head"):
            st.write(data.head())

        if st.button("Tail"):
            st.write(data.tail())



# Check Datatype

if upload is not None:
    if st.checkbox("Data Type"):
        st.text("<dtype>")

        st.write(data.dtypes)

# Find shape of uploaded data shape

if upload is not None:
    if st.checkbox("Which dimension to check?"):
        d_shape= st.radio("",('Row' , 'Columns'))

    if d_shape == 'Row':
       st.text("Number of Rows:")
       st.write(data.shape[0])

    if d_shape == 'Columns':
       st.text("Number of Columns:")
       st.write(data.shape[1])

# Check the null value

if upload is not None:
    test= data.isnull().values.any()

    if st.checkbox("Check NUll Values"):
        if test == True:
            st.text("Missing values")
            fig,ax= plt.subplots()
            sns.heatmap(data.isnull(),ax=ax)
            st.pyplot(fig)

        else:
            st.success("Congratulation!!!No Missing Values.")




# Find Duplicated values in Dataset

if upload is not None:

    test= data.duplicated().any()
    if test == True:
        st.warning("Dataset contains some Duplicates values")

        dup= st.selectbox("Do you want to remove the duplicated values?",
                          ("select one","Yes","NO"))
        
        if dup == "Yes":
            data.drop_duplicates(inplace=True)

            test = data.duplicated().any()

            if not test:
               st.success("Duplicated values are removed successfully!")



        elif dup == "NO":
            st.text("consider removing it ...")

        else:
            st.success("No Duplicated values are found.")


# Get Overall Statistics

if upload is not None:
    if st.checkbox("Statistical info"):
        st.write(data.describe(include="all"))





# About section

if upload is not None:
    if st.button("About App"):
        st.text("Built with Streamlit")
        st.text("Basic Data cleaning")


# By

if upload is not None:
    if st.button("Created By"):
        st.success("Abhiyan Timilsina.")





