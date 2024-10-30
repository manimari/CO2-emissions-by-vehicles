# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.5
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
import streamlit as st

import config

# %%
st.set_page_config(
    page_title=config.TITLE,
    page_icon="https://datascientest.com/wp-content/uploads/2020/03/cropped-favicon-datascientest-1-32x32.png",
)

st.sidebar.image(
    "https://i0.wp.com/datascientest.com/wp-content/uploads/2022/03/logo-2021.png?w=429&ssl=1",
    width=200,
)
#st.sidebar.markdown("---")
st.sidebar.markdown(f"## {config.PROMOTION}")

st.sidebar.markdown("### Team members:")
for member in config.TEAM_MEMBERS:
    st.sidebar.markdown(member.sidebar_markdown(), unsafe_allow_html=True)



#st.image("https://i0.wp.com/datascientest.com/wp-content/uploads/2022/03/logo-2021.png?w=429&ssl=1")

st.image("https://www.allianz-autowelt.de/sites/default/files/styles/detail_page_image_large/public/2019-03/tuev-abgasuntersuchung-abgase.jpg?itok=Nc6fgXrJ")

st.title("CO2 emissions by vehicles")

st.markdown("---")

st.subheader("Description of the project:")

st.markdown("Identifying the vehicles that emit the most CO2 is important to identify the technical characteristics that play a role in pollution. Predicting this pollution in advance makes it possible to prevent the appearance of new types of vehicles (new series of cars for example).")

st.subheader("Data:")

st.markdown("In this data set, you will find all the technical characteristics of vehicles marketed in France in 2013, as well as fuel consumption, CO2 emissions and pollutant emissions into the air.")
st.markdown("https://www.data.gouv.fr/fr/datasets/emissions-de-co2-et-de-polluants-des-vehicules-commercialises-en-france/#_")

st.markdown("CO2 and pollutant emissions of vehicles marketed in France - data.gouv.fr In this one: the CO2 emissions of all the cars that come out each year (several hundred thousand vehicles per year, the dataset for new cars from 2019 alone weighs more than 1gb) with a little more info than that govt data")
st.markdown("https://www.eea.europa.eu/data-and-maps/data/co2-cars-emission-20")


#st.subheader("Project team:")
#col1, col2, col3 = st.columns(3)

#with col1:
#    st.image("https://media.licdn.com/dms/image/C4D03AQGABHxqE2Ct8A/profile-displayphoto-shrink_800_800/0/1612613299861?e=1684972800&v=beta&t=OwCvG0fl23Rqn8bjZ_HeXJ4nyQwnW3td0aNJ27Q175Q")
#    st.subheader("Rauf Isgandarov")
#    st.markdown("Finance | Fintech | Business Intelligence | Big Data")
#    st.markdown("[GitHub](https://github.com/risgandar) / [LinkedIn](https://linkedin.com/in/rauf-isgandarov-56365a195)")

#with col2:
#    st.image("https://media.licdn.com/dms/image/C4E03AQEepZrEwr5MZg/profile-displayphoto-shrink_800_800/0/1653754732831?e=1684972800&v=beta&t=4tGLYdHr_Mpae0LF1NVP_pqmCP4lQuYzsklU83we9Ac")
#    st.subheader("Marianthi Maniou")
#    st.markdown("Data Scientist & Online Math Tutor")
#    st.markdown("[GitHub](https://github.com/manimari) / [LinkedIn](https://www.linkedin.com/in/marianthi-maniou/)")

#with col3:
#    st.image("https://media.licdn.com/dms/image/C4E03AQFkte7fb2a1qw/profile-displayphoto-shrink_400_400/0/1667917848753?e=1684972800&v=beta&t=AMONIJq33uzWmg082S0Mspu9j21uJvSBQYFh19rnSzI")
 #   st.subheader("Oleh Polupan")
 #   st.markdown("Data Scientist / Reporting Analyst")
 #   st.markdown("[GitHub](https://github.com/oleh-polupan) / [LinkedIn](https://www.linkedin.com/in/oleh-polupan-55946656/)")



# %%
#jupytext --set-formats ipynb,py:percent "/Users/olehpolupan/DataspellProjects/JAN23_BDS_INT-Rakuten/notebooks/JAN23_BDS_INT_CO2 Emissions.ipynb"

#jupytext --sync "/Users/olehpolupan/DataspellProjects/JAN23_BDS_INT-Rakuten/notebooks/JAN23_BDS_INT_CO2 Emissions.ipynb"

#streamlit run "/Users/olehpolupan/DataspellProjects/JAN23_BDS_INT-Rakuten/notebooks/JAN23_BDS_INT_CO2 Emissions.py"
