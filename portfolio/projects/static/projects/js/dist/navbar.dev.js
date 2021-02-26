"use strict";

document.addEventListener("DOMContentLoaded", function () {
  var button = document.getElementById("menu-button");
  button.addEventListener("click", function () {
    var sidebar = document.getElementById("sidebar");
    var icon = document.getElementById('fas');

    if (sidebar.classList.contains('show-sidebar')) {
      sidebar.classList = "sidebar";
      icon.classList.replace('fa-times', 'fa-bars');
    } else {
      sidebar.classList = "sidebar show-sidebar";
      icon.classList.replace('fa-bars', 'fa-times');
    }
  });
});