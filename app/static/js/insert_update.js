// Counter for field set IDs
let fieldSetId = 1;

// Function to add new field set
function addNewField() {
     // Select the first field set to clone
     const fieldSet = document.querySelector('.field-set');

     // Clone the selected field set
     const newFieldSet = fieldSet.cloneNode(true);
 
     // Get all input fields in the cloned field set
     const inputs = newFieldSet.querySelectorAll('input');
 
     // Update the IDs and clear values for new input fields
     inputs.forEach((input) => {
         if (input.type === 'text') {
             input.value = ''; // Clear value
         }
         
         if (input.id) {
             const idParts = input.id.split('-');
             const baseId = idParts.slice(0, -1).join('-');
             const newId = `${baseId}-${Date.now()}`; // Use a unique ID
             input.id = newId;
             input.setAttribute('id', newId);
         }
     });
 
     // Append the cloned field set to the container
     document.querySelector('.dynamic-fields').appendChild(newFieldSet);
}
