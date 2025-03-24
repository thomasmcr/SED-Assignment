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
}

//Display feedback to the user
function displayFeedback(input, valid, message="")
{
    const feedback = document.querySelector(`.invalid-feedback[data-for=${input.id}]`);
    input.classList.toggle("is-valid", valid);
    input.classList.toggle("is-invalid", !valid);
    if(feedback){ feedback.textContent = message; }
}

//Validate form inputs
function validate(name, description, quantity) {
    let isValid = true;

    // Validate name
    if (!name?.trim()) {
        displayFeedback(nameInput, false, "Name is required.");
        isValid = false;
    } else {
        displayFeedback(nameInput, true);
    }

    // Validate description
    if (!description?.trim()) {
        displayFeedback(descriptionInput, false, "Description is required.");
        isValid = false;
    } else {
        displayFeedback(descriptionInput, true);
    }

    // Validate quantity
    if (!quantity?.trim() || isNaN(quantity) || Number(quantity) <= 0) {
        displayFeedback(document.getElementById("input-quantity"), false, "Quantity must be a valid number greater than zero.");
        isValid = false;
    } else {
        displayFeedback(document.getElementById("input-quantity"), true);
    }

    return isValid;
}