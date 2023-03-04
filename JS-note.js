
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
   // let data = '{{ data }}'
  // window.location.href = `https://www.google.com/search?q=${data}`
  // window.open(
 	//     `https://www.google.com/search?q=${data}`, '_blank'
 // )

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
