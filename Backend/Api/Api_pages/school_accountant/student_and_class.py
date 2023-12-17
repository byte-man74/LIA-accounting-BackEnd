from django.utils import timezone
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework import status, viewsets
from rest_framework.views import APIView
# from Background_Tasks.tasks import
from django.core.cache import cache
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404
from Api.helper_functions.payment_section.main import get_student_id_from_request
from Main.models import Payroll, Operations_account_transaction_record
from Api.helper_functions.main import *
from Api.helper_functions.auth_methods import *
from Api.helper_functions.directors.main import *
from Api.Api_pages.operations.serializers import *
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework.exceptions import APIException


class GetListOfClass (APIView):
    '''This API returns the list of all the classes available in the school'''


class GetAllStudentsByClass (APIView):
    '''This API returns all the students depending on the class arguments passed'''


class GetStudentDetails (APIView):
    '''This API returns the details of a student based on the ID passed as a parameter'''


class GetStudentReciept (APIView):
    '''This API returns the list of all the student's reciepts'''


class CreateStudent (APIView):
    '''This API creates a new student'''


class EditStudent (APIView):
    '''This API updates a student's information'''


class DeleteStudent (APIView):
    '''This API deletes a student record'''


class GetFullRecieptInfo (APIView):
    '''This API retrieves the full student information'''
