import pandas as pd
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        file_name = fs.save(uploaded_file.name, uploaded_file)
        file_url = fs.url(file_name)
        
        # Read the uploaded file
        if uploaded_file.name.endswith('.csv'):
            data = pd.read_csv(fs.path(file_name))
        elif uploaded_file.name.endswith('.xlsx'):
            data = pd.read_excel(fs.path(file_name))

        # Generate summary report
        summary = data.describe(include='all')  # Summary report using Pandas
         
        context = {
            'file_url': file_url,
            'columns': data.columns,
            'summary': summary.to_html(classes="table table-bordered"),
        }
        return render(request, r'D:\machine learning\Django Assignment\DevTest\fileupload\templates\fileupload\upload_file.html', context)
    return render(request, r'D:\machine learning\Django Assignment\DevTest\fileupload\templates\fileupload\upload_file.html')