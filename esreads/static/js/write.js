
let publishButton = document.querySelector('.top-right-btn');
let story_title_input = document.getElementById('title-field');
let story_content_input = document.getElementById('content-field');

let titleLabel = document.querySelector("label[for = 'title-field']");
let contentLabel = document.querySelector("label[for = 'content-field']");


story_title_input.addEventListener('keyup', evt => {
    (story_title_input.value.trim().length === 0) ? titleLabel.style.visibility = 'hidden' : titleLabel.style.visibility = 'visible';
});

story_content_input.addEventListener('keyup', evt => {
    (story_content_input.value.trim().length === 0) ? contentLabel.style.visibility = 'hidden' : contentLabel.style.visibility = 'visible';
});


publishButton.addEventListener('click', (evt => {
    evt.preventDefault();
    let story_content = story_content_input.value.trim();
    let story_title = story_title_input.value.trim();
    if ((story_content.length < 5) || (story_title.length < 3)){
        window.alert(`The content or title of this story is short`);
        return
    }

    let api_url = `http://${window.location.host}/api/posts/`;
    let headers = new Headers();
    headers.set('ESREADS-API-KEY', '90-1827567');
    headers.set('Content-Type', 'application/json');
    let request = new Request(api_url, {
        'method': 'POST',
        'redirect': "follow",
        'headers': headers,
        'body': JSON.stringify({
            'title': story_title,
            'content': story_content
        })
    });

    fetch(request) .then(res => res.json()) .then(data => console.log(data))
    
}));


