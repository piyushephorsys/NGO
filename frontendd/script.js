const API_BASE_URL = "http://localhost:8000";

async function loadDonations() {
    try {
        const response = await fetch(`${API_BASE_URL}/donate/`);
        const donations = await response.json();

        const container = document.getElementById("donationContainer");
        container.innerHTML = "";

        donations.forEach(donation => {
            const card = document.createElement("div");
            card.className = "card";

            card.innerHTML = `
                <img src="${API_BASE_URL}${donation.image_url}" alt="Donation Image">
                <h3>${donation.name}</h3>
                <p><strong>Email:</strong> ${donation.email}</p>
                <p><strong>Address:</strong> ${donation.address}</p>
            `;

            container.appendChild(card);
        });

    } catch (error) {
        console.error("Error loading donations:", error);
    }
}


loadDonations();
