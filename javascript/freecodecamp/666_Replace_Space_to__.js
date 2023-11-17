// Помогатор с именованием.

title = "Understanding Uninitialized Variables";

console.log(newTitle(title));

function newTitle(str) {
    return str.split(" ").join("_")
}
