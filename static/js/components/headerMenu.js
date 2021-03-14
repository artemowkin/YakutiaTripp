// Other

let switchCount = false;


// Header menu button and Smooth scroll for site menu 

let menuBtn = document.querySelector('.header__menuBtn');
let menu = document.querySelector('.header__nav');

function switchTranslateY(e) {
    switchCount === false ? $(menu).css('transform', 'translateY(60%)')
                            :
                            $(menu).css('transform', 'translateY(-500%)');

    switchCount = !switchCount;
}

menuBtn.addEventListener('click', switchTranslateY);

menuBtn.addEventListener('blur', e => {
    if (switchCount === true) {
        switchTranslateY();
    }
})

menu.addEventListener('click', e => {
    e.preventDefault();

    if (e.target.tagName != "A") return;

    let anchor = $(e.target).attr('href');

    $('html, body').stop().animate({
        scrollTop: $(anchor).offset().top - 80
    }, 500)
});
