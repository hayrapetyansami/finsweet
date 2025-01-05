"use strict";

window.addEventListener("load", () => {
  const mobileMenuBtn = document.querySelector(".mobile__menu-btn");
  const menu = document.querySelector(".menu");

  mobileMenuBtn.addEventListener("click", function () {
    if (this.classList.contains("active")) {
      this.classList.remove("active");
      menu.classList.remove("menu__active");
    } else {
      this.classList.add("active");
      menu.classList.add("menu__active");
    }
  });
});