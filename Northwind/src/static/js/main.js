function confirmDelete() {
    const ok = confirm("Are you sure?");
    if (!ok) event.preventDefault();
}


// Finds element by css:
const errorSpan = document.querySelector(".error");
if(errorSpan) {
    setTimeout(() => {
        errorSpan.parentNode.removeChild(errorSpan);
    }, 4000);
}


// console.log(window.location.pathname);

