def generate_script_js(directory_path):
    js_code = f'''document.addEventListener('DOMContentLoaded', function() {{

    let deleteButtons = document.querySelectorAll('.delete-button');
    deleteButtons.forEach(function(button) {{
        button.addEventListener('click', function() {{
            let imageId = button.getAttribute('data-image-id');

            // Ask for confirmation
            let confirmation = confirm('Voulez-vous vraimetn supprimer cette image ?');
            if (confirmation) {{
                // User clicked "OK" in the confirmation dialog, proceed with deletion
                let xhr = new XMLHttpRequest();
                xhr.onreadystatechange = function() {{
                    if (xhr.readyState === 4 && xhr.status === 200) {{
                        // Image deleted successfully, remove the image from the page
                        let imageBox = button.closest('.image-box');
                        imageBox.remove();
                    }} else if (xhr.readyState === 4) {{
                        // Handle error if needed
                        console.error("Impossible de supprimer l'image.");
                    }}
                }};

                xhr.open('POST', 'requires/delete_image.php', true);
                xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
                xhr.send('image_id=' + imageId);
            }} else {{
                // User clicked "Cancel" in the confirmation dialog, do nothing
            }}
        }});
    }});


    const editButtons = document.querySelectorAll('.edit-button');
    
    editButtons.forEach(function(button) {{
        button.addEventListener('click', function() {{
            const imageId = button.getAttribute('data-image-id');
            const legendElement = document.querySelector('#legend-' + imageId);
            console.log("image id : " + imageId);
            const editContainer = document.querySelector(`#edit-container-${{imageId}}`);

            // Toggle the display of the edit container
            if (editContainer.style.display === 'none') {{
                editContainer.style.display = 'block';
            }} else {{
                editContainer.style.display = 'none';
            }}

            // Handle "Save" button click
            const saveButton = document.querySelector('#save-button-' + imageId);
            saveButton.addEventListener('click', function() {{
                const editedLegend = document.querySelector('#edited-legend-' + imageId).value;
                // Send an AJAX request to update the database with the edited legend
                const xhr = new XMLHttpRequest();
                xhr.onreadystatechange = function() {{
                    if (xhr.readyState === 4 && xhr.status === 200) {{
                        // Update the legend element with the edited value
                        legendElement.textContent = editedLegend;
                        // Hide the edit container
                        const editContainer = document.querySelector(`#edit-container-${{imageId}}`);
                        editContainer.style.display = 'none';
                    }} else if (xhr.readyState === 4) {{
                        // Handle error if needed
                        console.error("Impossible d'éditer la légende");
                    }}
                }};

                // Prepare data for the AJAX request
                const data = new FormData();
                data.append('image_id', imageId);
                data.append('legend', editedLegend);

                // Send a POST request to update_legend.php
                xhr.open('POST', 'requires/update_legend.php', true);
                xhr.send(data);
            }});

            const cancelButton = document.querySelector('#cancel-button-' + imageId);
            cancelButton.addEventListener('click', function() {{
                editContainer.style.display = 'none';
            }})

        }});
    }});
}});
'''

    with open(f"{directory_path}/gallery/js/script.js", "w") as js_file:
        js_file.write(js_code)
