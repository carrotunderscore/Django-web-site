
function publishBlogPost(){
    title = document.getElementById("blogPostTitle").value;
    content = document.getElementById("blogPostTextbox").value;
    if(typeof title === "string" && title.length === 0 || typeof content === "string" && content.length === 0){
        alert("Title and content can not be empty")
    }else{
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
            window.location.href = '/';
        })
        .then(data => {
            console.log(data);
            window.location.href = '/';
        });
    }
}


function deletePost(id){
    if (confirm("Are you sure you want to delete the post?") == true) {
         blogObject = {
            blogPostId: id
         }
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
            window.location.href = '/';
        })
        .then(data => {
             window.location.href = '/';
        });

    }
    else {
        text = "You canceled!";
  }
}

function publishProject(){
    title = document.getElementById("projectPostTitle").value;
    content = document.getElementById("projectPostTextbox").value;
    if(typeof title === "string" && title.length === 0 || typeof content === "string" && content.length === 0){
        alert("Title and content can not be empty")
    }else{
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
            window.location.href = '/projects';
        })
        .then(data => {
            console.log(data);
            window.location.href = '/projects';
        });
    }

}


function deleteProject(id){
    if (confirm("Are you sure you want to delete the post?") == true) {
         projectObject = {
            projectId: id
         }
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
            window.location.href = '/projects';
        })
        .then(data => {
             window.location.href = '/projects';
        });

    }
    else {
        text = "You canceled!";
  }
}
