
function publishBlogPost(){
    title = document.getElementById("blogPostTitle").value;
    content = document.getElementById("blogPostTextbox").value;
    blogObject = {
        title: title,
        content: content
    }

    const csrftoken = document.querySelector('[name="csrfmiddlewaretoken"]').value;
    fetch("/blog/publish_post/", {
      method: "POST",
      credentials: "same-origin",
      headers: {
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": csrftoken
      },
      body: JSON.stringify({blogObject: blogObject})
    })
    .then(response => {
        console.log(response);
    })
    .then(data => {
      console.log(data);
    });
}


