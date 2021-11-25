from rest_framework import serializers 
from library.models import Books
 
 
class LibrarySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Books
        fields = ('name',
                  'isbn',
                  'authors',
                  'number_of_pages',
                  'publisher',
                  'country',
                  'release_date')