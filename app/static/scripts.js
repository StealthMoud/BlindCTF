// Fetch the status of an item and update the DOM
async function fetchItemStatus(itemId) {
    const itemElement = document.getElementById(`item-${itemId}`);
    itemElement.classList.add('loading');
    itemElement.textContent = `Loading item ${itemId}...`;

    try {
        const response = await fetch(`/get_item?id=${itemId}`);
        const data = await response.json();

        if (data.result) {
            itemElement.textContent = `Item ${itemId}: ${data.result}`;
            itemElement.classList.remove('loading');
            itemElement.classList.add('success');
        } else {
            itemElement.textContent = `Item ${itemId}: Not Found`;
            itemElement.classList.remove('loading');
            itemElement.classList.add('error');
        }
    } catch (error) {
        itemElement.textContent = `Item ${itemId}: Error retrieving status`;
        itemElement.classList.remove('loading');
        itemElement.classList.add('error');
    }
}

// Fetch statuses for all items on page load
document.addEventListener('DOMContentLoaded', () => {
    const itemIds = [1, 2, 3]; // Example item IDs
    itemIds.forEach(fetchItemStatus);
});
