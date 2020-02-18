const HamBurgerIconClick = () => {
    var navMenu = document.getElementById("nav-menu");
    var hamIcon1 = document.getElementById("ham-icon-1");
    var hamIcon2 = document.getElementById("ham-icon-2");
    var hamIcon3 = document.getElementById("ham-icon-3");
    if (hamIcon1.classList.contains("ham-icon-1-anim")){
        hamIcon1.classList.add("ham-icon-1-anim-remove");
        hamIcon2.classList.add("ham-icon-2-anim-remove");
        hamIcon3.classList.add("ham-icon-3-anim-remove");
        navMenu.classList.add("nav-menu-anim-remove");
        document.body.style.setProperty('--scroll', "scroll");
        setTimeout(() => {
            navMenu.classList.add("none");
            navMenu.classList.remove("nav-menu-anim-remove");
            hamIcon1.classList.remove("ham-icon-1-anim-remove");
            hamIcon2.classList.remove("ham-icon-2-anim-remove");
            hamIcon3.classList.remove("ham-icon-3-anim-remove");
            hamIcon1.classList.remove("ham-icon-1-anim");
            hamIcon2.classList.remove("ham-icon-2-anim");
            hamIcon3.classList.remove("ham-icon-3-anim");
        }, 500);
    }
    else{
        navMenu.classList.remove("none");
        hamIcon1.classList.add("ham-icon-1-anim");
        hamIcon2.classList.add("ham-icon-2-anim");
        hamIcon3.classList.add("ham-icon-3-anim");
        document.body.style.setProperty('--scroll', "hidden");
    }
}