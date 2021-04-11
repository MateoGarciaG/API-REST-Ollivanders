/* Generate Error Request HTML */
function errorMessage(message) {

    const listItems = document.querySelector('#list-items');

    listItems.innerHTML = `
    <div class="carta" id="error"> 
        <div class="contenido">  
            <div class="div-icon-user"> 
                <img src="{{ url_for('static',filename='img/error-404.jpg') }}" class="user-icon" alt="">
            </div>
            <h4> Error: ${message} </h4>
            <h5> Description: Al parecer la petición no ha funcionado </h5>
        </div>
    </div>
    `
}


/***********************************************************/

/* Get reference button of updatE_quality*/
const updateQualityButton = document.querySelector("#update_quality");
updateQualityButton.addEventListener("click", update_quality);


function update_quality() {


    /* const myRequest = new Request('/inventory', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
        mode: 'cors',
        cache: 'default',
    }); */

    var miHeaders = new Headers();

    var requestDetails = {
        method: 'GET',
        headers: miHeaders,
        mode: 'cors',
        cache: 'default'
    };

    fetch('http://127.0.0.1:5000/update_quality', requestDetails)
    .then((response) => {
        if(response.ok) {
            console.log("Response Status:", response.status);
            console.log("Reponse statuts text:", response.statusText);
            response.json().then((json) => loadItems(json))
        } else {
            console.log("Response Status:", response.status);
            console.log("Reponse statuts text:", response.statusText);  
        }  
    })
    .catch((error) => {
        //console.log(error.message);
        errorMessage(error.message);
    });
}






        /***********************************************/ 

    /* Get reference button of updatE_quality*/
    const inventoryButton = document.querySelector("#inventory");
    inventoryButton.addEventListener("click", inventory); 

    // Get stock
    function inventory() {


        /* const myRequest = new Request('/inventory', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
            mode: 'cors',
            cache: 'default',
        }); */

        var miHeaders = new Headers();

        var requestDetails = {
            method: 'GET',
            headers: miHeaders,
            mode: 'cors',
            cache: 'default'
        };

        fetch('http://127.0.0.1:5000/inventory', requestDetails)
        .then((response) => {
            if(response.ok) {
                console.log("Response Status:", response.status);
                console.log("Reponse statuts text:", response.statusText);
                response.json().then((json) => loadItems(json))
            } else {
                console.log("Response Status:", response.status);
                console.log("Reponse statuts text:", response.statusText);  
            }  
        })
        .catch((error) => {
            //console.log(error.message);
            errorMessage(error.message);
        });
}

    // Get stock items
    function loadItems(items) {

        const listItems = document.querySelector('#listitems');

        listItems.innerHTML = items.map((item, i) => {
            return `
                    <div class="carta" id="item${i}"> 
                    <div class="contenido">  
                        <div class="div-icon-user"> 
                            <img src="{{ url_for('static',filename='img/item_ollivanders.jpg') }}" class="user-icon" alt="">
                        </div>
                        <h4> Name: ${item.name} </h4> 
                        <h5> Sell in: ${item.sell_in} </h5> 
                        <h5> Quality: ${item.quality} </h5>
                    </div>
                </div>
                    `;
        }).join('');
    }