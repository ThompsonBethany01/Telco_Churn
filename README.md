# **Predicting Churn at Telco**

## About the Project
### Goals
Churn is defined as the rate at which customers leave a company. This is bad for business, as it often costs more to attract new customers than to keep current customers. The goal of this project is to determine which customers from Telco are more likely to churn. While it would be impossible to eliminate churn completely, simply reducing the rate of churn could save the company a significant amount of revenue.


>Deliverables for this project include:
> - Final model created to predict if a customer will leave the company
> - This repo containing: 
>   - A Jupyter Notebook detailing the process to create this model
>   - Individual modules (.py files) that hold functions to acquire and prep the data
> - CSV file with customer_id, probability of churn, and prediction of churn 

### Background
Why is customer loyalty important? What is the cost of churn?
According to Fred Reichheld from [Bain&Company](https://media.bain.com/Images/BB_Prescription_cutting_costs.pdf),
>"A 5% increase in customer retention produces
>more than a 25% increase in profit. Why? Return customers tend
>to buy more from a company over time. As
>they do, operating costs to serve them decline."

### Data Dictionary
The Telco Churn data base contains four tables. The visual below shows each table name with the features in each, along with the foriegn keys that connect them together. For this project, the database is combined into one pandas dataframe.
![telco_churn_dataframe](https://i.pinimg.com/originals/6d/dd/1a/6ddd1a8c78c29dbb2d893ca820b2e79f.png)

After prepping the dataframe, the variables are as follows...

| Feature                   | Definition                            | Data Type                          |
|---------------------------|---------------------------------------|------------------------------------|
|senior_citizen             |senior or not senior                   |int - boolean                       |
|part_depd                  |has partner, dependents, or both       |int - (0-2)                         |
|phone_service              |one or multiple lines, or no service   |int - (0-2)                         |
|internet_service_type      |DSL, fiber optic, or no service        |int - (0-2)                         |
|online_security            |security or not                        |int - boolean                       |
|online_backup              |backup or not                          |int - boolean                       |
|device_protection          |protection or not                      |int - boolean                       |
|tech_support               |support or not                         |int - boolean                       |
|streaming (tv or movies)   |streaming or not                       |int - boolean                       |
|contract_type              |monthy, 1 year, 2 year                 |int - (0-2)                         |
|paperless_billing          |paperless or mailed bills              |int - boolean                       |
|charges (monthly or total) |in USD $                               |float                               |
|churn                      |customer has left the company or stayed|int - boolean                       |
|tenure (months or years)   |length the customer has remained loyal |int for months, float for years     |
|male                       |binary m/f                             |int - boolean, dummy var of gender  |

With the visual below, we can see these features split by service: phone, internet, or the overall company. Note: There are several more options for customers with internet service than phone service. Could this be influencing churn for customers with only phone service?
![telco_churn_service_features](https://i.pinimg.com/originals/c4/18/fd/c418fd573658ce791234564b3ea1e66d.png)
## Inital Hypothesis & Thought
### Thoughts
- Are customers with internet service more likely to remain loyal to the company? If so, is this because of the additional services that can be included? (Such as technical support or device protection)
- Could other factors be motivating customers to leave within phone or internet services? Are prices higher for one group? Are customers more likely to choose one contract type over another?
### Hypotheses
****
# **Project Steps**
## Acquire & Prepare
### acquire.py
Data is aquired from the company SQL database using a [querry](https://github.com/ThompsonBethany01/Telco_Churn/blob/master/acquire_churn.sql) to join all tables. Login credentials are required. Functions are stored in the [acquire.py](https://github.com/ThompsonBethany01/Telco_Churn/blob/master/acquire.py) file, which allows quick access to the data. Once the aquire file is imported, it can be used each time using the data.
### prepare.py
Within the [prepare.py](https://github.com/ThompsonBethany01/Telco_Churn/blob/master/prepare.py) file:
- Any duplicate observations are removed
- Features are converted to integer or float values
    - i.e. contract_type changed from monthly, yearly, ... to 0,1,2
- Feature for tenure in months created
- Null values in total_charges changed to 0 (due to new customer not being charged yet)
- Values for categorical variables are shown below
![telco_churn_service_features](https://i.pinimg.com/originals/77/e6/f9/77e6f9ae8f37e6f42c645d3fb55c2fb7.png)
## Explore
- Finding which features have the highest correlation to churn
- Testing hypothesis with Chi-Squared Contigency and T-test
- Visualizing churn with plots
    - Using sns.heatmap of correlation creates the visual below
    - I have highlighted the section which specifically displays correlation of churn to each feature
    - The heatmap can guide features we test and include in our model  


![telco_correlation_for_churn](https://i.pinimg.com/originals/56/01/cb/5601cbcca5eee9af0e24c575661140f5.png)  


Relevant exploration is documented in the final Modeling.ipynb. For the more in-depth exploration process, go to [Exploration.ipynb](https://github.com/ThompsonBethany01/Telco_Churn/blob/master/Exploration.ipynb)
## Model

## Conclusion
****
# **How to Reproduce**
