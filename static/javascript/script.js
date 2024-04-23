


function loadRatingButtons(){
    buttons = document.querySelectorAll(".btn-scale");
    buttons.forEach(button => {
      button.addEventListener("click", function() {
        buttons.forEach(btn => btn.style.outline = "none");
        this.style.outline = "2px solid black";
      });
    });
}

function submitRating(){
    selectedButtonId = 0;
    buttons = document.querySelectorAll(".btn-scale");
    buttons.forEach(button => {
        if (button.style.outline === "black solid 2px") {
            selectedButtonId = button;
        }
        else{
        }
    });
    catRatingValue =  selectedButtonId.value

    catObject = {
        catRating: catRatingValue,
        catId: document.getElementById("id_cat").value
    }
    console.log(selectedButtonId.value)

    const csrftoken = document.querySelector('[name="csrfmiddlewaretoken"]').value;

    fetch("/rate_cat/", {
      method: "POST",
      credentials: "same-origin",
      headers: {
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": csrftoken
      },
      body: JSON.stringify({catObject: catObject})
    })
    .then(response => {
        document.getElementById("cardRating").textContent = "Rating: " + catRatingValue
    })
    .then(data => {
      console.log(data);
    });
}

function changeName(){
    input = document.getElementById("changeCatName").value;
    console.log(input)
    catObject = {
        name: input,
        catId: document.getElementById("id_cat").value
    }

    const csrftoken = document.querySelector('[name="csrfmiddlewaretoken"]').value;

    fetch("/change_cat_name/", {
      method: "POST",
      credentials: "same-origin",
      headers: {
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": csrftoken
      },
      body: JSON.stringify({catObject: catObject})
    })
    .then(response => {
        document.getElementById("cardName").textContent = input
    })
    .then(data => {
      console.log(data);
    });
}


