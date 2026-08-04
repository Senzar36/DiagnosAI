function login_validate() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    let flag = false;

    if (username === "" || password === "") {
        alert("Please fill in all fields.");
        flag = true;
    }

    if (!isNaN(username) || !isNaN(password)) {
        alert("Please enter valid credentials.");
        flag = true;
    }

    if (flag) {
        return false;
    }
    
    return true;
}

function post_validate() {
    if (login_validate()) {
        window.location.href = "main.html";
    }
}

function register_validate() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    let flag = false;

    if (username === "" || password === "") {
        alert("Please fill in all fields.");
        flag = true;
    }

    if (!isNaN(username) || !isNaN(password)) {
        alert("Please enter valid credentials.");
        flag = true;
    }

    if (flag) {
        alert("Registration failed. Please try again.");
        return false;
    }

    return true;
}

function patient_data_display() {
}