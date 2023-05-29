function signin() {
    let email = $(".email-input").val();
    let password = $(".password-input").val();

    $.ajax({
        type: "post",
        url: "/api/signin/",
        data: {
            email: email,
            password: password,
        },
        success: function (data, text) {
            Swal.fire({
                icon: 'success',
                title: 'Вы успешно вошли в аккаунт!',
                text: 'Теперь вы можете начать делать этот мир лучше!',
                showConfirmButton: false,
                timer: 2500,
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
            })
        }
    })
}