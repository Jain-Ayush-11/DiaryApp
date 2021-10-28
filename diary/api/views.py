import collections
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from diary.models import Entry, Collection
from .serializers import NoteSerializer, CollectionSerializer

class NotesList(APIView):
    def get(self, request, format = None):
        notes = Entry.objects.all()
        serializer = NoteSerializer(notes, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class NoteDetails(APIView):
    def get(self, request, pk, format = None):
        pk = int(pk)
        notes = Entry.objects.get(id=pk)
        serializer = NoteSerializer(notes, many = False)
        return Response(serializer.data)

    def put(self, request, pk, format = None):
        pk = int(pk)
        note = Entry.objects.get(id = pk)
        serializer = NoteSerializer(instance=note, data = request.data)

        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk, format = None):
        pk = int(pk)
        note = Entry.objects.get(id = pk)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CollectionList(APIView):
    def get(self, request, format = None):
        collection = Collection.objects.all()
        serializer = CollectionSerializer(collection, many = True)
        return Response(serializer.data)