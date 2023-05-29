from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import AccountModel
from ..utils.account_data_validator import AccountDataValidator
from ..utils.signin_exceptions import *
from loguru import logger


class SigninService(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data["email"]
        password = request.data["password"]

        AccountDataValidator.validate_emptiness(email, password)

        accounts_with_same_email = AccountModel.objects.filter(email=email)

        if len(accounts_with_same_email) == 0:
            raise NotCorrectEmailGivenException

        account = accounts_with_same_email[0]

        if account.password != password:
            raise NotCorrectPasswordGivenException

        request.session["account_id"] = str(account.id)

        logger.info(f"User {email} started session on their account")

        return Response(status=status.HTTP_200_OK)
