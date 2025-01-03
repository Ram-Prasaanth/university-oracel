
            let searchEntryCount = 0;
            let sortEntryCount = 0;

            function addSearchEntry() {
                const container = document.getElementById('search-container');
                const entry = document.querySelector('.search-entry');
                const clone = entry.cloneNode(true);
            
                searchEntryCount++;
                clone.querySelector('select').id = `title-name-${searchEntryCount}`;
                clone.querySelector('input').id = `title-value-${searchEntryCount}`;
            
                container.appendChild(clone);
                container.appendChild(document.createElement('br')); 
            }
            

            function addSortEntry() {
                const container = document.getElementById('sort-container');
                const entry = document.querySelector('.sort-entry');
                const clone = entry.cloneNode(true);
            
                sortEntryCount++;
                clone.querySelector('[name="sort_titles[]"]').id = `sort-title-${sortEntryCount}`;
                clone.querySelector('[name="sort_values[]"]').id = `sort-value-${sortEntryCount}`;
            
                container.appendChild(clone);
                container.appendChild(document.createElement('br')); 
            }
      