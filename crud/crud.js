const bookForm = document.getElementById('bookForm');
const bookList = document.getElementById('bookList');

let books = [];

function renderBookList() {
  bookList.innerHTML = '';
  books.forEach((book, index) => {
    const listItem = document.createElement('div');
    listItem.className = 'book-item';
    listItem.innerHTML = `
      <span>${book.bookTitle} - ${book.borrowerName}</span>
      <button onclick="editBook(${index})">Editar</button>
      <button onclick="deleteBook(${index})">Excluir</button>
    `;
    bookList.appendChild(listItem);
  });
}

function addBook(event) {
  event.preventDefault();
  const bookTitle = document.getElementById('bookTitle').value;
  const borrowerName = document.getElementById('borrowerName').value;
  books.push({ bookTitle, borrowerName });
  renderBookList();
  bookForm.reset();
}

function editBook(index) {
  const newTitle = prompt('Digite o novo título do livro:');
  const newName = prompt('Digite o novo nome do tomador:');
  if (newTitle !== null && newName !== null) {
    books[index].bookTitle = newTitle;
    books[index].borrowerName = newName;
    renderBookList();
  }
}

function deleteBook(index) {
  const confirmDelete = confirm('Tem certeza de que deseja excluir este registro?');
  if (confirmDelete) {
    books.splice(index, 1);
    renderBookList();
  }
}

bookForm.addEventListener('submit', addBook);
