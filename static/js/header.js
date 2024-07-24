document.addEventListener("DOMContentLoaded", function() {
    const carousel = document.querySelector(".carousel");
    const prevBtn = document.getElementById("prevBtn");
    const nextBtn = document.getElementById("nextBtn");
    const items = document.querySelectorAll(".carousel-item");
    const itemWidth = items[0].offsetWidth;
    const itemsVisible = 3;
    const totalItems = items.length;
    let currentIndex = 0;

    function updateCarousel() {
        const offset = -currentIndex * itemWidth;
        carousel.style.transform = `translateX(${offset}px)`;
    }

    prevBtn.addEventListener("click", function() {
        if (currentIndex > 0) {
            currentIndex--;
            updateCarousel();
        }
    });

    nextBtn.addEventListener("click", function() {
        if (currentIndex < totalItems - itemsVisible) {
            currentIndex++;
            updateCarousel();
        }
    });

    updateCarousel(); // Инициализация начального положения карусели
});
