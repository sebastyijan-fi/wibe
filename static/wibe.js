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
                    // Refresh the wibe feed
                    fetchAndDisplayWibes();
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
function timeAgo(serverTimestamp) {
    const serverTime = new Date(serverTimestamp); // This is already in UTC
    const localTime = new Date(); // This is in the local timezone

    const getDifferenceIn = (unit) => Math.floor((localTime - serverTime) / unit);

    const minute = 1000 * 60;
    const hour = minute * 60;
    const day = hour * 24;
    const week = day * 7;

    if (getDifferenceIn(week) > 0) {
        const diff = getDifferenceIn(week);
        return `${diff} week${diff !== 1 ? 's' : ''} ago`;
    } else if (getDifferenceIn(day) > 0) {
        const diff = getDifferenceIn(day);
        return `${diff} day${diff !== 1 ? 's' : ''} ago`;
    } else if (getDifferenceIn(hour) > 0) {
        const diff = getDifferenceIn(hour);
        return `${diff} hour${diff !== 1 ? 's' : ''} ago`;
    } else if (getDifferenceIn(minute) > 0) {
        const diff = getDifferenceIn(minute);
        return `${diff} minute${diff !== 1 ? 's' : ''} ago`;
    } else {
        return 'Just now';
    }
}


function fetchAndDisplayWibes() {
    // Send a GET request to the server to fetch the wibes
    fetch('/get-wibe', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        // The data should be an array of wibes
        // Now we can display them on the webpage
        displayWibes(data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function displayWibes(wibes) {
    var wibeFeed = document.getElementById('wibe-feed');

    // Remove all existing children
    while (wibeFeed.firstChild) {
        wibeFeed.removeChild(wibeFeed.firstChild);
    }

    // Rearrange wibes so that user's latest wibe is always first
    const userLatestWibe = wibes.pop();
    wibes.unshift(userLatestWibe);

    // Sort other wibes in descending order of timestamp
    wibes.slice(1).sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));

    // For each wibe, create a new div and append it to the feed
    for (var i = 0; i < wibes.length; i++) {
        var wibe = wibes[i];
        var wibeDiv = document.createElement('div');
        wibeDiv.classList.add('wibe-card');

        // Add a special class to user's latest wibe
        if (i === 0) {
            wibeDiv.classList.add('user-latest-wibe');
        }

        var countryPara = document.createElement('p');
        countryPara.textContent = `From: ${wibe.country}`;
        wibeDiv.appendChild(countryPara);

        var timestampPara = document.createElement('p');
        timestampPara.textContent = timeAgo(wibe.timestamp);
        timestampPara.classList.add('timestamp');
        wibeDiv.appendChild(timestampPara);

        var textPara = document.createElement('p');
        textPara.textContent = wibe.mood_input;
        wibeDiv.appendChild(textPara);

        wibeFeed.appendChild(wibeDiv);
    }
}

// Call the function to fetch and display wibes when the page loads
fetchAndDisplayWibes();


function toggleTooltip() {
    var tooltip = document.getElementById("tooltip");
    tooltip.style.display = tooltip.style.display === "none" ? "inline" : "none";
}
