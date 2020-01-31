from django.shortcuts import render
from django.http import HttpResponse

from django.http import JsonResponse


from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io

from .models import Incident
from .serializers import IncidentSerializer
from django.views.decorators.csrf import csrf_exempt


def index(request):

	return HttpResponse("Your are on the main page: isn't it beautiful ?")

def predict_Duree(unscaled_data):

	from sklearn.externals import joblib

	colonnes = ["reassignment_count","reopen_count","sys_mod_count","made_sla","u_priority_confirmation","knowledge"]

	path_to_model  = "./ipynb/model_simple.sav"

	path_for_scaler= "./ipynb/scaler.sav"

	unscaled_data   = [unscaled_data[colonne] for colonne in colonnes]

	model = joblib.load(path_to_model)

	scaler= joblib.load(path_for_scaler)

	donnees_scalees = scaler.transform([unscaled_data])

	duree = model.predict(donnees_scalees)

	return duree

# Create your views here.
@csrf_exempt
def predict(request):
	"""
		renvoie un incident avec une durée de Open To Close
	"""
	if request.method == 'GET':
		return JsonResponse(serializer.errors, status=400)

	if request.method == 'POST':

		data = JSONParser().parse(request)
		serializer  = IncidentSerializer(data=data)

		if serializer.is_valid():
			data["Duree_openToClose"]= predict_Duree(data)
			serializer          = IncidentSerializer(data=data)
			if serializer.is_valid():
				serializer.save()
				return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

