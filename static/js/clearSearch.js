let search = document.querySelector("input[type='text']");
let clearSearch = document.querySelector(".clear-search");
if (search.value.trim().length > 0) {
  clearSearch.style.opacity = 1;
  console.log("r");
  clearSearch.style.pointerEvents = "all";
} else {
  clearSearch.style.opacity = 0;
  clearSearch.style.pointerEvents = "none";
}
search.addEventListener("input", () => {
  if (search.value.trim().length > 0) {
    clearSearch.style.opacity = 1;
    console.log("r");
    clearSearch.style.pointerEvents = "all";
  }
});