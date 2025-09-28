const createPostForm = document.querySelector(".create-form");
const createBtn = document.querySelector(".add-a-post");

window.addEventListener("DOMContentLoaded", handleCreateBtn);

function handleCreateBtn() {
    createBtn.addEventListener("click", (e) => {
        e.preventDefault();

        const cancelBtn = document.querySelector(".cancel-create-post-btn");
        const userStatus = JSON.parse(
            window.localStorage.getItem("userstatus")
        );

        if (userStatus.authenticated) {
            createPostForm.classList.add("show-create-form");

            function handleFormBtns() {
                cancelBtn.addEventListener("click", (e) => {
                    createPostForm.classList.remove("show-create-form");
                });
            }
            handleFormBtns();
        } else {
            handleAlert(
                "error",
                "You are not logged in. Please login to add a post."
            );
        }
    });
}

async function handleCreateFormSubmit(event) {
    event.preventDefault();

    const url = `${window.location.origin}/create/post/`;
    const title = createPostForm.querySelector("input[name=title]").value;
    const body = createPostForm.querySelector("textarea[name=body]").value;
    const images = createPostForm.querySelector("input[name=image]").files;
    const newObj = { title: title, body: body, images: [] };
    const p = document.createElement("p");
    p.setAttribute("class", "input-error");

    for (const key in images) {
        if (typeof images[key] === "object") {
            newObj.images = [...newObj.images, images[key]];
        }
    }

    const formData = new FormData();

    for (let key in newObj) {
        if (key == "images") {
            newObj[key].forEach((obj) => {
                formData.append("image", obj);
            });
        } else {
            formData.append(key, newObj[key]);
        }
    }

    try {
        const resp = await fetch(url, {
            method: "POST",
            headers: { "X-CSRFToken": getCSRFToken("csrftoken") },
            body: formData,
        });
        const data = await resp.json();
        if (resp.ok) {
            handleNewPost(data);
            event.target.reset();
        } else {
            p.innerHTML = data.error;
            createPostForm.append(p);
        }
    } catch (error) {
        console.log(error.message);
    }
}

function handleNewPost(post) {
    const posts = document.querySelector(".posts");
    const newDate = new Date(post.created);
    const dateString = newDate.toDateString();
    const timeString = newDate.toLocaleTimeString(
        {},
        { hour: "2-digit", minute: "2-digit" }
    );

    const newPost = `<div class="post">
                        <div class="post-author-created">
                            <span class="post-author">${post.author}</span>
                            <span class="post-created">${dateString} ${timeString}</span>
                        </div>
                        <h3 class="post-title">${post.title}</h3>
                        <p class="post-body">${post.body}</p>
                        <div class="post-read-more">
                            <button id=${post.id} class="read-more-btn">Read more</button>
                        </div>
                    </div>
                `;
    posts.insertAdjacentHTML("afterbegin", newPost);
    createPostForm.classList.remove("show-create-form");
    handleAlert("success", post.message);
}
