from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views import View
import os
from mysite.settings import BASE_DIR
from file_monitoring.models import FileLog

# Create your views here.
PATH_OF_FILE = os.path.join(BASE_DIR, './sample.txt')

class File:


    @classmethod
    def watcher(cls):
        file_data = ''
        with open(PATH_OF_FILE, 'r') as f:
            file_data = f.read()
        file_data = file_data.split('\n')
        last_15 = 0
        if (len(file_data)-15) > 0:
            last_15 = len(file_data)-15
        
        file_data = file_data[last_15:]
        file_data = " \n".join(file_data)
        return file_data



    @classmethod
    def update_the_file(cls, data):
        with open(PATH_OF_FILE, 'w') as f:
            data = f.write(data)
        FileLog(data).publish()



class GetFileData(View):
    def get(self, request):
        file_data = File.watcher()
        print("input_file_data",file_data)
        response = {
            "data":file_data
        }
        
        return JsonResponse(response)
    

class UpdateFile(View):
    def update(self, request):
        data = request.data['file']
        File.update_the_file(data)
        file_data = File.watcher()
        print("input_file_data",file_data)
        response = {
            "data":file_data
        }
        return JsonResponse(response)
