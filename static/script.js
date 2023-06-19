document.getElementById('register-link').addEventListener('click', function(event) {
    event.preventDefault();
    document.getElementById('login-form').style.display = 'none';
    document.getElementById('registration-form').style.display = 'flex';
});

document.getElementById('login-link').addEventListener('click', function(event) {
    event.preventDefault();
    document.getElementById('registration-form').style.display = 'none';
    document.getElementById('login-form').style.display = 'flex';
});

document.getElementById('login-submit').addEventListener('click', function(event) {
    event.preventDefault();  // Prevent the form from being submitted normally

    // Get the username and password from the form
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;

    console.log('Username: ' + username); // Debug line
    console.log('Password: ' + password); // Debug line

    // Prepare the data to be sent
    let data = {
        'username': username,
        'password': password
    }

    console.log('Data to be sent: ', data); // Debug line

    // Make a POST request to the /login route
    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        console.log('Response status: ' + response.status); // Debug line
        return response.json();
    })  // Parse the JSON response
    .then(data => {
        console.log('Response data: ', data); // Debug line
        if (data.error) {
            // If there was an error logging in, display it to the user
            alert(data.error);
        } else {
            // If the login was successful, redirect the user to the home page
            console.log("Login successful!");
            window.location.href = "/";
        }
    })
    .catch((error) => {
        // Log any errors to the console
        console.error('Error:', error);
    });
});


document.getElementById('register-submit').addEventListener('click', function(event) {
    event.preventDefault();  // Prevent the form from being submitted normally

    // Get the username, password and email from the form
    let username = document.getElementById('register-username').value;
    let password = document.getElementById('register-password').value;
    let email = document.getElementById('register-email').value;

    console.log('Username: ' + username); // Debug line
    console.log('Password: ' + password); // Debug line
    console.log('Email: ' + email); // Debug line

    // Prepare the data to be sent
    let data = {
        'username': username,
        'password': password,
        'email': email
    }

    console.log('Data to be sent: ', data); // Debug line

    // Make a POST request to the /register route
    fetch('/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        console.log('Response status: ' + response.status); // Debug line
        return response.json();
    })  // Parse the JSON response
    .then(data => {
        console.log('Response data: ', data); // Debug line
        if (data.error) {
            // If there was an error during registration, display it to the user
            alert(data.error);
        } else {
            // If the registration was successful, redirect the user to the home page
            console.log("Registration successful!");
            window.location.href = "/";
        }
    })
    .catch((error) => {
        // Log any errors to the console
        console.error('Error:', error);
    });
});
