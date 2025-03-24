
//Display form feedback to the user
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

// Validate form inputs
function validate(nameInput, descriptionInput, quantityInput) {
    let isValid = true;

    // Extract values from the input elements
    const name = nameInput?.value?.trim();
    const description = descriptionInput?.value?.trim();
    const quantity = quantityInput?.value;

    // Validate name
    if (!name) {
        displayFeedback?.(nameInput, false, "Name is required.");
        isValid = false;
    } else if (isEntirelyNumeric(name)) {
        displayFeedback?.(nameInput, false, "Name cannot be entirely numeric.");
        isValid = false;
    } else {
        displayFeedback?.(nameInput, true);
    }

    // Validate description
    if (!description) {
        displayFeedback?.(descriptionInput, false, "Description is required.");
        isValid = false;
    } else if (isEntirelyNumeric(description)) {
        displayFeedback?.(descriptionInput, false, "Description cannot be entirely numeric.");
        isValid = false;
    } else {
        displayFeedback?.(descriptionInput, true);
    }

    // Validate quantity
    if (!quantity || isNaN(quantity) || Number(quantity) <= 0) {
        displayFeedback?.(quantityInput, false, "Quantity must be a valid number greater than zero.");
        isValid = false;
    } else {
        displayFeedback?.(quantityInput, true);
    }

    return isValid;
}