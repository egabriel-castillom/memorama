document.addEventListener('DOMContentLoaded', () => {
    if (sessionStorage.getItem('indices')) {
        let elements: NodeListOf<Element> = document.querySelectorAll('.marco');
        let parent: Node = elements[0].parentNode;
        let indices: number[] = JSON.parse(sessionStorage.getItem('indices'));
        indices.forEach(i => parent.appendChild(elements[i]));
    }
});