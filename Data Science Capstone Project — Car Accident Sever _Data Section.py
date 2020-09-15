#!/usr/bin/env python
# coding: utf-8

# # IBM Data Science Capstone Report 

# # Seattle Car Accident Severity # 

# ## 1-  Business Understanding

# The Seattle government is going to prevent avoidable car accidents by employing methods that alert drivers, health system, and police to remind them to be more careful in critical situations.
# 

# In most cases, not paying enough attention during driving, abusing drugs and alcohol or driving at very high speed are the main causes of occurring accidents that can be prevented by enacting harsher regulations. Besides the aforementioned reasons, weather, visibility, or road conditions are the major uncontrollable factors that can be prevented by revealing hidden patterns in the data and announcing warning to the local government, police and drivers on the targeted roads.
# 

# The target audience of the project is local Seattle government, police, rescue groups, and last but not least, car insurance institutes. The model and its results are going to provide some advice for the target audience to make insightful decisions for reducing the number of accidents and injuries for the city.
# 

# ## 2-  Data section

# The data was collected by the Seattle Police Department and Accident Traffic Records Department from 2004 to present

# The data consists of 37 independent variables and 194,673 rows. The dependent variable, “SEVERITYCODE”, contains numbers that correspond to different levels of severity caused by an accident from 0 to 4

# Severity codes are as follows:

# 0: Little to no Probability (Clear Conditions)
# 
# 1: Very Low Probability — Chance or Property Damage
# 
# 2: Low Probability — Chance of Injury
# 
# 3: Mild Probability — Chance of Serious Injury
# 
# 4: High Probability — Chance of Fatality

# Furthermore, because of the existence of null values in some records, the data needs to be preprocessed before any further processing.

# ## Data Preprocessing

# The dataset in the original form is not ready for data analysis. In order to prepare the data, first, we need to drop the non-relevant columns. In addition, most of the features are of object data types that need to be converted into numerical data types.

# After analyzing the data set, I have decided to focus on only four features, severity, weather conditions, road conditions, and light conditions, among others.

# To get a good understanding of the dataset, I have checked different values in the features. The results show, the target feature is imbalance, so we use a simple statistical technique to balance it.

# In[ ]:




