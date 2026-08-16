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

    var username = document.getElementById("username").value.trim();
    var password = document.getElementById("password").value.trim();

    if (username === "" || password === "") {
        alert("Please fill in all fields.");
        return false;
    }

    if (/^\d+$/.test(username)) {
        alert("Username cannot contain only numbers.");
        return false;
    }

    if (password.length < 8) {
        alert("Password must be at least 8 characters long.");
        return false;
    }

    return true;
}


function register_form_display() {

    document.getElementById("continueButton").addEventListener("click", function() {

        if (register_validate()) {

            document.getElementById("accountDetails").style.display = "none";

            document.getElementById("importantDetails").style.display = "block";
        }

    });
}

register_form_display();