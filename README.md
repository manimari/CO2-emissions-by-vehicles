# CO2 emissions by vehicles

This repository contains the code for our project **CO2 emissions by vehicles**, developed during our [Data Scientist training](https://datascientest.com/en/data-scientist-course) at [DataScientest](https://datascientest.com/).

The goal of this project is to **to identify the technical characteristics that play a role in pollution** and **compare different standards for emissions**. 

This project was developed by the following team :

- Rauf Isgandarov  ([GitHub](https://github.com/risgandar) / [LinkedIn](https://www.linkedin.com/in/rauf-isgandarov-56365a195/))
- Marianthi Maniou ([GitHub](https://github.com/manimari) / [LinkedIn](https://www.linkedin.com/in/marianthi-maniou/))
- Oleh Polupan ([GitHub](https://github.com/oleh-polupan) / [LinkedIn](https://www.linkedin.com/in/oleh-polupan-55946656/))

## Application Streamlit

For the presentation of the project [Streamlit](https://streamlit.io/) was used. You can browse and run the [notebooks](./notebooks). You will need to install the dependencies (in a dedicated environment):
To run the app (as example):
```shell
cd notebooks
conda create --name my-awesome-streamlit python=3.9
conda activate my-awesome-streamlit
pip install -r requirements.txt
streamlit run "JAN23_BDS_INT_CO2 Emissions.py"
```

## Data description
In this data set, you will find all the technical characteristics of vehicles marketed in France in 2013, as well as fuel consumption, CO2 emissions and pollutant emissions into the air.
CO2 and pollutant emissions of vehicles marketed in France - data.gouv.fr
https://www.data.gouv.fr/fr/datasets/emissions-de-co2-et-de-polluants-des-vehicules-commercialises-en-france/#_

In this one: the CO2 emissions of all the cars that come out each year (several hundred thousand vehicles per year, the dataset for new cars from 2019 alone weighs more than 1gb) with a little more info than that govt data
https://www.eea.europa.eu/data-and-maps/data/co2-cars-emission-20 

Identifying the vehicles that emit the most CO2 is important to identify the technical characteristics that play a role in pollution. Predicting this pollution in advance makes it possible to prevent the appearance of new types of vehicles (new series of cars for example).
