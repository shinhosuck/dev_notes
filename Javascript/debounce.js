function parent(){
    function wrapper() {
        let id;
        return (e) => {
            clearTimeout(id)

            id = setTimeout(()=> {
                console.log('hello world')
            }, 1000)
        }
    }
    inputs.forEach((input) => {
        input.addEventListener('click', wrapper())
    })
}
parent()
