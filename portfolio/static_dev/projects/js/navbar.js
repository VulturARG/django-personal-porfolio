document.addEventListener("DOMContentLoaded", function() {
    let button = document.getElementById("menu-button");

    button.addEventListener("click", function() {
        let sidebar = document.getElementById("sidebar");
        
        if(sidebar.classList.contains('show-sidebar'))
            sidebar.classList = "sidebar";
        else
            sidebar.classList = "sidebar show-sidebar";
    });
});