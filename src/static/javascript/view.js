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

    const confirmUpdate = await Swal.fire({
        title: "Are you sure?",
        text: "Are you sure you want to update this item?",
        icon: "warning",
        showCancelButton: true, 
        confirmButtonText: "Yes, update it",
        showCancelButton: "No, I've changed my mind"
    });
    if(!confirmUpdate.isConfirmed){ return; }

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

async function deleteItem(id, old_location)
{
    const confirmUpdate = await Swal.fire({
        title: "Are you sure?",
        text: "Are you sure you want to delete this item? this cannot be undone",
        icon: "warning",
        showCancelButton: true, 
        confirmButtonText: "Yes, delete it",
        showCancelButton: "No, I've changed my mind"
    });
    if(!confirmUpdate.isConfirmed){ return; }

    const token = sessionStorage.getItem("access_token");
    const headers = {
        "Content-Type": "application/json",
        ...(token && { "Authorization": `Bearer ${token}` })
    };
    try {
        const response = await fetch(`/item?id=${id}`, { 
            method: "DELETE", 
            headers: headers
        });
        if (!response.ok) {
            const errorMessage = await response.text();
            insertAlert?.(`Error: ${response.status} - ${errorMessage}`, "danger", alertWrapper);
            return;
        }
        location.replace(old_location);
    } catch (error) {
        console.error("An unexpected error occured: ", error);
        insertAlert?.(`Unexpected error: ${error.message}`, "danger", alertWrapper);
    }
}