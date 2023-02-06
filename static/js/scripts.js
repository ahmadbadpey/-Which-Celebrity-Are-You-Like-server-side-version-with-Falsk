const upload_form = document.getElementById('upload_form')
const user_file = document.getElementById('user_file')
const s_btn = document.getElementById('s_btn')

upload_form.addEventListener('submit', e => {
    e.preventDefault()
    uploadFile()
        .then(r => {
            console.log(r)
            getPredict(r.message)
        })
})

user_file.addEventListener('change', () => {
    s_btn.click()
})

async function uploadFile() {
    let formData = new FormData()
    let resp = null;
    formData.append('file', user_file.files[0])

    await fetch('/upload', {
        method: 'POST',
        body: formData
    })
        .then(response => {
            resp = response.json()
        })
        .catch(error => {
            alert("HTTP-Error: " + error.status);
        })

    return resp
}

function getPredict(image) {
    fetch('/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'image' : image
        })
    })
        .then(r => {
            console.log(r)
        })
        .catch(e => {
            console.log(e)
        })
}