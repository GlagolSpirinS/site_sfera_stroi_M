// Получаем модальное окно
var modal = document.getElementById("myModal");

// Получаем изображение внутри модального окна
var modalImg = document.getElementById("img01");

// Получаем элемент <span> для закрытия окна
var span = document.getElementsByClassName("close")[0];

// При клике на изображение галереи показываем его в модальном окне
var images = document.getElementsByClassName('gallery-image');
for (var i = 0; i < images.length; i++) {
    images[i].onclick = function() {
        modal.style.display = "flex"; // Делаем модальное окно видимым и центрированным
        modalImg.src = this.src; // Устанавливаем источник изображения в модальном окне
        modalImg.alt = this.alt; // Копируем альтернативный текст (необязательно)
    }
}

// Закрываем модальное окно при клике на <span>
span.onclick = function() {
    modal.style.display = "none"; // Скрываем модальное окно
}

// Закрываем модальное окно при клике вне изображения
modal.onclick = function(event) {
    if (event.target === modal) {
        modal.style.display = "none"; // Скрываем модальное окно, если клик был вне изображения
    }
}
