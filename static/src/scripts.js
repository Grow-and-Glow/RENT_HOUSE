const Detail_img_accueil = document.getElementById('detail_img_accueil');
const images = document.querySelectorAll('.gallery-img');
const viewer = document.getElementById('viewer');
const mainImage = document.getElementById('mainImage');
const counter = document.getElementById('counter');
const precedenteBtn = document.getElementById('precBtn');
const suivanteBtn = document.getElementById('suivBtn');
const btnrtn = document.getElementById('rtnbtn')

let currentIndex = 0;

images.forEach((img, index) => {
    img.addEventListener('click', () => {
        currentIndex = index;
        openViewer();
    });
});

function openViewer() {
    mainImage.src = images[currentIndex].src;

    Detail_img_accueil.classList.remove('block');
    Detail_img_accueil.classList.add('hidden');
    viewer.classList.remove('hidden');
    
    counter.textContent = `${currentIndex + 1} / ${images.length}`;
    viewer.scrollIntoView({ behavior: 'smooth' });
}

function closeViewer(){
    viewer.classList.add('hidden');
    viewer.classList.remove('block');
    Detail_img_accueil.classList.remove('hidden');
    Detail_img_accueil.classList.add('block');

}

btnrtn.addEventListener("click", closeViewer);


suivanteBtn.addEventListener('click', () => {
    currentIndex = (currentIndex + 1) % images.length;
    mainImage.src = images[currentIndex].src;
    counter.textContent = `${currentIndex + 1} / ${images.length}`;
});

precedenteBtn.addEventListener('click', () => {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    mainImage.src = images[currentIndex].src;
    counter.textContent = `${currentIndex + 1} / ${images.length}`;
});