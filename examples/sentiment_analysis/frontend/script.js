const socket = new WebSocket("ws://localhost:8765");

socket.onmessage = function(event) {
    const data = JSON.parse(event.data);
    const postsDiv = document.getElementById("posts");
    const postDiv = document.createElement("div");
    postDiv.className = `post ${data.sentiment.label}`;
    postDiv.innerHTML = `
        <p><strong>${data.post.author}</strong></p>
        <p>${data.post.text}</p>
        <p>Sentiment: ${data.sentiment.label} (${data.sentiment.score.toFixed(2)})</p>
    `;
    postsDiv.prepend(postDiv);
};
