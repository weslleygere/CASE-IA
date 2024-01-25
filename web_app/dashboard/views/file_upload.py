from django.shortcuts import render, redirect
from django.views.generic import View
from dashboard.forms import UploadFileForm
import pandas as pd
import pickle
from dashboard.models import PreProcessModel

class FileUploadView(View):
    """
    A view class for uploading a file.

    Attributes:
        template_name (str): The name of the template to render.
    """
    template_name = 'dashboard/dashboard.html'  # Use the same template as the dashboard
    model_tech_path = 'dashboard/models/arima_model_tech.pkl'
    model_furn_path = 'dashboard/models/arima_model_furn.pkl'
    model_office_path = 'dashboard/models/arima_model_office.pkl'

    def get(self, request):
        """
        Renders the file upload page.

        Args:
            request (HttpRequest): The request object used to generate this page.

        Returns:
            HttpResponse: The file upload page.
        """
        form = UploadFileForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        """
        Uploads a file.

        Args:
            request (HttpRequest): The request object used to generate this page.

        Returns:
            HttpResponse: The file upload page.
        """
        form = UploadFileForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, self.template_name, {'form': form})
        
        file = request.FILES['file']
        # Read the file
        data = pd.read_excel(file)
        # Preprocess the data
        preprocess_data = PreProcessModel.preprocess_data(data)

        # Load the model
        model_tech = pickle.load(open(self.model_tech_path, 'rb'))
        model_furn = pickle.load(open(self.model_furn_path, 'rb'))
        model_office = pickle.load(open(self.model_office_path, 'rb'))

        # filter the preprocess_data
        preprocess_data_technology = preprocess_data[preprocess_data['Category'] == 'Technology'].drop(columns=['Category'])
        preprocess_data_furniture = preprocess_data[preprocess_data['Category'] == 'Furniture'].drop(columns=['Category'])
        preprocess_data_office = preprocess_data[preprocess_data['Category'] == 'Office Supplies'].drop(columns=['Category'])    

        # Make predictions
        period = 12
        predictions_tech = model_tech.predict(period)
        predictions_furn = model_furn.predict(period)
        predictions_office = model_office.predict(period)
        
        # Last date
        last_date_tech = preprocess_data_technology.index[-1]
        last_date_furn = preprocess_data_furniture.index[-1]
        last_date_office = preprocess_data_office.index[-1]
        
        # Create the date range for predictions
        predictions_tech = pd.DataFrame(
            predictions_tech, 
            index=pd.date_range(last_date_tech, 
                                periods=period + 1, 
                                freq='MS')[1:], 
                                columns=['predicted_quantity']).reset_index().rename(columns={'index': 'Year_Month'})
        
        predictions_furn = pd.DataFrame(
            predictions_furn, 
            index=pd.date_range(last_date_furn, 
                                periods=period + 1, 
                                freq='MS')[1:], 
                                columns=['predicted_quantity']).reset_index().rename(columns={'index': 'Year_Month'})
        
        predictions_office = pd.DataFrame(
            predictions_office, 
            index=pd.date_range(last_date_office, 
                                periods=period + 1, 
                                freq='MS')[1:], 
                                columns=['predicted_quantity']).reset_index().rename(columns={'index': 'Year_Month'})

        context = {
            'form': form,
            'data': data.head().to_html(index=False),
            'preprocess_data': preprocess_data.head().reset_index().to_html(index=False),
            'prediction_tech': predictions_tech.to_html(index=False),
            'prediction_furn': predictions_furn.to_html(index=False),
            'prediction_office': predictions_office.to_html(index=False),
        }

        return render(request, self.template_name, context)
