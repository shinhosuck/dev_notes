1. useState()
2. useEffect()
3. useRef()
4. useReducer()
5. useLocation()
6. useLoaderData()
7. useRouterError()

8. useSearchParams():
const [searchParams, setSearchParams] = useSearchParams() -> <button onClick={()=>setSearchParams({category:'laptops'})}></button>. setSearchParams('yourFilter=whatever you are looking for')

9. State prop to Link:
const [searchParams, setSearchParams] = useSearchParams()
<Link to={`/product/${id}/detail`} state={{search:`?${searchParams.toString()}`}}>Detail</Link>

10. useConext() / need to create custom contextApi using 'createContext()'

11. propTypes - use to validate properties of an object. Checks if object's property exist or not.

12. custom hook -  function name starts with 'use', can use other builtin hooks inside the custom hook.

13. useParams() - use for retrieving param from <Route path='/person/:id/detail/' /> - id or string.

14. Navigate () => {return <Navigate to='/login' replace={true} state={{message:'hello'}}/>} -> also here like the Link or NavLink, can pass state={{message:'hello world}}

15. NavLink <NavLink className={(isActive)=>isActive ? 'active-link' : 'nav-link'}></NavLink>

16. Outlet

17. useOutletContext / in the <Outlet context={}> pass obj to the cotext.

18. end / <NavLink to='/description' end>Description</NavLink> end is used when you don't want the activeNavLink to match the parentLayout.

19. relative='path' /<NavLink to='..' relative='path'></NavLink> going back to previous route, on default .. takes back to parent route. relative='path' previous path. 

20. dot(.) on <NavLink to='.'><NavLink> / dot(.) on NavLink or Link represents current path.

<!-- LOADER / <Route  loader={} />  -->
When the loader is passed to a <Route loader={}/>, the the function in the loader gets called first, the function checks the neccessary condition or performs given task before the component get loaded. If the given task in the function returns 'false', the component will not laod.

21. redirect() / used with custom loader function:  
    export const userLoader = async() => {
        const userAuth = JSON.parse(localStorage.getItem('auth'))
        if(userAuth) {
            return redirect('/products')
        }
        return ''
    }
    PS: loader function can receive arguments such as params or request.


<!-- REACT FORM /Action -->
22. 

import { Form, useActionData } from 'react-router-dom'

export const action = async(obj) => {
    const { request, params } = obj
    const formData = request.formData()
    const username = formData.get('username)
    const password = formData.get('password')
    
    try {
        const data = await authenticateUser({username:username, password:password})
        if(data.error){
            throw 'Username or password did not match'
        }
        return redirect('/products')
    }
   catch(error) {
        return error
   }

}
<Form method='POST' replace={true}>
</Form>

<Route action={action}/>


23. useNavigation()

24. useNavigate('/product', {replace:true}) / this can be only used inside to a component

25. window.history.replaceState({state:null}, '', '/login') => third parameter must be current url
