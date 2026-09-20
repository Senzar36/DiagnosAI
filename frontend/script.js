// =========================
// DIAGNOSAI FEATURES
// =========================

const features = [
    "fatigue",
    "vomiting",
    "high_fever",
    "loss_of_appetite",
    "nausea",
    "abdominal_pain",
    "headache",
    "yellowish_skin",
    "yellowing_of_eyes",
    "skin_rash",
    "chills",
    "malaise",
    "chest_pain",
    "sweating",
    "joint_pain",
    "itching",
    "diarrhoea",
    "cough",
    "dark_urine",
    "irritability",
    "muscle_pain",
    "lethargy",
    "excessive_hunger",
    "weight_loss",
    "breathlessness",
    "swelled_lymph_nodes",
    "phlegm",
    "mild_fever",
    "blurred_and_distorted_vision",
    "loss_of_balance",
    "dizziness",
    "red_spots_over_body",
    "muscle_weakness",
    "swelling_joints",
    "neck_pain",
    "abnormal_menstruation",
    "fast_heart_rate",
    "indigestion",
    "painful_walking",
    "family_history",
    "continuous_sneezing",
    "stiff_neck",
    "constipation",
    "obesity",
    "mood_swings",
    "restlessness",
    "depression",
    "back_pain",
    "burning_micturition",
    "acidity"
];


// =========================
// DASHBOARD FEATURE SELECTOR
// =========================

const featureList = document.getElementById("featureList");
const selectedCount = document.getElementById("selectedCount");

const selectedFeaturesContainer = document.getElementById("selectedFeatures");

if (featureList) {

    features.forEach(function(feature) {

        const featureItem = document.createElement("div");

        featureItem.className = "feature-item";
        featureItem.textContent = feature;

        featureItem.addEventListener("click", function() {

            featureItem.classList.toggle("selected");

            const selectedFeatures = document.querySelectorAll(".feature-item.selected");

            selectedCount.textContent = selectedFeatures.length + " selected";


    // Update selected feature display

            selectedFeaturesContainer.innerHTML = "";

            if (selectedFeatures.length === 0) {

                    selectedFeaturesContainer.innerHTML = `
                        <p class="empty-message">
                            No features selected yet.
                        </p>
            `;

    } else {

        selectedFeatures.forEach(function(selectedFeature) {

            const chip = document.createElement("div");

            chip.className = "selected-feature";
            chip.textContent = selectedFeature.textContent;

            selectedFeaturesContainer.appendChild(chip);

        });

    }

    });

    });
}

// =========================
// LOGIN
// =========================

const loginForm = document.getElementById("LoginForm");

if (loginForm) {

    loginForm.addEventListener("submit", async function(event) {

        event.preventDefault();

        const username =
            document.getElementById("username").value.trim();

        const password =
            document.getElementById("password").value;

        const loginMessage =
            document.getElementById("loginMessage");

        loginMessage.textContent = "";

        try {

            const response = await fetch(
                "http://127.0.0.1:8000/login",
                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json"
                    },

                    body: JSON.stringify({
                        username: username,
                        password: password
                    })
                }
            );

            const data = await response.json();

            if (data.message === "Login successful") {

                window.location.href = "dashboard.html";

            } else {

                loginMessage.textContent =
                    "Invalid username or password.";

            }

        } catch (error) {

            loginMessage.textContent =
                "Unable to connect to the server.";

            console.error(error);

        }

    });

}

// =========================
// REGISTRATION
// =========================

const registerForm = document.getElementById("RegisterForm");

if (registerForm) {

    registerForm.addEventListener("submit", async function(event) {

        event.preventDefault();

        const username =
            document.getElementById("username").value.trim();

        const password =
            document.getElementById("password").value;

        const fullName =
            document.getElementById("full_name").value.trim();

        const email =
            document.getElementById("email").value.trim();

        const dob =
            document.getElementById("dob").value;

        const gender =
            document.getElementById("gender").value;

        const bloodType =
            document.getElementById("blood_type").value;

        const phoneNumber =
            document.getElementById("phone_number").value.trim();


        try {

            const response = await fetch(
                "http://127.0.0.1:8000/register",
                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json"
                    },

                    body: JSON.stringify({
                        username: username,
                        password: password,
                        full_name: fullName,
                        email: email,
                        dob: dob,
                        gender: gender,
                        blood_type: bloodType,
                        phone_number: phoneNumber
                    })
                }
            );

            const data = await response.json();

            if (response.ok) {

                alert("Account created successfully.");

                window.location.href = "login.html";

            } else {

                alert("Registration failed.");

                console.error(data);

            }

        } catch (error) {

            alert("Unable to connect to the server.");

            console.error(error);

        }

    });

}

// =========================
// REGISTRATION FORM
// =========================

const continueButton =
    document.getElementById("continueButton");

if (continueButton) {

    continueButton.addEventListener("click", function() {

        const username =
            document.getElementById("username").value.trim();

        const password =
            document.getElementById("password").value;

        if (username === "" || password === "") {

            alert("Please fill in all fields.");
            return;

        }

        if (/^\d+$/.test(username)) {

            alert("Username cannot contain only numbers.");
            return;

        }

        if (password.length < 8) {

            alert("Password must be at least 8 characters long.");
            return;

        }

        document.getElementById("accountDetails").style.display = "none";

        document.getElementById("importantDetails").style.display = "block";

    });

}