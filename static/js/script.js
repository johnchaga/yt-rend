function downloadVideo() {
    const url = document.getElementById('url').value;
    const format = document.getElementById('format').value;

    if (url === '') {
        alert('Please enter a YouTube video URL');
        return;
    }

    const message = document.getElementById('message');
    message.textContent = 'Processing your download...';

    // Send a request to the backend to process the download
    fetch('/download', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url, format })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            message.innerHTML = `<a href="${data.fileUrl}" download>Click here to download your file</a>`;
        } else {
            message.textContent = 'An error occurred. Please try again.';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        message.textContent = 'An error occurred. Please try again.';
    });
}
