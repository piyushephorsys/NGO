const API_BASE_URL = "http://localhost:8000/images";

async function loadImages() {
    try {
        // 1️⃣ Fetch all image metadata
        const response = await fetch(API_BASE_URL);
        const images = await response.json();

        const container = document.getElementById("imageContainer");
        container.innerHTML = "";

        // 2️⃣ Loop through all images
        images.forEach(image => {
            const card = document.createElement("div");
            card.className = "card";

            card.innerHTML = `
                <img 
                    src="${API_BASE_URL}/${image.id}" 
                    alt="${image.filename}"
                >
                <p><strong>Description:</strong> ${image.description}</p>
            `;

            container.appendChild(card);
        });

    } catch (error) {
        console.error("❌ Error loading images:", error);
    }
}

// 3️⃣ Call function
loadImages();
