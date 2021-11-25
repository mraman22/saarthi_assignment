from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from library.models import Books
from library.serializers import LibrarySerializer
from rest_framework.decorators import api_view

from django.core.exceptions import ObjectDoesNotExist


@api_view(['GET'])
def searchBookByName(req, name):
    try :
        result = Books.objects.filter(name__exact = name)
        books_serialized = LibrarySerializer(result, many = True)
        res = {"status_code" : status.HTTP_200_OK, "status" : "success", "data" : books_serialized.data }
    
    except ObjectDoesNotExist:
        res = {"status_code" : status.HTTP_200_OK, "status" : "success", "data" : [] }
    return JsonResponse(res, safe=False)



# add book and get allbooks
@api_view(['GET', 'POST'])
def getAllBooks_addBook(req):  
    if req.method == "POST":
        newBook_data = JSONParser().parse(req)
        newBook_serializer = LibrarySerializer(data=newBook_data)

        if newBook_serializer.is_valid():
            newBook_serializer.save()
            res = {"status_code" : status.HTTP_201_CREATED, "status" : "success", "data" : [{"book" : newBook_serializer.data}] }
            return JsonResponse(res, status=status.HTTP_201_CREATED) 
        else :
            res = {"status_code" : status.HTTP_400_BAD_REQUEST, "status" : "failed", "error" : newBook_serializer.errors }
            return JsonResponse(res, status=status.HTTP_400_BAD_REQUEST)

    elif req.method == "GET":
        try:
            result = Books.objects.all()
            books_serialized = LibrarySerializer(result, many = True)
            print(books_serialized)
            res = {"status_code" : status.HTTP_200_OK, "status" : "success", "data" :  books_serialized.data}

        except ObjectDoesNotExist:
            res = {"status_code" : status.HTTP_200_OK, "status" : "success", "data" : [] }
        return JsonResponse(res, safe=False)

    else :
        res = {"status_code" : status.HTTP_400_BAD_REQUEST, "status" : "failed"}
        return JsonResponse(res, status=status.HTTP_204_NO_CONTENT)

    
# get , delete , update book by id

@api_view(['GET', 'PATCH', 'DELETE'])
def bookById(req, id):
    if req.method == "GET":
        try:
            result = Books.objects.filter(pk = id)
            books_serialized = LibrarySerializer(result, many = True)

            data = []
            if(len(books_serialized.data)>0):
                data = books_serialized.data[0]
                data["id"] = int(id)
            res = {"status_code" : status.HTTP_200_OK, "status" : "success", "data" :  data}
        except ObjectDoesNotExist:
            res = {"status_code" : status.HTTP_200_OK, "status" : "success", "data" : [] }
        return JsonResponse(res, safe=False)

    elif req.method == "PATCH":
        try:
            book = Books.objects.get(pk=id)
            updateBook_data = JSONParser().parse(req)
            updateBook_serializer = LibrarySerializer(book, data=updateBook_data)

            if updateBook_serializer.is_valid():
                updateBook_serializer.save()
                data =  updateBook_serializer.data
                data["id"] = int(id)
                res = {"status_code" : status.HTTP_200_OK, "status" : "success", "message": "The book " + data["name"] + " was updated successfully", "data" : data}
                return JsonResponse(res, status=status.HTTP_201_CREATED) 

            else :
                res = {"status_code" : status.HTTP_400_BAD_REQUEST, "status" : "failed", "error" : updateBook_serializer.errors }
                return JsonResponse(res, status=status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:
            res = {"status_code" : status.HTTP_200_OK, "status" : "success", "message" : "requested book does not exist!", "data" : [] }
            return JsonResponse(res, safe=False)

    elif req.method == "DELETE":
        try : 
            book = Books.objects.get(pk=id)
            book.delete()
            res = {"status_code" : status.HTTP_200_OK, "status" : "success", "message": "The book " + book.name + " was deleted successfully", "data" : []}
        except ObjectDoesNotExist:
            res = {"status_code" : status.HTTP_200_OK, "status" : "success", "message" : "requested book does not exist!", "data" : [] }
        return JsonResponse(res, status=status.HTTP_200_OK)

    else :
        res = {"status_code" : status.HTTP_400_BAD_REQUEST, "status" : "failed"}
        return JsonResponse(res, status=status.HTTP_204_NO_CONTENT)
