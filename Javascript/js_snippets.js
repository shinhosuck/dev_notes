// loop FormData()
 for (const obj of formData.entries()) {
    console.log(obj)
}

// Get csrf token from the django form
const csrf = document.getElementsByName('csrfmiddlewaretoken')
console.log(csrf[0].value)

 // searchParams
 const url = new URL(document.URL)
 const search = url.searchParams.get('q')
 // searchParams = URLSearchParams()
 or
 const url = document.URL
 const newUrl = new URL(url)
 const search = newUrl.searchParams.get('q');

 // location of the scroll bar
window.addEventListener('scroll', function(){
    console.log(window.pageYOffset)
})

// full html document height
console.log('Document Height:', document.body.scrollHeight)

// windows view port height (vh)
console.log('Window View Port Height:', window.innerHeight)

// element offset height
console.log('Main First Child Offset Height', main.children[0].offsetHeight)

// element client height
console.log('Main First Child Client Height', main.children[0].clientHeight)

// window innerHeight and innerWidth
console.log(window.innerHeight)

// redirect to new url
   let data = 'dog'
  window.location.href = `https://www.google.com/search?q=${data}`
  window.open(`https://www.google.com/search?q=${data}`, '_blank')

  // removes nav items when clicked on window
    window.addEventListener("click", function(event){
        if(navItems.classList.contains("show-nav-items")) {
            if(event.target == navOpenBtn || event.target == barsBtn
                || event.target == navCloseBtn || event.target == closeBtn) {
                console.log("do nothing")
            }
            else{
                navItems.classList.remove("show-nav-items")
                navOpenBtn.style.display = "flex"
                navCloseBtn.style.display = "none"
            }
        }
    })

// DOMContentLoaded => only when DOM content is loaded without css, images, and etc.
window.addEventListener('DOMContentLoaded', function(){
    console.log('window loaded')
})

//load => when DOM content loaded including css, images, and etc.
window.addEventListener('laod', function(){
    console.log('window loaded')
})

/*=====USEFUL METHODS=====*/
window.scrollTo() => takes 2 arguments (x, y) or just {top:value} or {left:value}
map()
filter()
reduce()
find()
join('')
includes()
contains() // check if a node, childnode, childnode's childnode and so forth are in.
slice()
split()
splice(index, num_of_item_to_remove)
delete someArray[index]
pop() -> removes from end of an array
shift() -> removes from start of an array
const year = new Date().getFullYear()
push() -> adds to end of an array
unshift() -> adds to beginning of an array
new Set()
substr(0, 100)
replaceAll(' ','')
firstElementChild
lastElementChild
peviousElementSibling
nextElementSibling
parentElement
children
onclick
onsubmit
window.location.reload()
window.location -> gives location object
Object.keys()
Object.values()
Object.assign(target, source)
items.indexOf(item)
new Boolean()
focus()
typeof
someValue instanceof Object
sort()
Array.from()
console.dir(obj)
toFixed(2) -> similar to python round()
window.addEventListener('DomContentLoaded', loadContent) -> as soon as the DOM loads, loadContent will be invoked.
createDocumentFragment() -> use this with document.createElement(), append the element to, similar to React.Fragment
await Promise.all(ids.map((id)=>getPosts(id))) -> this gets all the promises at once,but one fails, all fails
await Promise.allSettled(ids.map((id)=>getPosts(id))) -> this get all the promises at once,failed items are omitted.
Array.isArray(someValue)

const path = e.composedPath()
path.some((element)=>console.log(element))
window.history.replaceState({state: null}, '', 'sign-in')

const ele = document.createElement('div')
const content = document.createTextNode('hello world')
append()
prepend()
insertBefore()
scrollIntoView()

// HISTORY OBJECT
history.back() -> history object back() method -> go back to previous page
history.pushState()
history.replaceState()

container.insertAdjacentHTML('afterbegin', alertMessage) -> inserts alertMessage html element beginning of the container

const newItems = [...new Set(menu.map((item)=> {
        return item.category
    }))]

// get month/date/year
const getMonthDateYear = function() {
    const data = new Date()
    const result = `${data.getMonth()+1}/${data.getDate()}/${data.getFullYear()}`
    console.log(result)
}
// getMonthDateYear()


const linksContainer = document.querySelector('.nav-links-container')

const navHeight = linksContainer.getBoundingClientRect().height
// console.log(navHeight)

// distance from top to the element
let position = element.offsetTop

// used with hre='#main-container'
// scroll down button
scrollDownBtn.addEventListener('click', function(e){
    e.preventDefault()
    const elementId = e.currentTarget.getAttribute('href').slice(1)
    const element = document.querySelector(`#${elementId}`)
    const position = element.offsetTop
    window.scrollTo({left:0, top:position-83})
})


// error when importing a module
`caught SyntaxError: Cannot use import statement`

// need to set type='module'
`<script type='module' src="./main.js"></script>`


// Fetch Data
const url = 'https://course-api.com/react-tabs-project'
const FetchData = async()=> {
    const response = await fetch(url)
    const data = await response.json()
    console.log(data)
}
FetchData()


// Get Random Number
const randomNum = Math.floor(Math.random()*1000000)

// Get formatted year, month, day, date, and time
const date = Date();
let d = new Date(Date.parse(date));
console.log(d.toDateString(),d.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'}));

// Document loaded
document.readyState === 'complete'

// for(const i in obj) && for(const i of arrayObjs)
const obj = { name: "jack", age: 33 };
const arrayObj = [1, 2, 3, 4, 5];

// dictionary/Obj
for (const i in obj) {
    console.log(obj[i]);
}

// list/array obj
for (const i of arrayObj) {
    console.log(i);
}









