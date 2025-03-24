const searchInput = document.getElementById("search");
const resultCount = document.getElementById("result-count"); 
const spinner = document.getElementById("browse-spinner");
const alertWrapper = document.getElementById("browse-alert-wrapper")

//Get items from the database 
async function getItems(event) {
    if(event) event.preventDefault();
    setLoading(true);
    const searchQuery = searchInput.value; 
    const token = sessionStorage.getItem("access_token");
    const headers = {
        "Content-Type": "application/json",
        ...(token && { "Authorization": `Bearer ${token}` })
    };
    try {
        const response = await fetch(`/item?query=${searchQuery}`, {method: "GET", headers: headers});
        if (!response.ok) {
            const errorMessage = await response.text();
            insertAlert?.(`Error: ${response.status} - ${errorMessage}`, "danger", alertWrapper);
            return;
        }
        const data = await response.json();
        populateTable(data, searchQuery);
    } catch (error) {
        console.error("An unexpected error occured: ", error);
        insertAlert?.(`Unexpected error: ${error.message}`, "danger", alertWrapper);
    } finally {
        setLoading(false);
    }
}

//Populate table with the given array of items
function populateTable(items, searchQuery="", clear=true) {
    const tableBody = document.getElementById("item-table");
    const plural = items.length > 1; 
    resultCount.innerHTML = `Found ${items.length} result${plural ? "s" : ""} ${searchQuery ? `for "${searchQuery}"` : ""}`;
    if(clear){ tableBody.innerHTML = ""; }
    items.forEach(item => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <th scope="row">${item.id}</th>
            <td>${item.name}</td>
            <td>${item.description}</td>
            <td>${item.quantity}</td>
        `;
        tableBody.appendChild(row);
    });
}

//Toggle loading
function setLoading(state) {
    spinner.style.visibility = state ? "visible" : "hidden";
}