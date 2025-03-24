const loginAlertWrapper = document.getElementById("login-alert-wrapper")

async function handleLogin(event, path) {
    if(event) event.preventDefault();
    const formData = new FormData(event.target); 
    //TODO: validate input
    try {
        const response = await fetch("/token", { method: "POST",  body: formData });
        const data = await response.json();
        if (!response.ok) { 
            throw new Error(`${data.detail} (Status: ${response.status})`);
        }
        else { 
            console.log(data);
            sessionStorage.setItem("access_token", data.access_token);
            location.replace(path); //Reload the page on success
        }
    } catch (error) {
        console.error(error);
        insertAlert?.(error, "danger", loginAlertWrapper);
    } 
}
