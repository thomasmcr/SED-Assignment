function insertAlert(message, type, wrapper)
{
    const hasExistingAlert = wrapper.innerHTML.trim() !== ""; 
    const alertHTML = `
        <div class="alert alert-${type} alert-dismissible ${hasExistingAlert ? "pulse" : ""}" role="alert" style="display: flex; align-items: center">
        <i class="bi bi-exclamation-triangle-fill" style="margin-right: 1rem"></i>
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
    `;
    wrapper.innerHTML = alertHTML;
}