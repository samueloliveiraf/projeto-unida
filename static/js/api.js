async function getUsers() {
    await fetch('http://localhost:8000/api-users/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer'
            }
        })
        .then(response => response.json())
        .then(data => {
            var html = ""
            data.forEach(function(users) {
                if (users.is_staff === true) {
                    users.is_staff = 'SIM'
                } else {
                    users.is_staff = 'NÃO'
                }

                html += `
                <div class="card">
                    <div>
                        <p>Usuário: ${users.username}<p>
                    </div>
                    <div>
                        <p>E-mail: ${users.email}<p>
                    </div>
                    <div>
                        <p>Super Usuário: ${users.is_staff}<p>
                    </div>
                </div>
                `
            })
            document.getElementById('info-users').innerHTML = html
        })
}
getUsers()