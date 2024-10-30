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
st.title("Report 2: modeling")
st.markdown("---")

# %% [markdown]
# Stages of the project
# Classification of the problem
# What kind of machine learning problem is your project like? (classification, regression, clustering, etc)
# What task does your project relate to? (fraud detection, facial recognition, sentiment analysis, etc)?
# What is the main performance metric used to compare your models? Why this one?
# Did you use other qualitative or quantitative performance metrics? If yes, detail it.
# Model choice and optimization
# What algorithms have you tried?
# Describe which one(s) you selected and why?
# Did you use parameter optimization techniques such as Grid Search and Cross Validation?
# Have you tested advanced models? Bagging, Boosting, Deep Learning… Why?
# Interpretation of results
# Have you analyzed the errors in your model?
# Did this contribute to his improvement? If yes, describe.
# Have you used interpretability techniques such as SHAP, LIME, Skater… (Grad-CAM for Deep Learning…)
# What has (or not) generated a significant improvement in your performance?
#
#
# Assessment methods:
# Professional scenario: based on a proposed solution, the candidate will have to produce a summary report including: the explanation of the choices of AI solutions implemented, the interpretation of the results, the evaluation of the reliability of the algorithms and an optimization proposal.
#

# %%
#jupytext --set-formats ipynb,py:percent "/Users/olehpolupan/DataspellProjects/JAN23_BDS_INT-Rakuten/notebooks/pages/2-Report2.ipynb"

#jupytext --sync "/Users/olehpolupan/DataspellProjects/JAN23_BDS_INT-Rakuten/notebooks/pages/2-Report2.ipynb"

#streamlit run "/Users/olehpolupan/DataspellProjects/JAN23_BDS_INT-Rakuten/notebooks/JAN23_BDS_INT_CO2 Emissions.py"
