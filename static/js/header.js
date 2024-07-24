document.addEventListener("DOMContentLoaded", function() {
    const carousel = document.querySelector(".carousel");
    const items = document.querySelectorAll(".carousel-item");
    const itemWidth = items[0].offsetWidth;
    const itemsVisible = 3;
    const totalItems = items.length;
    let currentIndex = 0;

    function updateCarousel() {
        const offset = -currentIndex * itemWidth;
        carousel.style.transform = `translateX(${offset}px)`;
    }

    carousel.addEventListener("wheel", function(event) {
        if (event.deltaY > 0) {
            if (currentIndex < totalItems - itemsVisible) {
                currentIndex++;
                updateCarousel();
            }
        } else {
            if (currentIndex > 0) {
                currentIndex--;
                updateCarousel();
            }
        }
    });

    updateCarousel(); // Инициализация начального положения карусели
});