from django.db import models
import pandas as pd

class PreProcessModel(models.Model):
    """
    A model class for storing and processing data.

    Attributes:
        data (pd.DataFrame): The data stored in the model.
    """

    @staticmethod
    def preprocess_data(data):
        """
        Preprocess the input data.

        Args:
            data (pd.DataFrame): The input data.

        Returns:
            pd.DataFrame: The preprocessed data.
        """
        data = data.copy()

        # Filter the relevant columns
        data = data[['Order Date', 'Category','Quantity']]
        # Create a Year_Month column
        data['Year_Month'] = data['Order Date'].dt.strftime('%Y-%m')
        # Drop the Order Date column
        data = data.drop(columns=['Order Date'])
        # Group by Year_Month and Category, and sum the Quantity
        data = data.groupby(['Year_Month', 'Category'], as_index=False)['Quantity'].sum()
        # Change the column Year_Month to datetime type
        data['Year_Month'] = pd.to_datetime(data['Year_Month'])        
        # Set the Year_Month column as the index
        data = data.set_index('Year_Month')

        return data