from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from healandhelp import serializers
from healandhelp.models import Website
import healandhelp.app_queries as queries
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import action 
import json  
from rest_framework import status

class Listing(viewsets.ModelViewSet):
    serializer_class = serializers.WebsiteSerializer

    def get_queryset(self):
        try:
            branch_id = self.request.query_params.get('branch_id')
            if branch_id is not None:
                return queries.Website.filter(branch__id=branch_id)
            return JsonResponse({
                    'status':False,
                    'message':'No Registration data',
                    'permits':[]
                }, safe=False, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({
                    'status':False,
                    'message':'No Registration data',
                    'permits':[]
                }, safe=False, status=status.HTTP_400_BAD_REQUEST)


class WebsiteViewSet(viewsets.ModelViewSet):
    
    @action(methods=['post'], detail=False)
    def add_registration_form(self, request, pk=None):
        try:
            data = request.data
            name = data['name']
            branch = data['branch']
            address = data['address']
            ref_no = data['ref_no']
            locality = data['locality']
            city = data['city']
            state = data['state']
            postalcode = data['postalcode']
            country = data['country']
            mobileno = data['mobileno']
            refrenced_by = data['refrenced_by']
            email = data['email'] 
            age = data['age']
            gender = data['gender']
            dateofbirth = data['dateofbirth']
            maritialstatus = data['maritialstatus']
            medication = data['medication']
            allergies = data['allergies']
            height = data['height']
            weight = data['weight']
            emergency_name = data['emergency_name']
            emergency_contact_no = data['emergency_contact_no']
            emergency_relationship = data['emergency_relationship']

        except Exception as e:
            return HttpResponse(json.dumps({
                'hot_ptw_id':None,
                'status': False,
                'message': 'Please Add Valid Data'+str(e)
            }), content_type='application/json', status=status.HTTP_400_BAD_REQUEST)

        try:

            if branch!=None:
                branch=queries.Branch.get(pk=branch)

            registration_form_instance = queries.Website.create(
                name=name,
                branch = branch,
                address=address,
                locality=locality,
                ref_no=ref_no,
                city=city,
                state=state,
                postalcode=postalcode,
                country=country,
                mobileno=mobileno,
                refrenced_by=refrenced_by,
                email=email,
                age=age,
                gender=gender,
                dateofbirth=dateofbirth,
                maritialstatus=maritialstatus,
                medication=medication,
                allergies=allergies,
                height=height,
                weight=weight,
                emergency_name=emergency_name,
                emergency_contact_no=emergency_contact_no,
                emergency_relationship=emergency_relationship
            )
            registration_form_instance.save()

            return HttpResponse(json.dumps({
                'registration_id':str(registration_form_instance.id),
                'status': True,
                'message': "Registraion form added successfully"
            }), content_type='application/json', status=status.HTTP_200_OK)

        except Exception as e:
            return HttpResponse(json.dumps({
                'registration_id':None,
                'status': False,
                'message': 'Something went wrong'+str(e)
            }), content_type='application/json', status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=True)
    def get_registration_details(self, request, pk=None):
        # Pass id of Risk Management
        try:
            rg_instance = queries.Website.get(pk=pk)
            rg_details = serializers.WebsiteSerializer(rg_instance).data

            return JsonResponse({
                'message': "Registration Details",
                'status':True,
                'registration_details':rg_details
                })
        except Exception as e:
            return HttpResponse(json.dumps({
                'registration_details':"",
                'status': False,
                'message': 'Something went wrong'+ str(e)
            }), content_type='application/json', status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=True)
    def update_registration_form(self, request, pk=None):
        try:
            data = request.data
            name = data['name']
            address = data['address']
            branch = data['branch']
            locality = data['locality']
            city = data['city']
            state = data['state']
            postalcode = data['postalcode']
            country = data['country']
            mobileno = data['mobileno']
            refrenced_by = data['refrenced_by']
            email = data['email'] 
            age = data['age']
            gender = data['gender']
            dateofbirth = data['dateofbirth']
            maritialstatus = data['maritialstatus']
            medication = data['medication']
            allergies = data['allergies']
            height = data['height']
            weight = data['weight']
            emergency_name = data['emergency_name']
            emergency_contact_no = data['emergency_contact_no']
            emergency_relationship = data['emergency_relationship']

        except Exception as e:
            return HttpResponse(json.dumps({
                'registration_id':"",
                'status': False,
                'message': 'Please Add Valid Data'+str(e)
            }), content_type='application/json', status=status.HTTP_400_BAD_REQUEST)


        try:
            if branch!=None:
                branch=queries.Branch.get(pk=branch)

            registration_instance = queries.Website.get(pk=pk)

            registration_instance.name=name
            registration_instance.branch = branch
            registration_instance.address=address
            registration_instance.locality=locality
            registration_instance.city=city
            registration_instance.state=state
            registration_instance.postalcode=postalcode
            registration_instance.country=country
            registration_instance.mobileno=mobileno
            registration_instance.refrenced_by=refrenced_by
            registration_instance.email=email
            registration_instance.age=age
            registration_instance.gender=gender
            registration_instance.dateofbirth=dateofbirth
            registration_instance.maritialstatus=maritialstatus
            registration_instance.medication=medication
            registration_instance.allergies=allergies
            registration_instance.height=height
            registration_instance.weight=weight
            registration_instance.emergency_name=emergency_name
            registration_instance.emergency_contact_no=emergency_contact_no
            registration_instance.emergency_relationship=emergency_relationship

            registration_instance.save()

            return HttpResponse(json.dumps({
                    'registration_id':"",
                    'status': True,
                    'message': "Registration Updated Successfully"
                }), content_type='application/json', status=status.HTTP_200_OK)

        except Exception as e:
            return HttpResponse(json.dumps({
                'registration_id':"",
                'status': False,
                'message': 'Something went wrong'+str(e)
            }), content_type='application/json', status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['DELETE'], detail=True)
    def delete_registration(self, request, pk=None):
        try:

            queries.Website.filter(pk=pk).delete()

            return JsonResponse({
                'status':True,
                'message':'Deleted',
            },  status=status.HTTP_200_OK)

        except Exception as e:
            return JsonResponse({
                'status':False,
                'message':'Could not delete permit' + str(e)
            }, safe=False, status=status.HTTP_400_BAD_REQUEST)


