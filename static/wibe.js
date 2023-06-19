document.getElementById('logout-button').addEventListener('click', function() {
    fetch('/logout', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            // Redirect to the login page or show a logout success message
            location.reload();
        } else {
            console.error('Logout failed');
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
