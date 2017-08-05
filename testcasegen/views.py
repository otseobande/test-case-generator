from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse

from xml.dom import minidom
import json
from .state import State
# Create your views here.

def index(request):
	return render(request, 'testcasegen/index.html')

@csrf_exempt
def processFile(request):
	if request.method == 'POST':
		file = request.FILES['file']

		fileContents = ""
		for chunk in file.chunks():
			fileContents += chunk.decode('unicode_escape')

		states = stateExtractor(fileContents)
		return JsonResponse(states)

def stateExtractor(contentString):
	doc = minidom.parseString(contentString);

	pseudoStates = doc.getElementsByTagName("UML:Pseudostate");
	simpleStates = doc.getElementsByTagName("UML:SimpleState");
	finalStates = doc.getElementsByTagName("UML:FinalState");

	stateList = []
	OrderedStateList = []
	stateDict = {}

	for i in pseudoStates:
		state_obj = State(i)
		if state_obj.kind == "initial":
			stateList.append(state_obj)

	for j in simpleStates:
		stateList.append(State(j))

	for k in finalStates:
		state_obj = State(i)
		if state_obj.kind == "final":
			stateList.append(state_obj)

	for i in stateList:
		if i.outgoing != None:
			outgoing = i.outgoing
		for j in stateList:
			if j.incoming != None:
				incoming = j.incoming
				if [node_id for node_id in outgoing if node_id in incoming]:
					if not i in OrderedStateList:
						OrderedStateList.append(i)
					if not j in OrderedStateList:
						OrderedStateList.append(j)

	for index, value in enumerate(OrderedStateList):
		stateDict[index] = {"name" : value.name,
							"id" : value.id,
							"incoming" : value.incoming,
							"outgoing" : value.outgoing,
							"kind" : value.kind,
							"type" : value.type }

	return stateDict;

		


