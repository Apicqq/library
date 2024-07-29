const _buttons = document.getElementsByClassName('btn btn-outline-secondary');
for (let i = 0; i < _buttons.length; i++) {
    _buttons[i].addEventListener('click', function () {
        const cardTitle = this.parentNode.parentNode.querySelector('.card-title').innerHTML;
        navigator.clipboard.writeText(cardTitle);
    });
}