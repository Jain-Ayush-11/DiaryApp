from rest_framework.decorators import api_view
from rest_framework.response import Response
from diary.models import Entry
from .serializers import NoteSerializer
from django.shortcuts import render, redirect

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/Note',
        'GET /api/Note/:id',
    ]
    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    notes = Entry.objects.all()
    serializer = NoteSerializer(notes, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request, pk):
    pk = int(pk)
    notes = Entry.objects.get(id=pk)
    serializer = NoteSerializer(notes, many = False)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def createNote(request):
    serializer = NoteSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def updateNote(request, pk):
    pk = int(pk)
    note = Entry.objects.get(id = pk)
    serializer = NoteSerializer(instance=note, data = request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
