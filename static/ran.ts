document.addEventListener('DOMContentLoaded', () => {
    const startCounterElement = document.getElementById('startCounter') as HTMLInputElement;
    const startCounter = startCounterElement ? parseInt(startCounterElement.value) : 0;

    if (startCounter === 1) {
        // Obtener todos los elementos que deseas reorganizar
        let elements: NodeListOf<Element> = document.querySelectorAll('.marco');

        // Crear una lista de índices
        let indices: number[] = [...Array(elements.length)].map((_, i) => i);

        // Mezclar aleatoriamente la lista de índices
        for (let i: number = indices.length - 1; i > 0; i--) {
            let j: number = Math.floor(Math.random() * (i + 1));
            [indices[i], indices[j]] = [indices[j], indices[i]];
        }

        // Reorganizar los elementos en el orden especificado por la lista mezclada
        let parentElement: Node | null = elements[0].parentNode;
        indices.forEach(i => {
            if (parentElement) {
                parentElement.appendChild(elements[i]);
            }
        });

        // Almacenar el orden de los elementos en una variable de sesión
        sessionStorage.setItem('indices', JSON.stringify(indices));
    }
});