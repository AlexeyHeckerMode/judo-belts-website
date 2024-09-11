document.addEventListener("DOMContentLoaded", function() {
    const urlParams = new URLSearchParams(window.location.search);
    const beltId = urlParams.keys().next().value; // Get the first query string key

    if (!beltId) {
        console.error('No belt specified in the URL.');
        return;
    }

    fetch('data.json')
        .then(response => response.json())
        .then(data => {
            const belt = data.belts.find(b => b.id === beltId);

            if (belt) {
                // Determine the correct background style for the footer
                const footer = document.querySelector('footer');
                
                let style = document.createElement('style');
                style.type = 'text/css';
                
                if (belt.color.split(" ").length === 2) {
                    const colors = belt.color.split(" ");
                    const color1 = colors[0];
                    const color2 = colors[1];
                    console.log("Two colors detected:", color1, color2);
                    
                    style.innerHTML = `
                        footer.second-color::before {
                            background: linear-gradient(45deg, ${color1}, ${color2});
                        }
                    `;
                    footer.className = 'second-color';
                } else {
                    const color = belt.color;
                    console.log("Single color detected:", color);
                    
                    style.innerHTML = `
                        footer.first-color::before {
                            background-color: ${color};
                        }
                    `;
                    footer.className = 'first-color';
                }
                
                document.head.appendChild(style);
                
                // Apply the footer image if present
                if (belt.footerImage) {
                    footer.style.backgroundImage = `url(${belt.footerImage})`;
                }

                // Update the belt image in the footer
                const beltImage = document.getElementById('beltImage');
                beltImage.url = belt.beltImage;
                beltImage.alt = `${belt.name} Image`;

                // Update the belt name
                document.querySelector('h1').textContent = `${belt.name} - Techniques`;

                const container = document.getElementById('beltList');

                for (const [category, techniques] of Object.entries(belt.techniques)) {
                    const categoryTitle = document.createElement('h2');
                    categoryTitle.textContent = category;
                    categoryTitle.classList.add('technique-category');  // Add class to the category title
                    container.appendChild(categoryTitle);

                    techniques.forEach(technique => {
                        const techniqueContainer = document.createElement('div');
                        techniqueContainer.className = 'technique-container';  // Add class to each technique container
                        techniqueContainer.innerHTML = `
                            <a href="${technique.link}" class="technique-link">  <!-- Add class to the link -->
                                <img src="${technique.image}" alt="${technique.name}" class="technique-image">
                                <div class="technique-content">
                                    <p>${technique.name}</p>
                                </div>
                            </a>
                        `;
                        container.appendChild(techniqueContainer);
                    });
                }
            } else {
                console.error('Belt not found');
            }
        })
        .catch(error => console.error('Error loading data:', error));
});
