# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, Donation, SUB_CHOICES
from .serializers import ProjectSerializer, ProjectDetailSerializer, DonationSerializer, DonationDetailSerializer
from django.http import Http404
from rest_framework import status, permissions
from .permissions import IsOwnerOrReadOnly, IsDonorOrReadOnly
from rest_framework.decorators import api_view

# Create your views here.

# for /projects
class ProjectList(APIView):
    # this make it so that a user must be logged in to post a project (remoes the POST button from /projects list)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

 #GET /projects
    def get(self, request):
        #get all the projects
        projects = Project.objects.all()
        #serialize all the projects
        serializer = ProjectSerializer(projects, many=True)
        #send all the serialized projects back in response body
        return Response(serializer.data)

#POST projects
    def post(self, request):
        #try to create a serializer from the data in the request body
        serializer = ProjectSerializer(data=request.data)
        #if the serializer thinks its valid
        if serializer.is_valid():
            #save the object
            serializer.save(owner=request.user)
            #send the serialized (saved) data back in response body
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )
#/projects/<pk>
class ProjectDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

#helper method to get the object with the pk

    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return project
        except Project.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

#update /project/<pk>
    def put(self, request, pk):
        project = self.get_object(pk)
        data = request.data
        serializer = ProjectDetailSerializer(
            instance=project,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
#delete a project

    def delete(self, request, pk):
        project = self.get_object(pk)
        project.delete()
        return Response(dict(message = 'Project successfully deleted'))

#for /donations/        
class DonationList(APIView):

#GET donation
    def get(self, request):
        if self.request.user.is_superuser:
            donations = Donation.objects.all()
        else:
            donations = Donation.objects.filter(donor=self.request.user)

        serializer = DonationSerializer(donations, many=True)
        return Response(serializer.data)

#POST donation
    def post(self, request):
        serializer = DonationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(donor = request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

# for /donations/<pk>
class DonationDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsDonorOrReadOnly
    ]

#GET /donations/<pk>
    def get_object(self, pk):
        try:
            donation = Donation.objects.get(pk=pk)
            self.check_object_permissions(self.request, donation)
            return donation
        except Donation.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        donation = self.get_object(pk)
        serializer = DonationSerializer(donation)
        return Response(serializer.data)

# update /donations/<pk>  
    def put(self, request, pk):
        donation = self.get_object(pk)
        serializer = DonationDetailSerializer(
            instance=donation,
            data = request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

# We dont want users to be able to delete donations!
# # delete /donations/<pk>
#     def delete(self, request, pk):
#         donation = self.get_object(pk)
#         donation.delete()
#         return Response(dict(message= 'Donation deleted!'))

# @api_view(['GET'])
# def get_all_locations(self, request):
#     locations = []
#     for i in SUB_CHOICES:
#         locations.append(i[0])
#     return Response(locations)