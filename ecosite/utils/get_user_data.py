from ..models import AccountModel


def get_user_data(request):
    authorized = "account_id" in request.session
    data = {
        "authorized": authorized,
    }

    if authorized:
        account_id = request.session["account_id"]
        data["email"] = AccountModel.objects.filter(id=account_id)[0].email

    return data
