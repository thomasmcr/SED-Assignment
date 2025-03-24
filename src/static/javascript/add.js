const alertWrapper = document.getElementById("add-alert-wrapper");
const nameInput = document.getElementById("input-name");
const descriptionInput = document.getElementById("input-description");

//Add item to database
async function addItem(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    const name = formData.get("name");
    const description = formData.get("description");
    const quantity = formData.get("quantity");

    if (!validate(name, description, quantity)) { return; }
    const token = sessionStorage.getItem("access_token");
    const headers = {
        "Content-Type": "application/json",
        ...(token && { "Authorization": `Bearer ${token}` })
    };
    try {
        const response = await fetch(`/item`, { 
            method: "POST", 
            headers: headers, 
            body: JSON.stringify({ name, description, quantity }) 
        });
        if (!response.ok) {
            const errorMessage = await response.text();
            insertAlert?.(`Error: ${response.status} - ${errorMessage}`, "danger", alertWrapper);
            return;
        }
        insertAlert?.("Successfully added item to database.", "success", alertWrapper);
    } catch (error) {
        console.error("An unexpected error occured: ", error);
        insertAlert?.(`Unexpected error: ${error.message}`, "danger", alertWrapper);
    }
}

//Display feedback to the user
function displayFeedback(input, valid, message = "") {
    const feedback = document.querySelector(`.invalid-feedback[data-for=${input.id}]`);
    input.classList.toggle("is-valid", valid);
    input.classList.toggle("is-invalid", !valid);
    if (feedback) { feedback.textContent = message; }
}

// Checks if a given string is entirely made of numbers
function isEntirelyNumeric(testString) {
    return /^\d+$/.test(testString);
}

//Validate form inputs
function validate(name, description, quantity) {
    let isValid = true;

    // Validate name
    if (!name?.trim()) {
        displayFeedback(nameInput, false, "Name is required.");
        isValid = false;
    }
    else if (isEntirelyNumeric(name)) {
        displayFeedback(nameInput, false, "Name cannot be entirely numeric.");
        isValid = false;
    }
    else {
        displayFeedback(nameInput, true);
    }

    // Validate description
    if (!description?.trim()) {
        displayFeedback(descriptionInput, false, "Description is required.");
        isValid = false;
    }
    else if (isEntirelyNumeric(description)) {
        displayFeedback(descriptionInput, false, "Description cannot be entirely numeric.");
        isValid = false;
    }
    else {
        displayFeedback(descriptionInput, true);
    }

    // Validate quantity
    if (!quantity || isNaN(quantity) || Number(quantity) <= 0) {
        displayFeedback(document.getElementById("input-quantity"), false, "Quantity must be a valid number greater than zero.");
        isValid = false;
    } else {
        displayFeedback(document.getElementById("input-quantity"), true);
    }

    return isValid;
}