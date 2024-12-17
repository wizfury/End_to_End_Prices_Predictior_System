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

    ## Strategy Design pattern
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
        a. Handlig Missing Data:

            - Significant missing values: columns like Alley, Pool QC, Fence, and Misc Feature have a high percentage of missing data. Decisions need to be made whether to:
                i. Drop these columns entirely.
                ii. impute missing values with a placeholder to retain them in the analysis.

            - Moderate missing values: Features related to basements and garages will require careful handling. Missing values could be filled with "No Basement" or "No Garages" for categorical features, and zeros for numericsl ones.

            - Single missing values: these can likely be filled with the mode for categorical and mean for numerical features.
            
        b. Outlier Detection and Handling:
            - this will need to be detected and handled appropriately to avoid skewing model predictions.

        c. Categorical Encoding:
            - Decisions need to be made on how to encode these(e.g. one-hot encoding, label encoding, or frequency encoding) based on their relationship with the target values

        d. Feature Engineering:
            - Based on insights, certain geatures might need to be engineered(e.g. combining related features, creating interaction terms, or transforming skewed features) to better capture the relationship in the data.

        5. Correlation and Multicollinearity:
            - Initial correlation analysis suggests that some features might be highly correlated with each other. this could lead to Multicollinearity issues, which need to be addressed during feature selection.

    5. Insights from Univariate Analysis:
        1. SalesPrice Distribution:
            i. SalesPrice is positively skewed, with majority of house prices falling between $100000 and 250000.

            ii. This skewness suggests that most homes is the dataset ar relatively affordable, with a few high end properties. A long tail on the right indicates a small number of more expensive homes.
        
        2. Neighbourhood Distribution:
            i. insight: The Neighborhood features shows a varied distribution, with NAmes being the most common neighborhood, followerd by CollCr and OldTown.

            ii. High frequency of neighborhood suggests that these could significantly influence overall housing prices.

    6. Insights from Bivariate Analysis:
        1. Gr Liv Area vs SalePrice (Numerical vs Numerical):
            i. Insight: There is a strong positive correlation between Gr Liv Area(Above Fround Living Area) and SalePrice, indication that larger homes generally sell for higher prices. The relationship appears mostly linear, but there are a few outliers, especiallt at higher Gr Liv Area values.

            ii. Implication: This linear relationship confirms that Gr Liv Area is likely a string Predictor of SalePrice. However, the presence of outliers might require further investigstion.

        2. Overall Qual vs SalePrice (Categorical vs Numerical):
            i. Insight: there is a clear relationship between Overall Qual and SalePrice, wirj higher rating associated  with significantly higher price.

            ii. Implication: Overall Qual is another stronger predictior of SalePrice. Homebuyers highly value quality.

        







