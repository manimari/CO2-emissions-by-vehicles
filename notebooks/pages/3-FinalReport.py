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
st.title("Final report")
st.markdown("---")

# %% [markdown]
# Conclusion drawn
# Difficulties encountered during the project
# What was the main scientific obstacle encountered during this project?
# For each of the following points, if you encountered difficulties, detail how they slowed you down in setting up your project.
# Forecast: tasks that took longer than expected, etc.
# Datasets: acquisition, volumetry, processing, aggregation, etc.
# Technical/theoretical skills: timing of skill acquisition, skill not offered in training, etc.
# Relevance: of the approach, model, data, etc.
# IT: storage power, computational power, etc.
# Other
# Report
# Detail what was your main contribution to achieving the project's goals.
# Have you changed the model since the last iteration? If yes, provide details.
# Present the results obtained and compare them to the benchmark
# For each of the project's goals, detail how they were achieved or not.
# If they have been reached, in which process(es) can your model fit? Detail.
#
# Continuation of the project
#
# What avenues for improvement do you suggest to increase the performance of your model?
# How has your project contributed to an increase in scientific knowledge?
# Bibliography
# What bibliographical elements (research articles, blog, books, etc.) did you rely on to carry out your project?
# Appendices
# Gantt diagram.
# Description of code files.
#

# %%
#jupytext --set-formats ipynb,py:percent "/Users/olehpolupan/DataspellProjects/JAN23_BDS_INT-Rakuten/notebooks/pages/3-FinalReport.ipynb"

#jupytext --sync "/Users/olehpolupan/DataspellProjects/JAN23_BDS_INT-Rakuten/notebooks/pages/3-FinalReport.ipynb"

#streamlit run "/Users/olehpolupan/DataspellProjects/JAN23_BDS_INT-Rakuten/notebooks/JAN23_BDS_INT_CO2 Emissions.py"
