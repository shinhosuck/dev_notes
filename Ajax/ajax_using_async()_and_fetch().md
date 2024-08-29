# Ajax using async() and fetch() functions

```javascript

const postContainer = document.querySelector('.postContainer')

window.addEventListener('DOMContentLoaded', getPosts)

async function getPosts() {
    const numOfPageToShow = JSON.parse(localStorage.getItem('postID')) || 2
    const url = `posts/${numOfPageToShow}`

    try {
        const resp = fetch(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        const data = resp.json()
        if(resp.ok) {
            renderElements(data)
        }
        else {
            console.log({status:resp.status, message:resp.statusText})
        }
    }
    catch(error) {
        console.log(error.message)
    }
}

function renderElements(data) {
    const elements = data.posts.map((post)=> {
        return `
            <div class='post'>
                <h3>${post.title}</h3>
                <button id=${post.id} class="like-btn" type='button'>
                    <span>Likes</span>
                    <span>${post.likes}</span>
                </button>
            </div>
        `
    })
    postContainer += elements.join('')
    handleLikeBtnClickEvent()
}

function handleLikeBtnClickEvent() {
    const likeBtns = Array.from(document.querySelectorAll('.like-btn'))
    likeBtns.forEach((button)=> {
        button.addEventListener('click', (e)=> {
            const postID = e.currentTarget.id
            const body = {postID}
            updateLike(body)
        })
    })
}


// Fetch csrf_token
function getCookie(name) {
    const cookie = document.cookie.split(';').find((obj)=> obj.startsWith('csrftoken'))
    const token = cookie.split('=')[-1].join('')
    if (token):
        return decodeURIComponent(token)
    return null
}


async() function updateLike(body) {
    const cookie = getCookie('csrftoken')
    if (cookie){
        const url = 'updateLike/'
        try {
            const resp = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                    'X-CSRFToken': cookie
                },
                body: JSON.Stringify(body)
            })
            const data = await resp.json()
            console.log(data)
        }
        catch(error) {
            console.log(error.message)
        }
    }else {
        console.log('Token not available.')
    }
}

```

```python

def updateLike(request):
    type = request.headers.get('Content-Type')
    post_id = json.loads(request.body.decode('utf-8')).get('postID')

    if type == 'application/json':
        try:
            post = Post.objects.get(id=id)
        except Post.DoesNotExist:
             return JsonResponse(data={'error': 'Post not found.'}, status=400)
        post.liked.add(request.user)
        return JsonResponse(data={'message': 'successfully added.'}, status=200)
    else:
        return render(request, 'blog/posts.html', {})
```



