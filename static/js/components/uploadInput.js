// Upload Input Component

let uploadInput = document.querySelector('.uploadInput');

uploadInput.addEventListener('change', (e) => {
    let title = document.querySelector('.uploadInput__title');
    let fileName = e.target.files[0].name;

    if (fileName.length > 25) {
        title.innerHTML = fileName.slice(0, 30) + "...";
        return;
    }

    title.innerHTML = fileName;
});