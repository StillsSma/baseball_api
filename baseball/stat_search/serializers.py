from rest_framework import serializers

from stat_search.models import Master, Batting, Pitching, Fielding

class MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = '__all__'

class BattingSerializer(serializers.ModelSerializer):

    on_base_percentage = serializers.ReadOnlyField()

    class Meta:
        model = Batting
        fields = '__all__'

class PitchingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pitching
        fields = '__all__'

class FieldingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fielding
        fields = '__all__'
