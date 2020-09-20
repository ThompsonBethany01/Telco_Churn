# **Predicting Churn at Telco**

## About the Project
### Goals
Churn is defined as the rate at which customers leave a company. This is bad for business, as it often costs more to attract new customers than to keep current customers. The goal of this project is to determine which customers from Telco are more likely to churn. While it would be impossible to eliminate churn completely, simply reducing the rate of churn could save the company a significant amount of revenue.
### Background
### Data Dictionary
The Telco Churn data base contains four tables. The visual below shows each table name with the features in each, along with the foriegn keys that connect them together. For this project, the database is combined into one pandas dataframe.
![telco_churn_dataframe](https://i.pinimg.com/originals/94/f3/bc/94f3bcb57a2a2ce1755337dc684b54c1.png)

After prepping the dataframe, the variables are as follows...
Booleans represent 1 as 'Yes' and 0 as 'No'

| Feature                   | Definition                            | Data Type                          |
|---------------------------|---------------------------------------|------------------------------------|
|senior_citizen             |senior or not senior                   |int - boolean                       |
|partner                    |has partner or not                     |int - boolean                       |
|dependents                 |has dependent or not                   |int - boolean                       |
|phone_service              |has phone service or not               |int - boolean                       |
|multiple_lines             |phone lines - one, mulitple, or none   |object                              |
|internet_service_type      |DSL, fiber Optic, or None              |object                              |
|online_security            |secuirty, no security, no internet     |object                              |
|online_backup              |backup, no backup, no internet         |object                              |
|device_protection          |protection, no protection, no internet |object                              |
|tech_support               |support, no support, no internet       |object                              |
|streaming (tv or movies)   |streaming, no streaming, no internet   |object                              |
|paperless_billing          |paperless or mailed bills              |int - boolean                       |
|charges (monthly or total) |in USD $                               |float                               |
|churn                      |customer has left the company or stayed|int - boolean                       |
|tenure (months or years)   |length the customer has remained loyal |int for months, float for years     |
|male                       |binary m/f                             |int - boolean, dummy var of gender  |

With the visual below, we can see these features split by service: phone, internet, or the overall company. Note: There are many more options for customers with internet service than phone service. Could this be influencing churn for customers with only phone service?
![telco_churn_service_features](https://i.pinimg.com/originals/c4/18/fd/c418fd573658ce791234564b3ea1e66d.png)
## Inital Hypothesis & Thought
### Thoughts
### Hypotheses
****
# **Project Steps**
## Acquire & Prepare
### acquire.py
Data is aquired from the company SQL database. Login credentials are required. Functions are stored in the [acquire.py](https://github.com/ThompsonBethany01/Telco_Churn/blob/master/acquire.py) file, which allows quick access to the data. Once the aquire file is imported, it can be used each time using the data.
### prepare.py

## Explore

## Model

## Conclusion
****
# **How to Reproduce**
