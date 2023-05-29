function quit() {
    $.ajax({
        url: "/api/quit/",
        success: function (data, text) {
            Swal.fire({
                icon: 'success',
                title: 'Вы успешно вышли из своего аккаунта',
                text: 'Теперь вы можете войти в другой свой аккаунт.',
                showConfirmButton: false,
                timer: 2000,
            }).then((value) => {
                window.location.replace('/login/');
            })
        },
        error: function (request, status, error) {
            Swal.fire({
                icon: 'error',
                title: 'Упс...',
                text: 'Произошла ошибка и вы не можете выйти из своего аккаунта.',
                confirmButtonText: 'Ок',
            });
        }
    })
}
