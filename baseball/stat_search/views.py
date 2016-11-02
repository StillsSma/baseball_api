from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from stat_search.models import Master, Batting, Pitching, Fielding
from stat_search.serializers import MasterSerializer, BattingSerializer, PitchingSerializer, FieldingSerializer

class MasterListCreateAPIView(ListCreateAPIView):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer

class MasterDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer

class BattingListCreateAPIView(ListCreateAPIView):
    queryset = Batting.objects.all()
    serializer_class = BattingSerializer

class BattingDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Batting.objects.all()
    serializer_class = BattingSerializer

class PitchingListCreateAPIView(ListCreateAPIView):
    queryset = Pitching.objects.all()
    serializer_class = PitchingSerializer

class PitchingDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Pitching.objects.all()
    serializer_class = PitchingSerializer

class FieldingListCreateAPIView(ListCreateAPIView):
    queryset = Fielding.objects.all()
    serializer_class = FieldingSerializer

class FieldingDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Fielding.objects.all()
    serializer_class = FieldingSerializer
