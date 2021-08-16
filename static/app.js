const form = document.getElementById('cupcake-form');
const cupcakes = document.getElementById('cupcake-container');


async function getCupcakeList(){
    res = await axios.get('/api/cupcakes');
    for (cupcake of res.data.cupcakes){
        renderCupcake(cupcake);
    }
}

function renderCupcake(cupcake){
    const element = $(`<div>
    <img width=auto height=200 src="${cupcake.image}" alt="Photo of Cupcake ${cupcake.id}">
    <p>Flavor: ${cupcake.flavor}<br>
    Size: ${cupcake.size}<br>
    Rating: ${cupcake.rating}/10</p>
    </div>`);

    element.appendTo(cupcakes);
}

async function createCupcake(data){
    res = await axios.post('/api/cupcakes', data=data);
    return res.data.cupcake;
}

form.addEventListener('submit', async function(e){
    e.preventDefault();
    data = {
        flavor : form.flavor.value ? form.flavor.value : null,
        size : form.size.value ? form.size.value : null,
        rating : form.rating.value || form.rating.value === 0 ? form.rating.value : null,
        image : form.image.value ? form.image.value : null,
    }
    newCupcake = await createCupcake(data);
    renderCupcake(newCupcake);
});

getCupcakeList();