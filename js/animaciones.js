//general constructor
const $ = (selector) => document.querySelector(selector) 
const $$ = (selector) => document.querySelectorAll(selector) 

document.addEventListener("DOMContentLoaded", function() {
    var animacionDivs = $$(".animacion-div");
    
    animacionDivs.forEach(function(container) {
        container.classList.add("loaded"); 
    });
});

document.addEventListener("DOMContentLoaded", function() {
    var sideAppearDiv = $(".side-appear");
    sideAppearDiv.classList.add("show");
});