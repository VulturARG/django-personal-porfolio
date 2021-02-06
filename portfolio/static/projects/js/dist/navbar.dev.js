"use strict";

document.addEventListener("DOMContentLoaded", function () {
  var button = document.getElementById("menu-button");
  button.addEventListener("click", function () {
    var sidebar = document.getElementById("sidebar");
    if (sidebar.classList.contains('show-sidebar')) sidebar.classList = "sidebar";else sidebar.classList = "sidebar show-sidebar";
  });
});