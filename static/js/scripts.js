document.getElementById('downloadForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const videoUrl = document.getElementById('videoUrl').value;
    const downloadType = document.getElementById('downloadType').value;
    const formatSelect = document.getElementById('formatSelect');
    const downloadButton = document.getElementById('downloadButton');

    const response = await fetch('/get_formats', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url: videoUrl, download_type: downloadType }),
    });
    const data = await response.json();

    if (data.formats) {
        formatSelect.innerHTML = data.formats
            .map(f => `<option value="${f.format_id}">${f.format_note || f.ext}</option>`)
            .join('');
        formatSelect.disabled = false;
        downloadButton.classList.remove('hidden');
    }
});
