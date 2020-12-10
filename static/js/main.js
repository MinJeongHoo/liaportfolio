'use strict'

const mainabout = document.querySelector("#main__about");
const header = document.querySelector('.header');
const closeMenu = document.querySelector(".fa-times");
const openMenu = document.querySelector(".fa-bars");
const navtoggle = document.querySelector(".nav__toggle");


openMenu.addEventListener('click', event => {
    navtoggle.setAttribute("style", "display:flex;");
});

closeMenu.addEventListener('click', event => {
    navtoggle.setAttribute("style", "display:none;");
});


window.addEventListener('scroll', (event) => {
    if (mainabout) {
        mainabout.setAttribute('style', 'visibility : visible; animation: imgFadeIn; animation-duration: 1s;');
    }
});

window.addEventListener('load', (event) => {
    const content = event.target.body.querySelector(".content");
    document.querySelector(".is-menuactive").classList.remove("is-menuactive");
    if (content.querySelector("#about")) {
        document.querySelector("#about-menu").classList.add("is-menuactive");
    }
    if (content.querySelector("#main__about")) {
        document.querySelector("#home-menu").classList.add("is-menuactive");
    }
    if (content.querySelector("#works")) {
        document.querySelector("#works-menu").classList.add("is-menuactive");
    }
    const info = document.querySelector(".works__info");
    info && info.addEventListener('contextmenu', function (e) {
        //here you draw your own menu
        e.preventDefault();
    }, false);
});

document.addEventListener('click', (event) => {
    const value = event.target.classList.value;
    if (value == "modal__form" || value == "modal__show") {
        closeModal();
    }
});

function openModal(object) {
    const modal = document.querySelector("#modal");
    const modalForm = document.querySelector(".modal__form");
    modalForm.innerHTML = "";
    let html = `
        <span class='closeBtn' onclick='closeModal()'>&times;</span>
        <img class='modal__img' src=${object.dataset.src}>
    <div class='modal__caption'><div>${object.dataset.title}</div>`

    if (object.dataset.title != "Drawing") {
        html += `<div>${object.dataset.material}</div>
        <div>${object.dataset.size}</div>
        <div>${object.dataset.year}</div>`
    }
    html += "</div>"
    modalForm.innerHTML = html;
    modal.classList.remove("modal__close");
    modal.classList.add("modal__show");
}

function closeModal() {
    const modal = document.querySelector("#modal");
    modal.classList.add("modal__close");
    modal.classList.remove("modal__show");
}

function menuactive(object) {
    const acitvemenu = document.querySelector(".is-menuactive");
    acitvemenu.classList.remove("is-menuactive");
    object.classList.add("is-menuactive");
}

