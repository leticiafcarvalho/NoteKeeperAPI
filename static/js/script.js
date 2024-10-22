document.getElementById('noteForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const title = document.getElementById('title').value;
    const content = document.getElementById('content').value;

    const response = await fetch('/notes', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title, content })
    });

    const feedback = document.getElementById('feedback');
    if (response.ok) {
        feedback.className = 'alert alert-success';  // Estilo de sucesso
        feedback.textContent = 'Nota criada com sucesso!';
        feedback.style.display = 'block';

        // Limpa os campos do formulário
        document.getElementById('title').value = '';
        document.getElementById('content').value = '';

        // Atualiza a lista de notas
        loadNotes();
    } else {
        feedback.className = 'alert alert-danger';  // Estilo de erro
        feedback.textContent = 'Erro ao criar nota.';
        feedback.style.display = 'block';
    }
});

async function loadNotes() {
    const response = await fetch('/notes');
    const notes = await response.json();
    const notesList = document.getElementById('notesList');
    notesList.innerHTML = '';

    notes.forEach(note => {
        const noteDiv = document.createElement('div');
        noteDiv.className = 'list-group-item list-group-item-action';  // Estilo do Bootstrap
        noteDiv.textContent = `${note.title}: ${note.content}`;
        notesList.appendChild(noteDiv);
    });
}

// Carrega as notas ao iniciar
loadNotes();
