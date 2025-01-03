
let fieldCount = 1;

function addFields() {
    fieldCount++;
    const dynamicFields = document.getElementById("dynamic-fields");

    // Create a new div for the set of inputs
    const newDiv = document.createElement("div");
    newDiv.classList.add("same-line");

    // Create the Title label and input
    const titleLabel = document.createElement("label");
    titleLabel.setAttribute("for", `title-name-${fieldCount}`);
    titleLabel.textContent = "Title";
    newDiv.appendChild(titleLabel);

    const titleInput = document.createElement("input");
    titleInput.setAttribute("list", "titles");
    titleInput.setAttribute("name", "title[]");
    titleInput.setAttribute("id", `title-name-${fieldCount}`);
    newDiv.appendChild(titleInput);

    // Create the Value label and input

    // Append the new div to the dynamic fields section
    dynamicFields.insertBefore(newDiv, dynamicFields.querySelector("#add-btn"));
}

function toggleFields(isChecked) {
    const inputs = document.querySelectorAll("#dynamic-fields input");
    const addButton = document.getElementById("add-btn");

    inputs.forEach(input => {
        if (isChecked) {
            input.style.transition = "opacity 0.5s ease, background-color 0.5s ease";
            input.style.opacity = "0.5"; // Dim the input field
            input.style.backgroundColor = "#f8d7da"; // Light red background
            input.disabled = true;
        } else {
            input.style.opacity = "1"; // Reset opacity
            input.style.backgroundColor = ""; // Reset background color
            input.disabled = false;
        }
    });

    // Apply visual feedback to the add button
    if (isChecked) {
        addButton.style.transition = "opacity 0.5s ease, background-color 0.5s ease";
        addButton.style.opacity = "0.5"; // Dim the button
        addButton.style.backgroundColor = "#f8d7da"; // Light red background
        addButton.disabled = true;
    } else {
        addButton.style.opacity = "1"; // Reset opacity
        addButton.style.backgroundColor = ""; // Reset background color
        addButton.disabled = false;
    }
}

    