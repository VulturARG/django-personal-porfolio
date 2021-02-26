document.addEventListener("DOMContentLoaded", function() {
    let button = document.getElementById("menu-button");

    button.addEventListener("click", function() {
        let sidebar = document.getElementById("sidebar");
        let icon = document.getElementById('fas');
        
        if(sidebar.classList.contains('show-sidebar')){
            sidebar.classList = "sidebar";
            icon.classList.replace('fa-times','fa-bars');
        } else {
            sidebar.classList = "sidebar show-sidebar";
            icon.classList.replace('fa-bars', 'fa-times');
        }
    });
});