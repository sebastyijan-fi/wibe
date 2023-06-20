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


document.getElementById('wibe-submit').addEventListener('click', function() {
    var wibeText = document.getElementById('wibe-text').value;  // Get the wibe text

    // Make sure the wibe isn't empty
    if(wibeText.trim() !== "") {
        // Fetch the country
        fetch('https://ipapi.co/json/')
        .then(response => response.json())
        .then(data => {
            var country = data.country_name;
            var wibeData = {
                text: wibeText,
                country: country  // Add the country to the wibe data
            };

            // Send the wibe to the server
            fetch('/submit-wibe', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(wibeData)
            })
            .then(response => response.json())
            .then(data => {
                if(data.status === 'success') {
                    // Handle successful wibe submission
                    // For example, clear the input field and show a success message
                    document.getElementById('wibe-text').value = "";
                    alert("Wibe submitted successfully!");
                } else {
                    // Handle failed wibe submission
                    // For example, show an error message
                    alert("Wibe submission failed. Please try again.");
                }
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        });
    } else {
        // Handle empty wibe
        // For example, show an error message
        alert("Please enter a wibe before submitting.");
    }
});
