fetch(dataUrl)
    .then(response => response.json())
    .then(data => {
        console.log('Fetched data:', data); // Debugging statement
        console.log('Selected technique:', selectedTechnique); // Debugging statement

        const techniqueData = data.find(item => normalizeString(item.title) === selectedTechnique);
        console.log('Found technique data:', techniqueData); // Debugging statement
        
        if (techniqueData) {
            // Your existing code to generate HTML content
        } else {
            container.innerHTML = '<p>Technique not found.</p>';
        }
    })
    .catch(error => console.error('Error fetching data:', error)); // Catch and log any fetch errors
