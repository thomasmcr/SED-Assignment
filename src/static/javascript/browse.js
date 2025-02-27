const searchInput = document.getElementById("search");
const resultCount = document.getElementById("result-count"); 
const spinner = document.getElementById("spinner");
const alertWrapper = document.getElementById("alert-wrapper")

async function getItems(event) {
    if(event) event.preventDefault();
    setLoading(true);
    const searchQuery = searchInput.value; 
    try {
        const response = await fetch(`/item?query=${searchQuery}`);
        const data = await response.json();
        if (!response.ok) {
            throw new Error(`${data.detail} (Status: ${response.status})`);
        }
        populateTable(data);
    } catch (error) {
        console.error(error);
        insertAlert?.(error, "danger", alertWrapper)
    } finally {
        setLoading(false);
    }
}

function populateTable(items, clear=true) {
    const tableBody = document.getElementById("item-table");
    const plural = items.length > 1; 
    resultCount.innerHTML = `Found ${items.length} Result${plural ? "s" : ""}`
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

function setLoading(state) {
    spinner.style.visibility = state ? "visible" : "hidden";
}