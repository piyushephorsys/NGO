document.getElementById("loginForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const errorMessage = document.getElementById("errorMessage");

    errorMessage.innerText = "";

    try {
        const response = await fetch("http://localhost:8000/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username: username,
                password: password
            })
        });

        if (response.ok) {
            // ✅ Login success → redirect
            window.location.href = "dashboard.html";
        } else {
            // ❌ Login failed → show popup message
            const data = await response.json();
            errorMessage.innerText = data.detail || "Invalid username or password";
        }

    } catch (error) {
        errorMessage.innerText = "Server not reachable";
    }
});
