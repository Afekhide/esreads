let clicked = 0;
let span = document.getElementById('val').innerHTML = `${clicked++}`;

document.getElementById('btn').addEventListener('click', ev => {
    let url = `http://${location.host}/api/users`;
    let headers = new Headers();
    headers.set('ESREADS-API-KEY', '89-7862098'); // admin: 58-9654440, member: 89-7862098
    headers.set('Accept', 'application/json');

    let request_settings = {
        method: 'GET',
        mode: 'cors',
        cache: 'default',
        headers: headers
    };

    let request = new Request(url, request_settings);
    let users = fetch(request).then(response => response.json()).then(data => console.log(data));

});


