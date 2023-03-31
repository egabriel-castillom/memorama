var tiempoRestante = Number(localStorage.getItem('tiempoRestante')) || 60; // 60 segundos
var elementoCuentaRegresiva = document.getElementById('cuenta-regresiva');
var actualizarCuentaRegresiva = function () {
    if (elementoCuentaRegresiva) {
        elementoCuentaRegresiva.textContent = "".concat(tiempoRestante, " segundos restantes");
    }
    tiempoRestante -= 1;
    if (tiempoRestante === 0) {
        tiempoRestante = 60;
    }
    localStorage.setItem('tiempoRestante', tiempoRestante.toString());
    if (tiempoRestante >= 0) {
        setTimeout(actualizarCuentaRegresiva, 1000);
    }
};
actualizarCuentaRegresiva();
