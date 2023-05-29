from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import AccountModel
from ..utils.account_data_validator import AccountDataValidator
from loguru import logger


class SignupApiView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data["email"]
        password = request.data["password"]

        AccountDataValidator.validate(email, password)

        account = AccountModel.objects.create(
            email=email,
            password=password)

        logger.info(f"New account created: {email}")

        request.session["account_id"] = str(account.id)

        logger.info(f"User {email} started session on their account")

        return Response(status=status.HTTP_200_OK)
