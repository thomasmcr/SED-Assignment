const alertWrapper = document.getElementById("add-alert-wrapper");
const nameInput = document.getElementById("input-name");
const descriptionInput = document.getElementById("input-description");
const quantityInput = document.getElementById("input-quantity");

//Add item to database
async function addItem(event) {
    event.preventDefault();

    if (!validate(nameInput, descriptionInput, quantityInput)) { return; }
    
    const name = nameInput.value
    const description = descriptionInput.value;
    const quantity = quantityInput.value; 

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