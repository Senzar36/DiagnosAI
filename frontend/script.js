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