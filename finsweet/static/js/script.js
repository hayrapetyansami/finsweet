"use strict";

window.addEventListener("load", () => {
  const mobileMenuBtn = document.querySelector("#burger-menu");
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

  try {
    new Swiper(".testimonials-slider", {
      loop: true,
      autoplay: {
        delay: 2500,
        disableOnInteraction: false,
      }
    });
  } catch {}
});