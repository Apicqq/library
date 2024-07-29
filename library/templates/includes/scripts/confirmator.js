const buttons = document.querySelectorAll("button#copy-button");
buttons.forEach(button => {
    button.addEventListener("click", function () {
        this.textContent = "Готово!";
        setTimeout(() => {
            this.textContent = "Копировать";
        }, 2000);
    });
})