document.addEventListener("DOMContentLoaded", function() {
    const carousel = document.querySelector(".carousel");
    const items = Array.from(document.querySelectorAll(".carousel-item"));
    const isMobile = window.innerWidth <= 768;

    if (!isMobile) {
        carousel.style.overflow = 'hidden';
        carousel.style.whiteSpace = 'nowrap';
        carousel.style.display = 'flex';
        carousel.style.flexWrap = 'nowrap';

        // items.forEach(item => {
        //     item.style.display = 'inline-block';
        // });

        // Обработка прокрутки колесика мыши
        carousel.addEventListener('wheel', (e) => {
            e.preventDefault();
            carousel.scrollLeft += e.deltaY; // Используем deltaY для прокрутки
        });

        // Вычисление ширины элемента
        const itemWidth = items[0].offsetWidth;

        // Функция обновления карусели
        function updateCarousel() {
            const offset = -currentIndex * itemWidth;
            carousel.style.transform = `translateX(${offset}px)`;
            carousel.style.transition = 'transform 1s ease';
        }

        // Переменная текущего индекса
        let currentIndex = 0;

        updateCarousel();
        startAutoScroll();
    }
});