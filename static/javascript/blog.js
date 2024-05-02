
function publishBlogPost(){
    const formData = new FormData();
    formData.append('title', title);
    formData.append('content', content);

    const csrftoken = document.querySelector('[name="csrfmiddlewaretoken"]').value;
    fetch("/publish_post/", {
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
         console.log(id)
         const csrftoken = document.querySelector('[name="csrfmiddlewaretoken"]').value;
         fetch("/delete_post/", {
            method: "POST",
            credentials: "same-origin",
            headers: {
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRFToken": csrftoken
            },
            body: JSON.stringify({blogObject: blogObject})
        })
        .then(response => {

        })
        .then(data => {
        });

    }
    else {
        text = "You canceled!";
  }
}

function publishProject(){
    const projectObject = {
        title: document.getElementById("projectPostTitle").value,
        imageUrl: document.getElementById("projectPostImageUrl").value,
        githubUrl: document.getElementById("projectPostGithub").value,
        content: document.getElementById("projectPostTextbox").value
    };
    const jsonData = JSON.stringify(projectObject);
    const csrftoken = document.querySelector('[name="csrfmiddlewaretoken"]').value;
    fetch("/publish_project/", {
      method: "POST",
      credentials: "same-origin",
      headers: {
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": csrftoken
      },
      body: jsonData
    })
    .then(response => {
        console.log(response);
    })
    .then(data => {
        console.log(data);
    });
}


function deleteProject(id){
    if (confirm("Are you sure you want to delete the post?") == true) {
         projectObject = {
            projectId: id
         }
         console.log(id)
         const csrftoken = document.querySelector('[name="csrfmiddlewaretoken"]').value;
         fetch("/delete_project/", {
            method: "POST",
            credentials: "same-origin",
            headers: {
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRFToken": csrftoken
            },
            body: JSON.stringify({projectObject: projectObject})
        })
        .then(response => {

        })
        .then(data => {
        });

    }
    else {
        text = "You canceled!";
  }
}
