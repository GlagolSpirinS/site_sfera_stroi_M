document.addEventListener("DOMContentLoaded", function() {
    const carousel = document.querySelector(".carousel");
    const items = Array.from(document.querySelectorAll(".carousel-item"));
    const itemWidth = items[0].offsetWidth;
    const totalItems = items.length;
    let currentIndex = 0;
    let autoScrollInterval;

    // Дублируем элементы карусели для бесконечной прокрутки
    function duplicateItems() {
        const itemsFragment = document.createDocumentFragment();
        items.forEach(item => {
            const clone = item.cloneNode(true);
            itemsFragment.appendChild(clone);
        });
        carousel.appendChild(itemsFragment);
    }

    function updateCarousel() {
        const offset = -currentIndex * itemWidth;
        carousel.style.transform = `translateX(${offset}px)`;
        carousel.style.transition = 'transform 1s ease'; // Плавный переход
    }

    function startAutoScroll() {
        autoScrollInterval = setInterval(() => {
            currentIndex = (currentIndex + 1) % (totalItems * 2); // Двойной счетчик для бесконечной прокрутки
            updateCarousel();
        }, 5000); // Интервал в миллисекундах (5000 мс = 5 секунд)
    }

    function stopAutoScroll() {
        clearInterval(autoScrollInterval);
    }

    // Инициализация карусели
    duplicateItems(); // Дублируем элементы
    updateCarousel(); // Инициализация начального положения карусели
    startAutoScroll(); // Запуск автоматической прокрутки

    // Обработка событий
    carousel.addEventListener("mouseenter", stopAutoScroll); // Останавливаем авто-прокрутку при наведении
    carousel.addEventListener("mouseleave", startAutoScroll); // Запускаем авто-прокрутку при уходе курсора
});