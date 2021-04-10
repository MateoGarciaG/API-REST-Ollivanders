

/* Generate Item HTML */



/* Generate Error Request HTML */
function errorMessage(message) {

    const listItems = document.querySelector('#list-items');

    listItems.innerHTML += `
    <div class="carta" id="${nombreUsuario}"> 
        <div class="contenido">  
            <div class="div-icon-user"> 
                <img src="../resources/svg/user_icon.svg" class="user-icon" alt="">
            </div>
            <h4> Error: ${message} </h4>
            <h5> Description: Al parecer la petición no ha funcionado </h5>
        </div>
    </div>
    `
}

/* Get reference button of updatE_quality*/
const updateQualityButton = document.querySelector("#update_quality");
updateQualityButton.addEventListener("click", update_quality);

function update_quality() {
    // var headers = new Headers();

    var requestDetails = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
        mode = 'cors',
        cache: 'default'
    };

    fetch('http://127.0.0.1:5000/update_quality', requestDetails)
    .then( (response) => {
        if(response.ok) {
            response.json().then( (json) => loadItem(json) )
        } else {
            console.log("Response Status:", response.status);
            console.log("Reponse statuts text:", response.statusText); 
        }
    } )
    .catch( (error) => 
    {
        errorMessage(error.message);
    }
    );

}