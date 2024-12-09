import os
import zipfile

import pandas as pd
from abc import ABC,abstractmethod

class DataIngestor(ABC):
    @abstractmethod
    def ingest(self,filepath:str) -> pd.DataFrame:
        pass
    
#Implement a concrete class for Zipfile Extraction (Cappuccino)
class ZipDataIngestor(DataIngestor):
    
    def ingest(self,filepath:str)-> pd.DataFrame:
        
        #Ensure the file is .zip
        if not filepath.endswith(".zip"):
            raise ValueError("The provided file is not a .zip file.")
        
        #Extract the zip file
        with zipfile.ZipFile(filepath,"r") as zip_ref:
            zip_ref.extractall("extracted_data")
            
        #Find the extracted CSV file (assuming there is only one CSV file inside the zip)
        extracted_files = os.listdir("extracted_data")
        csv_files = [f for f in extracted_files if f.endswith(".csv")]
        
        if len(csv_files)==0:
            raise FileNotFoundError("No CSV file found in the extracted data.")
        if len(csv_files)>1:
            raise ValueError("Multiple CSV files found. Please specify which one to use.")
        
        #Read the CSV into DataFrame 
        csv_file_path=os.path.join("extracted_data", csv_files[0])
        df=pd.read_csv(csv_file_path)
        
        #Return the DataFrame
        return df
    
    
#Implement a Factory to create DataIngestor(Coffee machine)
class DataIngestorFactory:
    
    @staticmethod
    def get_data_ingestor(file_extension:str) -> DataIngestor:
        if file_extension ==".zip":
            return ZipDataIngestor()
        else:
            return ValueError(f"No ingestor available for file extension: {file_extension}")
        

#Example Usage:

if __name__=="__main__":
    
    #Specify the file path
    file_path="C:/Users/aakar/Desktop/ML projects/End_to_End_Prices_Predictior_System/Data/archive.zip"
    
    #Determine the file extension
    file_extension = os.path.splitext(file_path)[1]
    
    
    #Get the appropriate DataIngestor
    data_ingestor = DataIngestorFactory.get_data_ingestor(file_extension)
    
    #Ingest the data and load 
    df = data_ingestor.ingest(file_path)
    
    #Now df contains the DataFrame from the extracted CSV
    print(df.head())
    

    
    

    
        
    
        