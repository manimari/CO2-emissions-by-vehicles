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

# %%

import config

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


# %%
st.title("Exploration, data visualization and data pre-processing")
st.markdown("---")

# %%
st.markdown("The New European Driving Cycle (NEDC) was a driving cycle, last updated in 1997, designed to assess the emission levels of car engines and fuel economy in passenger cars (which excludes light trucks and commercial vehicles). It is also referred to as MVEG cycle (Motor Vehicle Emissions Group).")

with st.expander("More details about NEDC"):
   st.markdown("The NEDC was conceived when European vehicles were lighter and less powerful. The test offers a stylized driving speed pattern with low accelerations, constant speed cruises, and many idling events. However, accelerations are much steeper and variable in practice, which is in part caused by the power surplus of modern engines as the 0–100 km/h (0–62 mph) average-time decreased from 14 seconds in 1981 to 9 seconds in 2007. In 1998, a Swedish researcher criticized the NEDC standard for allowing large emission differences between test and reality.")

   st.markdown("The WLTP replaces the European NEDC based procedure for type approval testing of light-duty vehicles, with the transition from NEDC to WLTP occurring over 2017-2019. The WLTP is also introduced for vehicle certification in Japan.")

   st.markdown("[Wikipedia: New European Driving Cycle](https://en.wikipedia.org/wiki/New_European_Driving_Cycle)")

st.markdown("The Worldwide harmonized Light vehicles Test Procedure (WLTP) is a global standard for determining the levels of pollutants, CO2 emissions and fuel consumption of traditional and hybrid cars, as well as the range of fully electric vehicles.")

with st.expander("More details about WLTP"):
   st.markdown("The new standard has been designed to be more representative of real and modern driving conditions. To pursue this goal, the WLTP is 10 minutes longer than the NEDC (30 instead of 20 minutes), its velocity profile is more dynamic, consisting of quicker accelerations followed by short brakes. Moreover, the average and the maximum velocities have been increased to 46.5 km/h and 131.3 km/h respectively. The distance covered is 23.25 km (more than double the 11 kilometers of the NEDC).")

st.markdown(
   """
   The key differences between the old NEDC and new WLTP test are that WLTP:
   - has higher average and maximum speeds
   - includes a wider range of driving conditions (urban, suburban, main road, highway)
   - simulates a longer distance
   - has higher average and maximum drive power
   - looks at steeper accelerations and decelerations
   - tests optional equipment separately
   """
)

st.markdown("[Wikipedia: Worldwide Harmonised Light Vehicles Test Procedure](https://en.wikipedia.org/wiki/Worldwide_Harmonised_Light_Vehicles_Test_Procedure)")

st.markdown("So, we have two datasets with old and new types of approval")

tab1, tab2 = st.tabs(["NEDC (France)", "WLTP (EU)"])

with tab1:
   st.header("NEDC (France)")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("WLTP (EU)")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)


# %% [markdown]
# Introduction to the project
# Context
# Context of the project's integration into your business.
# From a technical point of view.
# From an economic point of view.
# From a scientific point of view.
#
# Objectives
# What are the main objectives to be achieved? Describe in a few lines.
# For each member of the group, specify the level of expertise around the problem addressed?
# Have you contacted business experts to refine the problem and the underlying models? If yes, detail the contribution of these interactions.
# (Are you aware of a similar project within your company, or in your entourage? What is its progress? How has it helped you in the realization of your project? How does your project contribute to improving it?).
#
#
#
# Understanding and manipulation of data
# Framework
# Which set(s) of data(s) did you use to achieve the objectives of your project?
# Are these data freely available? If not, who owns the data?
# Describe the volume of your dataset?
# Relevance
# Which variables seem most relevant to you with regard to your objectives?
# What is the target variable?
# What features of your dataset can you highlight?
# Are you limited by some of your data?
# Pre-processing and feature engineering
# Did you have to clean and process the data? If yes, describe your treatment process.
# Did you have to carry out normalization/standardization type transformations of your data? If yes, why?
# Are you considering dimension reduction techniques in the modeling part? If yes, why?
# Visualizations and Statistics
# Have you identified relationships between different variables? Between explanatory variables? and between your explanatory variables and the target(s)?
# Describe the distribution of these data, distribution, outliers.. (pre/post processing if necessary)
# Present the statistical analyzes used to confirm the information present on the graphs.
# Draw conclusions from the elements noted above allowing them to project themselves into the modeling part
#
#
# Assessment methods:
# Reconstituted professional situation: from a set of company data, the candidate must implement various pre-processing and data augmentation to make them usable through machine learning techniques.
#

# %%
#jupytext --set-formats ipynb,py:percent "/Users/olehpolupan/DataspellProjects/JAN23_BDS_INT-Rakuten/notebooks/pages/1-Report1.ipynb"

#jupytext --sync "/Users/olehpolupan/DataspellProjects/JAN23_BDS_INT-Rakuten/notebooks/pages/1-Report1.ipynb"

#streamlit run "/Users/olehpolupan/DataspellProjects/JAN23_BDS_INT-Rakuten/notebooks/JAN23_BDS_INT_CO2 Emissions.py"
