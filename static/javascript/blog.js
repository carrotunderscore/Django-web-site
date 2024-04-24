
function publishBlogPost(){
    title = document.getElementById("blogPostTitle").value;
    content = document.getElementById("blogPostTextbox").value;
    blogObject = {
        title: title,
        content: content
    }
    const formData = new FormData();
    formData.append('title', title);
    formData.append('content', content);


    const csrftoken = document.querySelector('[name="csrfmiddlewaretoken"]').value;
    fetch("/blog/publish_post/", {
      method: "POST",
      credentials: "same-origin",
      headers: {
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": csrftoken
      },
      body: formData
    })
    .then(response => {
        console.log(response);
    })
    .then(data => {
      console.log(data);
    });
}


function deletePost(id){
    if (confirm("Are you sure you want to delete the post?") == true) {
         blogObject = {
            blogPostId: id
         }

         const csrftoken = document.querySelector('[name="csrfmiddlewaretoken"]').value;
         fetch("/blog/delete_post/", {
            method: "POST",
            credentials: "same-origin",
            headers: {
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRFToken": csrftoken
            },
            body: JSON.stringify({blogObject: blogObject})
        })
        .then(response => {
            location.reload()
        })
        .then(data => {
        });

    }
    else {
        text = "You canceled!";
  }
}


