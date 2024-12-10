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
        
    3. Missing Value Analysis
