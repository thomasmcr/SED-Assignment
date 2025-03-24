function handleLogout()
{
   fetch("/logout", { method: "POST" }).then(response => {
        if (response.ok) {
            sessionStorage.clear(); 
            location.reload();
        }
    });
}