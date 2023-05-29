function signup() {
    let email = $(".email-input").val();
    let password = $(".password-input").val();
    let confirmed_password = $(".confirmed-password-input").val();

    if (confirmed_password != password) {
        Swal.fire({
            icon: 'error',
            title: 'Упс...',
            text: 'Кажется, что потвержденный пароль не похож на вышестоящий. Попробуй еще раз.',
            confirmButtonText: 'Ок',
        });
        return;
    }
  
    $.ajax({
        type: "post",
        url: "/api/signup/",
        data: {
            email: email,
            password: password,
        },
        success: function (data, text) {
            Swal.fire({
                icon: 'success',
                title: 'Вы успешно зарегистрировались!',
                text: 'Теперь вы можете войти в свой аккаунт.',
                showConfirmButton: false,
                timer: 2000,
            }).then((value) => {
                window.location.replace('/');
            })
        },
        error: function (request, status, error) {
            Swal.fire({
                icon: 'error',
                title: 'Упс...',
                text: request.responseJSON["detail"],
                confirmButtonText: 'Ок',
            });
        }
    })
}