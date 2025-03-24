const viewCard = document.getElementById("view-card");
const editCard = document.getElementById("edit-card");
const alertWrapper = document.getElementById("view-alert-wrapper");
const nameInput = document.getElementById("input-name");
const descriptionInput = document.getElementById("input-description");
const quantityInput = document.getElementById("input-quantity");

function toggleEdit()
{
    viewCard.style.display = "none";
    editCard.style.display = "block";
}

async function updateItem(event, id)
{
    event.preventDefault();
    if(!validate(nameInput, descriptionInput, quantityInput)){ return; }

    const name = nameInput.value;
    const description = descriptionInput.value;
    const quantity = quantityInput.value;

    const token = sessionStorage.getItem("access_token");
    const headers = {
        "Content-Type": "application/json",
        ...(token && { "Authorization": `Bearer ${token}` })
    };
    try {
        const response = await fetch(`/item`, { 
            method: "PUT", 
            headers: headers, 
            body: JSON.stringify({ id, name, description, quantity }) 
        });
        if (!response.ok) {
            const errorMessage = await response.text();
            insertAlert?.(`Error: ${response.status} - ${errorMessage}`, "danger", alertWrapper);
            return;
        }
        location.reload();
    } catch (error) {
        console.error("An unexpected error occured: ", error);
        insertAlert?.(`Unexpected error: ${error.message}`, "danger", alertWrapper);
    }
}