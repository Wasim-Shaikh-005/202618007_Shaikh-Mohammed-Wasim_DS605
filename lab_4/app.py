import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pathlib import Path

st.set_page_config(page_title="Airbnb Price Predictor", page_icon="🏠")

@st.cache_resource
def load_model():
    model_path = Path(__file__).parent / "airbnb_price_pipeline.joblib"
    return joblib.load(model_path)
model = load_model()
st.title("🏠 Airbnb Nightly Price Predictor")
st.write("Enter listing details to estimate the nightly Airbnb price.")

groups=["Bronx","Brooklyn","Manhattan","Queens","Staten Island"]
rooms=["Entire home/apt","Private room","Shared room"]

with st.form("prediction"):
    c1,c2=st.columns(2)
    with c1:
        neighbourhood_group=st.selectbox("Neighbourhood group",groups,index=2)
        neighbourhood=st.text_input("Neighbourhood",value="Midtown")
        room_type=st.selectbox("Room type",rooms)
        latitude=st.number_input("Latitude",value=40.7549,format="%.6f")
        longitude=st.number_input("Longitude",value=-73.9840,format="%.6f")
        minimum_nights=st.number_input("Minimum nights",1,365,3)
    with c2:
        number_of_reviews=st.number_input("Number of reviews",0,1000,20)
        reviews_per_month=st.number_input("Reviews per month",0.0,100.0,1.5)
        calculated_host_listings_count=st.number_input("Host's total listings",1,500,1)
        availability_365=st.slider("Availability in next 365 days",0,365,180)
        has_review=st.checkbox("Listing has review history",True)
    submit=st.form_submit_button("Predict nightly price")

if submit:
    row=pd.DataFrame([{
        "neighbourhood_group":neighbourhood_group,"neighbourhood":neighbourhood,
        "latitude":latitude,"longitude":longitude,"room_type":room_type,
        "minimum_nights":minimum_nights,"number_of_reviews":number_of_reviews,
        "reviews_per_month":reviews_per_month if has_review else np.nan,
        "calculated_host_listings_count":calculated_host_listings_count,
        "availability_365":availability_365,"has_review":int(has_review)
    }])
    price=float(np.maximum(np.expm1(model.predict(row))[0],0))
    st.success(f"Estimated nightly price: **${price:,.0f}**")
