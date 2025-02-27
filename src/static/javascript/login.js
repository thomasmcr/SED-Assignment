async function handleLogin(event)
{
    if(event) event.preventDefault();
    const formData = new FormData(event.target); 
    const response = await fetch("/token", {
        method: "POST",
        body: formData
    });
    const data = await response.json();
    if (data.access_token) {
        sessionStorage.setItem("token", data.access_token); 
    } else {
        console.error("Login failed");
    }
}
