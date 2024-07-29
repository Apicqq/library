const buttons = document.querySelectorAll("button#copy-button");
buttons.forEach(button => {
    button.addEventListener("click", function () {
        this.textContent = "Готово!";
        setTimeout(() => {
            this.textContent = "Скопировать название";
        }, 2000);
    });
})