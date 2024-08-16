const modal = document.querySelector('#modal');
const close = document.querySelector('.close');

function openModal(jobId) {
    // Заполняем содержимое модального окна
    document.querySelector('#modal-body').innerHTML = `
        <form method="post" action="{% url 'apply_for_job' '${jobId}' %}">
            {% csrf_token %}
            <textarea name="cover_letter" placeholder="Ваше сопроводительное письмо"></textarea>
            <button type="submit" class="submit-button">Отправить</button>
        </form>
    `;
    modal.style.display = 'block';
}

close.onclick = function () {
    modal.style.display = 'none';
};

window.onclick = function (event) {
    if (event.target === modal) {
        modal.style.display = 'none';
    }
};