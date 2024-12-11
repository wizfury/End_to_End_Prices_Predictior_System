First step is always to load the data

# Data Ingestion:

    ** using design pattern to handle data.
    ** make it readable and reproducible.

        We'll use a Factory design pattern

        # Factory Design pattern

        Create a one simple general coffee machine.

    Key Elements:
        ** Type checkings
        ** Readability
        ** Error Handling
        ** Making sure we are handling errors

        ## Rule 5: Do not forgot all the 4 rules

# EDA (Exploratory Data Analysis):

    ** Strategy Design pattern
        Supppose, developing a e-commerce application. The context is same but the startegy differs.

    1. Data Type Analysis:
        ** This dataset contains 2930 entries and 82 columns
        ** Data Types: There are 11 columns with Float64 data type, 28 columns with int64 data type, 43 columns wirh object data type

    2. Summary Statistics:
        a. Numerical Features:
            - The target variable SalePrice has a mean of $180,796 with a standard deviation of $79,886, indicating a significant spread in house price.
            
            (Stanndard Deviation tells whether most data points are clustered near the average or spread out over a wider range.)
            
            - Overall Qual (quality of the house) rnages from 1 to 10, with a mean of 6.09, showing a relatively high quality on average.

            - Year Built ranges from 1872 to 2010, indicating that the data set includes both very old and relatively new houses and most of the houses were build around 1971.

            - Lot Area has a wide range, with some extreme outliers (max of 215,245 sqft), which indicates large properties.

            -The distribution of Gr Live Area shows mean of 1499 sqft with wide range, which could significantly impact SalesPrice.

        b. Categorically Features:
            - Neighborhood has 28 unique values with NAmes being the most common, suggesting some neighborhoods might dominate the dataset.

            - MS Zoning is Mostly RL(Residential low density), with 7 unique zoning types.

        
    3. Missing Value Analysis(Heatmap Insights)

        a. Colors Represent Missingness:
            - Yellow: Represent missing values. The more the yellow you see in a column, the more missing data is present in that particular feature.
            - Purple: Represents non-missing values. Columns that are mostly purple indicate that most of the data is present in that feature.

        b. Identifying Columns with Missing Data:
            - Look for columns with significant amount of yellow. These columns have a higher properties of missing data.
        
        c. Understanding the distribution of missinf values:
            - Randomly Distributed: If the yellow marks are scattered without any noticeable pattern, it suggests that the missing data might be randomly distributed.

            - Structures Missingness: If the yellow clustered in certain rows or columns it might indicate a non- random pattern of missingness.

        d. Assessing the Severity:
            - In the heatmap. some columns have little to no missing values, while others have subsequential missingness. Decisions will need to be made whether to impute, drop, or handle these features differently.

    4. Issues to be addressed:
        



